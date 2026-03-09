from fastapi import APIRouter
from app.models.ecommerce.billing.invoice import Invoice
from app.models.core.organization import Organization
from app.services import billing_service

router = APIRouter(prefix="/billing", tags=["Billing"])

@router.post("/invoice", response_model=Invoice)
async def create_invoice(org_id: str):
    """
    Create a new invoice.
    
    Generates the monthly invoice for the specified organization.

    Args:
        org_id (str): The unique identifier of the organization to bill.

    Returns:
        Invoice: The generated, unpaid invoice object.
    """
    # Mocking organization retrieval for documentation purposes
    mock_org = Organization(id=org_id, created_at="now", name="Acme", contact_emails=[])
    return await billing_service.generate_invoice(mock_org, [])
