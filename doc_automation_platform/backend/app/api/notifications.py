from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from app.models.core.notification import Notification, NotificationCreate
from app.services.notification_service import notification_service

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/", response_model=Dict[str, Any])
async def trigger_notification(payload: NotificationCreate):
    """
    Trigger a new system notification.

    This endpoint accepts a notification payload and dispatches it through the appropriate channel
    (email, SMS, or push) to the specified user.

    Args:
        payload: The NotificationCreate model containing target user and message data.

    Returns:
        Dict: A confirmation object indicating success or failure.

    Raises:
        HTTPException:
            400: If the notification service rejects the payload.
    """
    success = await notification_service.send_notification(
        user_id=payload.user_id,
        notif_type=payload.type,
        message=payload.message
    )
    
    if not success:
        raise HTTPException(status_code=400, detail="Failed to dispatch notification")
        
    return {"status": "success", "message": "Notification queued for delivery"}
