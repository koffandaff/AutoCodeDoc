# app.models.core.notification

::: app.models.core.notification

## Database Fields

Detailed breakdown for this model file.

### Entity: Notification

Notification model for system alerts and user messages.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `id` | `str` | Unique identifier for the notification. | *Required* |
| `user_id` | `int` | The ID of the user receiving the notification. | *Required* |
| `type` | `Literal` | The delivery channel. | *Required* |
| `message` | `str` | The actual notification content. | *Required* |
| `read` | `bool` | Whether the notification has been read. | `False` |

### Entity: NotificationCreate

Payload to trigger a new notification.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `user_id` | `int` | The ID of the target user. | *Required* |
| `type` | `Literal` | The desired delivery channel. | *Required* |
| `message` | `str` | The message payload. | *Required* |

