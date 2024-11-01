import pytest
from pydantic import ValidationError
from fastapi.testclient import TestClient
from backend.src.models.identity import Identity
from backend.src.api.main import app

client = TestClient(app)

# Sample data for testing
valid_identity_data = {
    "username": "testuser",
    "email": "testuser@example.com",
    "age": 30
}

invalid_identity_data = {
    "username": "us",  # Too short username
    "email": "invalid-email",  # Invalid email format
    "age": -5  # Invalid age
}

# Test Cases for Identity Model Validation
def test_identity_model_with_valid_data():
    """Test that valid data creates an Identity instance."""
    identity = Identity(**valid_identity_data)
    assert identity.username == "testuser"
    assert identity.email == "testuser@example.com"
    assert identity.age == 30


def test_identity_model_with_invalid_data():
    """Test that invalid data raises a ValidationError."""
    with pytest.raises(ValidationError):
        Identity(**invalid_identity_data)


# Test API Endpoints if Defined
def test_create_identity():
    """Test creating an identity with valid data."""
    response = client.post("/identity", json=valid_identity_data)
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"
    assert "id" in response.json()  # Assuming an ID is returned

def test_create_identity_with_invalid_data():
    """Test creating an identity with invalid data."""
    response = client.post("/identity", json=invalid_identity_data)
    assert response.status_code == 422  # 422 Unprocessable Entity for validation errors


def test_get_identity():
    """Test retrieving an identity by ID."""
    # First, create an identity
    create_response = client.post("/identity", json=valid_identity_data)
    identity_id = create_response.json().get("id")

    # Then, retrieve the created identity
    response = client.get(f"/identity/{identity_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"


def test_update_identity():
    """Test updating an existing identity."""
    # First, create an identity
    create_response = client.post("/identity", json=valid_identity_data)
    identity_id = create_response.json().get("id")

    # Update the identity
    updated_data = {
        "username": "updateduser",
        "email": "updateduser@example.com",
        "age": 32
    }
    response = client.put(f"/identity/{identity_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"
    assert response.json()["email"] == "updateduser@example.com"

def test_delete_identity():
    """Test deleting an identity by ID."""
    # First, create an identity
    create_response = client.post("/identity", json=valid_identity_data)
    identity_id = create_response.json().get("id")

    # Then, delete the created identity
    response = client.delete(f"/identity/{identity_id}")
    assert response.status_code == 204  # No Content

    # Verify the identity no longer exists
    response = client.get(f"/identity/{identity_id}")
    assert response.status_code == 404  # Not Found

# pytest backend/tests/test_identity.py