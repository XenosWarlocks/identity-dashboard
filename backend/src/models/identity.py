from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import re

class Identity(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50, example="John")
    last_name: str = Field(..., min_length=2, max_length=50, example="Doe")
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., min_length=8, example="Password123!")

    @classmethod
    def validate_password(cls, password: str) -> str:
        """Custom validator for password complexity"""
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            raise ValueError("Password must be at least 8 characters long and include letters and numbers")
        return password
    
    @classmethod
    def create_identity(cls, first_name: str, last_name: str, email: str, password: str) -> "Identity":
        """Factory method to create an identity instance with validation."""
        cls.validate_password(password)
        return cls(first_name=first_name, last_name=last_name, email=email, password=password)

class IdentityResponse(BaseModel):
    identity: Identity
    message: Optional[str] = Field(default="Identity created successfully", example="Identity created successfully")

    class Config:
        schema_extra = {
            "example": {
                "identity": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com",
                    "password": "Password123!"
                },
                "message": "Identity created successfully"
            }
        }