from fastapi import HTTPException, status

# Base Exception Class
class AppException(Exception):
    """Base application exception for custom error handling."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

# Custom Exceptions
class ResourceNotFoundException(AppException):
    """Exception for when a requested resource is not found."""
    def __init__(self, resource: str):
        message = f"{resource} not found."
        super().__init__(message)

class UnauthorizedAccessException(AppException):
    """Exception for unauthorized access attempts."""
    def __init__(self):
        message = "Unauthorized access. Authentication required."
        super().__init__(message)

class InvalidCredentialsException(AppException):
    """Exception for invalid login credentials."""
    def __init__(self):
        message = "Invalid credentials. Please check your username and password."
        super().__init__(message)

class BadRequestException(AppException):
    """Exception for bad requests, such as validation errors."""
    def __init__(self, detail: str = "Bad request"):
        message = f"Bad request: {detail}"
        super().__init__(message)

class ServerErrorException(AppException):
    """Exception for general server errors."""
    def __init__(self, detail: str = "An error occurred on the server"):
        message = f"Server error: {detail}"
        super().__init__(message)

# Utility function to convert custom exceptions to HTTPExceptions for FastAPI
def raise_http_exception(exc: AppException):
    """Raise an HTTPException based on the custom AppException provided."""
    if isinstance(exc, ResourceNotFoundException):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    elif isinstance(exc, UnauthorizedAccessException):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=exc.message)
    elif isinstance(exc, InvalidCredentialsException):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=exc.message)
    elif isinstance(exc, BadRequestException):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)
    elif isinstance(exc, ServerErrorException):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=exc.message)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unexpected error occurred.")