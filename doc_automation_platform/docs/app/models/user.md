# app.models.user

::: app.models.user

## Database Fields

Detailed breakdown for this model file.

### Entity: Address

Physical address of a user.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `street` | `str` | Street name and number. | *Required* |
| `city` | `str` | City name. | *Required* |
| `zip_code` | `str` | Postal zip code. | *Required* |

### Entity: Product

Model representing a store product.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `id` | `int` | Unique product ID. | *Required* |
| `name` | `str` | Name of the product. | *Required* |
| `price` | `float` | Price in USD. | *Required* |
| `category` | `str` | Product category (e.g., 'Electronics'). | *Required* |

### Entity: User

User model representing an account in the system.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `id` | `int` | The unique identifier for the user. | *Required* |
| `username` | `str` | The login username. | *Required* |
| `email` | `str` | The email address of the user. | *Required* |
| `role` | `str` | The user's role (e.g., 'admin', 'user'). | `user` |
| `bio` | `Optional` | A short biography of the user. | `None` |
| `is_active` | `bool` | Whether the user account is currently active. | `True` |
| `last_login` | `Optional` | Timestamp of the last successful login. | `None` |
| `tags` | `List` | Categorization tags for the user. | `list()` |
| `address` | `Optional` | User's primary mailing address. | `None` |
| `phone_number` | `Optional` | The user's contact phone number. | `None` |
| `preferred_language` | `str` | The user's preferred language code. | `en` |
| `secret_note` | `Optional` | A private note for administrative use only. | `None` |

### Entity: UserCreate

Model used to create a new User entry.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `username` | `str` | The chosen username. | *Required* |
| `email` | `str` | The associated email address. | *Required* |
| `bio` | `Optional` | A short biography for the profile. | `None` |

