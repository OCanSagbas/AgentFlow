from documents.models import Document
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
@tool
def list_documents(config: RunnableConfig):
    """
    Get Document for the current user
    """
    print(config)
    metadata = config.get("metadata") or config.get("configurable")
    user_id = metadata.get("user_id")
    qs = Document.objects.filter(active=True)
    response_data = []

    for obj in qs:
        response_data.append({
            "id": obj.id,
            "title": obj.title,
        })
    return response_data

@tool
def get_document(document_id: int, config: RunnableConfig ):
    """
    Get Document by ID
    """
    metadata = config.get("metadata") or config.get("configurable")
    user_id = metadata.get("user_id")
    if user_id is None:
        raise Exception("Invalid request for the user.")
    try:
        obj = Document.objects.get(id=document_id, owner_id=user_id, active=True)
    except Document.DoesNotExist:
        raise Exception("Document not found.")
    except:
        raise Exception("invalid request for a document detail.")
    response_data={
        "id": obj.id,
        "title": obj.title,
    }
    return response_data