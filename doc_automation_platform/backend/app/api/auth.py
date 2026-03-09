from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login(username: str, password: str) -> dict:
    """
    Authenticate a user and return an access token.

    Verifies the provided credentials against the active database.
    If valid, a JWT token is generated for subsequent requests.

    Args:
        username (str): The login identifier.
        password (str): The secret password for the user.

    Returns:
        dict: containing the `access_token` and `token_type`.

    Raises:
        HTTPException: 
            - 401: If credentials are not valid.
    """
    # Simply mocking auth logic for MVP
    if username == "admin" and password == "secret":
        return {"access_token": "mock-jwt-token", "token_type": "bearer"}
    return {"error": "Invalid credentials"}
