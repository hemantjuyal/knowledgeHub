from fastapi import APIRouter
from src.api.schemas.query import QueryRequest, QueryResponse
from src.api.services.query_service import process_query

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_endpoint(request: QueryRequest):
    """Endpoint to handle user queries."""
    answer = process_query(request.query)
    return {"answer": answer}
