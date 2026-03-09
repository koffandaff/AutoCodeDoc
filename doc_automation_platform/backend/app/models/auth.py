from pydantic import BaseModel, Field

class Token(BaseModel):
    """Authentication token details."""
    access_token: str = Field(description="The JWT access token.")
    token_type: str = Field(description="The type of token (e.g., 'Bearer').")
    # Missing description for testing
    expires_in: int = Field(default=3600, description="The duration in seconds until the token expires.")
