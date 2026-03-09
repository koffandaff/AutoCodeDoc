from fastapi import APIRouter
from typing import List
from app.models.core.organization import Organization, AccountType
from app.services import org_service

router = APIRouter(prefix="/orgs", tags=["Organizations"])

@router.post("/", response_model=Organization)
async def register_organization(name: str, account_type: AccountType, emails: List[str]):
    """
    Register a new Organization.
    
    This endpoint initializes a new tenant space for enterprise customers.

    Args:
        name (str): The legal name of the organization.
        account_type (AccountType): The subscription tier (Basic, Premium, Enterprise).
        emails (List[str]): List of administrative contact email addresses.

    Returns:
        Organization: The newly created organization record.
    """
    return await org_service.create_organization(name, account_type, emails)
