# app.models.ecommerce.billing.invoice

::: app.models.ecommerce.billing.invoice

## Database Fields

Detailed breakdown for this model file.

### Entity: Invoice

A billing invoice for an organization.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `invoice_id` | `str` | Unique invoice number. | *Required* |
| `organization` | `Organization` | The organization being billed. | *Required* |
| `items` | `List` | List of line items on the invoice. | *Required* |
| `total_amount` | `float` | Total amount due. | *Required* |
| `is_paid` | `bool` | Whether the invoice has been settled. | `False` |

### Entity: InvoiceItem

Line item on an enterprise invoice.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `description` | `str` | Line item description. | *Required* |
| `quantity` | `int` | Quantity of items. | `1` |
| `unit_price` | `float` | Price per unit. | *Required* |

