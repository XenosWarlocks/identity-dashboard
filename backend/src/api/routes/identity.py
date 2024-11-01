from fastapi import APIRouter, HTTPException
from backend.src.models.identity import IdentityResponse
from backend.src.services.identity_generator import IdentityGenerator

router = APIRouter()

@router.post("/create-identity", response_model=IdentityResponse)
async def create_identity(culture: str = 'christian'):
    try:
        generator = IdentityGenerator(culture=culture)
        identity = generator.create_identity()
        return identity
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))