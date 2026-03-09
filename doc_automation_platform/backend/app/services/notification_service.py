class NotificationService:
    """Service handling notification delivery logic."""

    async def send_notification(self, user_id: int, notif_type: str, message: str) -> bool:
        """
        Dispatch a notification to a specific user.

        Args:
            user_id: The recipient's user ID.
            notif_type: The channel (email, sms, push).
            message: The content to deliver.

        Returns:
            bool: True if dispatched successfully, False otherwise.
            
        Raises:
            ValueError: If an unsupported notification type is provided.
        """
        # Mock logic
        print(f"[{notif_type.upper()}] Sending to User {user_id}: {message}")
        return True

notification_service = NotificationService()
