from typing import List, Optional, Union, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field

class AccountType(str, Enum):
    """Types of enterprise accounts."""
    BASIC = "basic"
    PREMIUM = "premium"
    ENTERPRISE = "enterprise"

class BaseEntity(BaseModel):
    """Base class for all enterprise entities."""
    id: str = Field(description="Unique identifier.")
    created_at: str = Field(description="Creation ISO timestamp.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Extensible metadata dictionary.")

class Organization(BaseEntity):
    """An enterprise organization."""
    name: str = Field(description="Name of the organization.")
    account_type: AccountType = Field(default=AccountType.BASIC, description="The subscription tier.")
    parent_org_id: Optional[str] = Field(default=None, description="Parent organization ID if applicable (forward reference test).")
    
    # Complex type test
    contact_emails: List[str] = Field(description="List of administrative contact emails.")
