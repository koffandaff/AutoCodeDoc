import re
from typing import Optional

def validate_enterprise_email(email: str) -> bool:
    """
    Validates that an email belongs to an approved enterprise domain.
    
    Args:
        email: The email string to check.
        
    Returns:
        bool: True if strictly valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@(enterprise|corporate)\.com$"
    return bool(re.match(pattern, email))

def sanitize_metadata(data: dict) -> dict:
    """
    Sanitize metadata by removing null values and casting all values to strings.

    Ensures consistent, serialization-safe metadata output for
    downstream consumers including logging and analytics pipelines.

    Args:
        data (dict): Raw metadata dictionary, potentially containing None values.

    Returns:
        dict: Cleaned metadata with all values cast to strings.
    """
    return {k: str(v) for k, v in data.items() if v is not None}
