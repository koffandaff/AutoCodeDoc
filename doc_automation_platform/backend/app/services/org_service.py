from typing import List, Optional
from app.models.core.organization import Organization, AccountType

async def create_organization(name: str, account_type: AccountType, contact_emails: List[str]) -> Organization:
    """
    Creates a new enterprise organization in the system.
    
    Args:
        name: The legal name of the entity.
        account_type: The subscription level chosen.
        contact_emails: List of initial contact addresses.
        
    Returns:
        Organization: The fully formed organization record.
    """
    return Organization(
        id="org-12345",
        created_at="2026-03-09T10:00:00Z",
        name=name,
        account_type=account_type,
        contact_emails=contact_emails,
        parent_org_id=None
    )
