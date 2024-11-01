from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uuid
from datetime import datetime

# Import your IdentityGenerator class
from identity_generator import IdentityGenerator

app = FastAPI()

# Configure CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store generated identities in memory (replace with database in production)
identities = {}

class IdentityRequest(BaseModel):
    culture: str = 'christian'
    password_length: Optional[int] = 16

class GmailAccountRequest(BaseModel):
    headless: Optional[bool] = False
    recovery_email: Optional[str] = None
    recovery_phone: Optional[str] = None

class Identity(BaseModel):
    id: str
    created_at: datetime
    culture: str
    name: str
    first_name: str
    middle_name: str
    last_name: str
    email: str
    password: str
    gmail_created: bool = False
    gmail_creation_attempted: bool = False

@app.post("/api/identities", response_model=Identity)
async def create_identity(request: IdentityRequest):
    try:
        generator = IdentityGenerator(
            culture=request.culture,
            password_length=request.password_length
        )
        identity = generator.create_identity()

        # Add metadata
        identity_id = str(uuid.uuid4())
        identity['id'] = identity_id
        identity['created_at'] = datetime.now()
        identity['gmail_created'] = False
        identity['gmail_creation_attempted'] = False

        # Store in memory
        identities[identity_id] = identity

        return identity
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/identities", response_model=List[Identity])
async def get_identities():
    return list(identities.values())

@app.post("/api/identities/{identity_id}/gmail", response_model=Identity)
async def create_gmail_account(identity_id: str, request: GmailAccountRequest):
    if identity_id not in identities:
        raise HTTPException(status_code=404, detail="Identity not found")
    
    identity = identities[identity_id]

    if identity['gmail_creation_attempted']:
        raise HTTPException(
            status_code=400, 
            detail="Gmail account creation already attempted"
        )
    
    try:
        generator = IdentityGenerator(culture=identity['culture'])
        generator.identity = identity
        
        success = generator.create_gmail_account(
            headless=request.headless,
            recovery_email=request.recovery_email,
            recovery_phone=request.recovery_phone
        )

        # Update identity status
        identity['gmail_creation_attempted'] = True
        identity['gmail_created'] = success
        identities[identity_id] = identity

        return identity
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)