# app.models.payment

::: app.models.payment

## Database Fields

Detailed breakdown for this model file.

### Entity: PaymentRequest

Model used to initiate a payment transaction.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `amount` | `float` | The transaction amount. | *Required* |
| `currency` | `str` | The currency code (e.g., 'USD'). | `USD` |
| `payment_method` | `str` | The chosen payment method (e.g., 'credit_card', 'paypal'). | `credit_card` |

### Entity: PaymentResponse

Response returned after a payment attempt.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `transaction_id` | `str` | Unique gateway transaction ID. | *Required* |
| `status` | `str` | Payment status (e.g., 'success', 'failed'). | *Required* |

