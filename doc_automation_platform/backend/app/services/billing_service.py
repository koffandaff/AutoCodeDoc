from typing import List
from app.models.ecommerce.billing.invoice import Invoice, InvoiceItem
from app.models.core.organization import Organization

async def generate_invoice(org: Organization, items: List[InvoiceItem]) -> Invoice:
    """
    Generates a billing invoice for an organization.
    
    Calculates the total amount based on unit prices and quantities.
    
    Args:
        org: The target organization.
        items: List of billable items.
        
    Returns:
        Invoice: The generated, unpaid invoice.
    """
    total = sum(item.quantity * item.unit_price for item in items)
    return Invoice(
        invoice_id="INV-001",
        organization=org,
        items=items,
        total_amount=total,
        is_paid=False
    )
