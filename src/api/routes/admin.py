from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.api.services.admin_service import set_active_index

router = APIRouter()

class SetActiveIndexRequest(BaseModel):
    version: str

@router.post("/set_active_index")
def set_active_index_endpoint(request: SetActiveIndexRequest):
    """Endpoint to set the active FAISS index version."""
    success = set_active_index(request.version)
    if not success:
        raise HTTPException(status_code=404, detail="FAISS index version not found or failed to load.")
    return {"message": f"Active FAISS index set to version: {request.version}"}
