# AgentFlow

An intelligent multi-agent Django application powered by LangGraph and Google Gemini, featuring role-based access control and specialized AI agents for document management and movie discovery.

## 🌟 Features

- **Multi-Agent Supervisor System**: Intelligent routing between specialized agents using LangGraph
- **Document Management Agent**: Full CRUD operations with permission-based access control
- **Movie Discovery Agent**: Integrated TMDB API for movie search and detailed information
- **Role-Based Access Control (RBAC)**: Powered by Permit.io for fine-grained permissions
- **AI-Powered Intelligence**: Google Gemini LLM for natural language understanding
- **Interactive Development**: Jupyter notebooks for experimentation and testing

## 🏗️ Architecture

```
User Request
     ↓
Supervisor Agent (Router)
     ↓
  ┌──┴──┐
  ↓     ↓
Document  Movie
Agent     Agent
```

The supervisor agent intelligently routes user requests to the appropriate specialized agent based on the query context.

## 🚀 Quick Start
### Prerequisites

- Python 3.12+
- Django 5.0+
- Google Gemini API Key
- TMDB API Key
- Permit.io API Key

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd DJANGO-AI-AGENT
```

2. **Create and activate virtual environment**
```bash
python -m venv venv_aiagent
source venv_aiagent/bin/activate  # Linux/Mac
# or
venv_aiagent\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the `src` directory:
```env
# Django
SECRET_KEY=your-django-secret-key
DEBUG=True

# Google Gemini
GOOGLE_API_KEY=your-gemini-api-key

# TMDB API
TMDB_API_KEY=your-tmdb-api-key

# Permit.io
PERMIT_API_KEY=your-permit-api-key
PERMIT_PDP_URL=https://cloudpdp.api.permit.io
```

5. **Run migrations**
```bash
cd src
python manage.py migrate
```

6. **Create a superuser**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

## 📁 Project Structure

```
DJANGO-AI-AGENT/
├── src/
│   ├── AI/
│   │   ├── agents.py           # Agent definitions
│   │   ├── supervisors.py      # Supervisor routing logic
│   │   ├── llms.py            # LLM configurations
│   │   └── tools/
│   │       ├── documents.py    # Document management tools
│   │       └── movie_discovery.py  # Movie discovery tools
│   ├── documents/             # Document app
│   ├── cfehome/              # Django project settings
│   ├── mypermit/             # Permit.io client
│   └── tmdb/                 # TMDB API client
├── notebook/                 # Jupyter notebooks for testing
└── requirements.txt
```

## 🤖 Agents

### Document Agent
Manages document operations with permission checks:
- **Search documents**: Query-based document search
- **Create document**: Add new documents
- **Read document**: Retrieve document details
- **Update document**: Modify existing documents  
- **Delete document**: Remove documents

### Movie Discovery Agent
Provides movie information via TMDB API:
- **Search movies**: Find movies by title/keyword
- **Movie details**: Get comprehensive movie information including ratings, cast, and synopsis

## 🔐 Permissions & Roles

The system uses Permit.io for RBAC with the following default roles:

### Manager Role
- Full document access (read, create, update, delete)
- Movie discovery access (search, detail)

### Viewer Role
- Read-only document access
- Movie discovery access (search, detail)

Configure roles and permissions in the Permit.io dashboard or via the API.

## 📓 Jupyter Notebooks

Explore the `notebook/` directory for interactive examples:

- `1-django-users-perms.ipynb` - User and permission basics
- `3-langgraph-django-tools.ipynb` - LangGraph integration
- `5-ai-agent.ipynb` - Agent implementation
- `6-memory-agent.ipynb` - Agent memory management
- `7-agent-crud.ipynb` - CRUD operations with agents
- `9-movie-discovery-ai-agent.ipynb` - Movie agent examples
- `10-multiagent.ipynb` - Multi-agent system
- `11-roles-and-permissions.ipynb` - RBAC configuration

## 🛠️ Usage Examples

### Using the Supervisor Agent

```python
from AI.supervisors import get_supervisor
from langchain_core.messages import HumanMessage

supervisor = get_supervisor()

# Document query
response = supervisor.invoke({
    "messages": [HumanMessage(content="Show me my recent documents")]
}, config={"configurable": {"user_id": "user_123"}})

# Movie query
response = supervisor.invoke({
    "messages": [HumanMessage(content="Find movies about space exploration")]
}, config={"configurable": {"user_id": "user_123"}})
```

### Direct Agent Usage

```python
from AI.agents import get_document_agent, get_movie_discovery_agent

# Document agent
doc_agent = get_document_agent()
result = doc_agent.invoke({
    "messages": [HumanMessage(content="List my documents")]
}, config={"configurable": {"user_id": "user_123"}})

# Movie agent
movie_agent = get_movie_discovery_agent()
result = movie_agent.invoke({
    "messages": [HumanMessage(content="Search for Inception")]
}, config={"configurable": {"user_id": "user_123"}})
```

## 🔧 Configuration

### LLM Model

Configure the Gemini model in `AI/llms.py`:
```python
def get_gemini_model(model=None):
    return ChatGoogleGenerativeAI(
        model=model or "gemini-2.0-flash-exp",
        temperature=0.7
    )
```

### Supervisor Routing

Customize routing logic in `AI/supervisors.py` by modifying the `ROUTER_SYS` message and decision logic.

## 📦 Dependencies

- **Django 5.0+** - Web framework
- **LangGraph** - Agent orchestration
- **LangChain** - LLM framework
- **Google Generative AI** - LLM provider
- **Permit.io** - Authorization as a service
- **TMDB API** - Movie database
- **Jupyter** - Interactive development

## 🧪 Testing

Run Django tests:
```bash
python manage.py test
```

Use Jupyter notebooks for interactive testing and experimentation.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration
- [Google Gemini](https://ai.google.dev/) for AI capabilities
- [Permit.io](https://permit.io) for authorization management
- [TMDB](https://www.themoviedb.org/) for movie data

Built with ❤️ using Django, LangGraph, and AI
