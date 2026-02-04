from documents.models import Document
from langchain_core.tools import tool

@tool
def list_documents():
    """
    Get Document for the current user
    """
    qs = Document.objects.filter(active=True)
    response_data = []

    for obj in qs:
        response_data.append({
            "id": obj.id,
            "title": obj.title,
        })
    return response_data

@tool
def get_document(document_id: int):
    """
    Get Document by ID
    """
    try:
        obj = Document.objects.get(id=document_id, active=True)
        return {
            "id": obj.id,
            "title": obj.title,
        }
    except Document.DoesNotExist:
        return {"error": "Document not found."}