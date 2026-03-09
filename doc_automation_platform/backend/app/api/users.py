from fastapi import APIRouter, HTTPException
from app.models.user import User, UserCreate
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int) -> User:
    """
    Retrieve a user from the database by their unique ID.

    This endpoint queries the active database for a user matching the provided ID.
    If the user has been deactivated or does not exist, a 404 is returned.

    Args:
        user_id (int): The unique identifier of the user to retrieve.

    Returns:
        User: The user object containing profile details.

    Raises:
        HTTPException: 
            - 404: If the user does not exist.
    """
    user = await user_service.fetch_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=User)
async def create_user(user_data: UserCreate) -> User:
    """
    Create a new user within the system.

    Accepts username and email payload to provision a new active user.

    Args:
        user_data (UserCreate): The incoming JSON payload representing setup parameters.

    Returns:
        User: The created User instance containing the assigned ID.
    """
    # Simple simulated ID assignment
    new_id = len(user_service.FAKE_DB) + 1
    new_user = await user_service.create_user(new_id, user_data.username, user_data.email, user_data.bio)
    return new_user

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """
    Deactivate a user account.
    
    This is a soft-delete operation that updates the 'is_active' flag.
    """
    success = await user_service.deactivate_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deactivated successfully"}
