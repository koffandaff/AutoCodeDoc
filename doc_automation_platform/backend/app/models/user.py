from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class Address(BaseModel):
    """Physical address of a user."""
    street: str = Field(description="Street name and number.")
    city: str = Field(description="City name.")
    zip_code: str = Field(description="Postal zip code.")

class User(BaseModel):
    """User model representing an account in the system."""
    id: int = Field(description="The unique identifier for the user.")
    username: str = Field(description="The login username.")
    email: str = Field(description="The email address of the user.")
    role: str = Field(default="user", description="The user's role (e.g., 'admin', 'user').")
    bio: Optional[str] = Field(default=None, description="A short biography of the user.")
    is_active: bool = Field(default=True, description="Whether the user account is currently active.")
    last_login: Optional[str] = Field(default=None, description="Timestamp of the last successful login.")
    tags: List[str] = Field(default_factory=list, description="Categorization tags for the user.")
    address: Optional[Address] = Field(default=None, description="User's primary mailing address.")
    phone_number: Optional[str] = Field(default=None, description="The user's contact phone number.")
    preferred_language: str = Field(default="en", description="The user's preferred language code.")
    secret_note: Optional[str] = Field(default=None, description="A private note for administrative use only.")

class Product(BaseModel):
    """Model representing a store product."""
    id: int = Field(description="Unique product ID.")
    name: str = Field(description="Name of the product.")
    price: float = Field(description="Price in USD.")
    category: str = Field(description="Product category (e.g., 'Electronics').")

class UserCreate(BaseModel):
    """Model used to create a new User entry."""
    username: str = Field(description="The chosen username.")
    email: str = Field(description="The associated email address.")
    bio: Optional[str] = Field(default=None)
