# app.models.core.organization

::: app.models.core.organization

## Database Fields

Detailed breakdown for this model file.

### Entity: BaseEntity

Base class for all enterprise entities.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `id` | `str` | Unique identifier. | *Required* |
| `created_at` | `str` | Creation ISO timestamp. | *Required* |
| `metadata` | `Optional` | Extensible metadata dictionary. | `None` |

### Entity: Organization

An enterprise organization.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `id` | `str` | Unique identifier. | *Required* |
| `created_at` | `str` | Creation ISO timestamp. | *Required* |
| `metadata` | `Optional` | Extensible metadata dictionary. | `None` |
| `name` | `str` | Name of the organization. | *Required* |
| `account_type` | `AccountType` | The subscription tier. | `AccountType.BASIC` |
| `parent_org_id` | `Optional` | Parent organization ID if applicable (forward reference test). | `None` |
| `contact_emails` | `List` | List of administrative contact emails. | *Required* |

