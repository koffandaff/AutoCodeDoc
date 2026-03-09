from pydantic import BaseModel, Field
from typing import Optional

class PaymentRequest(BaseModel):
    """Model used to initiate a payment transaction."""
    amount: float = Field(description="The transaction amount.")
    currency: str = Field(default="USD", description="The currency code (e.g., 'USD').")
    # This field will be used for negative testing (missing description)
    payment_method: str = Field(default="credit_card", description="The chosen payment method (e.g., 'credit_card', 'paypal').")

class PaymentResponse(BaseModel):
    """Response returned after a payment attempt."""
    transaction_id: str = Field(description="Unique gateway transaction ID.")
    status: str = Field(description="Payment status (e.g., 'success', 'failed').")
