from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    """
    Simplified User model for ER diagram stress testing.
    
    We have removed the nested Address model and other metadata 
    to see if the ER diagram shrinks and simplifies automatically.
    """
    id: int = Field(description="Unique identifier.")
    username: str = Field(description="Login name.")
    email: str = Field(description="Primary contact email.")

class Product(BaseModel):
    """
    Simplified Product model.
    """
    id: int = Field(description="Product ID.")
    name: str = Field(description="Display name.")
    price: float = Field(description="Price in USD.")
