from typing import TypedDict, Literal, List
from langchain_core.messages import BaseMessage, SystemMessage, AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command

from AI import agents
from AI.llms import get_gemini_model


class State(TypedDict):
    messages: List[BaseMessage]


def get_supervisor(model=None, checkpointer=None):
    llm = get_gemini_model(model=model)

    document_agent = agents.get_document_agent(model=model, checkpointer=checkpointer)
    movie_agent = agents.get_movie_discovery_agent(model=model, checkpointer=checkpointer)

    ROUTER_SYS = SystemMessage(content=(
        "Return one of these three words: document, movie, or finish.\n"
        "- Documents / recent documents / list / CRUD operations => document\n"
        "- Movie search/recommendations/information => movie\n"
        "- Agent has responded and no new task pending => finish"
    ))

    def supervisor(state: State, config: RunnableConfig) -> Command[Literal["document", "movie", END]]:
        last_message = state["messages"][-1]
        
        # Agent'tan cevap geldiyse ve tool call yoksa bitir
        if isinstance(last_message, AIMessage) and not last_message.tool_calls:
            if last_message.name in ["document-assistant", "movie-discovery-assistant"]:
                return Command(goto=END)
        
        decision = llm.invoke([ROUTER_SYS] + state["messages"][-8:], config=config).content.strip().lower()
        
        if "finish" in decision:
            goto = END
        elif "document" in decision:
            goto = "document"
        else:
            goto = "movie"
        
        return Command(goto=goto)

    def document_node(state: State, config: RunnableConfig) -> Command[Literal["supervisor"]]:
        out = document_agent.invoke(state, config=config)
        return Command(goto="supervisor", update={"messages": out["messages"]})

    def movie_node(state: State, config: RunnableConfig) -> Command[Literal["supervisor"]]:
        out = movie_agent.invoke(state, config=config)
        return Command(goto="supervisor", update={"messages": out["messages"]})

    g = StateGraph(State)
    g.add_node("supervisor", supervisor)
    g.add_node("document", document_node)
    g.add_node("movie", movie_node)
    g.add_edge(START, "supervisor")

    return g.compile(checkpointer=checkpointer)