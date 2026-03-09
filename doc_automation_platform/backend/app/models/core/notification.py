from pydantic import BaseModel, Field
from typing import Optional, Literal

class Notification(BaseModel):
    """Notification model for system alerts and user messages."""
    id: str = Field(description="Unique identifier for the notification.")
    user_id: int = Field(description="The ID of the user receiving the notification.")
    type: Literal["email", "sms", "push"] = Field(description="The delivery channel.")
    message: str = Field(description="The actual notification content.")
    read: bool = Field(default=False, description="Whether the notification has been read.")

class NotificationCreate(BaseModel):
    """Payload to trigger a new notification."""
    user_id: int = Field(description="The ID of the target user.")
    type: Literal["email", "sms", "push"] = Field(description="The desired delivery channel.")
    message: str = Field(description="The message payload.")
