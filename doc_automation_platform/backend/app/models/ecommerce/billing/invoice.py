from typing import List, Optional
from pydantic import BaseModel, Field
from app.models.core.organization import Organization

class InvoiceItem(BaseModel):
    """Line item on an enterprise invoice."""
    description: str = Field(description="Line item description.")
    quantity: int = Field(default=1, description="Quantity of items.")
    unit_price: float = Field(description="Price per unit.")

class Invoice(BaseModel):
    """A billing invoice for an organization."""
    invoice_id: str = Field(description="Unique invoice number.")
    organization: Organization = Field(description="The organization being billed.")
    items: List[InvoiceItem] = Field(description="List of line items on the invoice.")
    total_amount: float = Field(description="Total amount due.")
    is_paid: bool = Field(default=False, description="Whether the invoice has been settled.")
