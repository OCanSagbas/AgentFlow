from langchain.agents import create_agent
from AI.llms import get_gemini_model
from AI.tools import (document_tools)


def get_document_agent(model=None, checkpointer=None):

    llm_model = get_gemini_model(model=model) 
    
    agent = create_agent(
    model=llm_model,
    tools=document_tools,
    system_prompt="You are a helpful assistant. You have access to document management tools. Use these tools when users ask about their documents, but feel free to answer other questions using your general knowledge.",
    checkpointer=checkpointer,
    )
    return agent
