from typing import Optional
from app.models.user import User

# Simulated in-memory database
FAKE_DB = {
    1: User(id=1, username="johndoe", email="john@example.com", is_active=True),
    2: User(id=2, username="janedoe", email="jane@example.com", is_active=False),
}

async def fetch_user_by_id(user_id: int) -> Optional[User]:
    """
    Retrieve a user from the simulated database by ID.

    Args:
        user_id (int): The unique identifier.

    Returns:
        Optional[User]: The user instance if found, otherwise None.
    """
    return FAKE_DB.get(user_id)

async def create_user(user_id: int, username: str, email: str, bio: Optional[str] = None) -> User:
    """
    Create a new user and add to the database.
    
    Args:
        user_id (int): The assigned ID.
        username (str): The desired username.
        email (str): The email address.
        bio (Optional[str]): Operational biography for the new user.
    
    Returns:
        User: The newly populated user.
    """
    new_user = User(id=user_id, username=username, email=email, bio=bio)
    FAKE_DB[user_id] = new_user
    return new_user

async def deactivate_user(user_id: int) -> bool:
    """
    Mark a user as inactive in the database.
    
    This feature ensures logical deletion while preserving history.
    
    Args:
        user_id (int): The ID of the user to deactivate.
        
    Returns:
        bool: True if deactivated, False if user not found.
    """
    user = FAKE_DB.get(user_id)
    if user:
        user.is_active = False
        return True
    return False
