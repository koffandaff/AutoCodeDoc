# app.models.auth

::: app.models.auth

## Database Fields

Detailed breakdown for this model file.

### Entity: Token

Authentication token details.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `access_token` | `str` | The JWT access token. | *Required* |
| `token_type` | `str` | The type of token (e.g., 'Bearer'). | *Required* |
| `expires_in` | `int` | The duration in seconds until the token expires. | `3600` |

