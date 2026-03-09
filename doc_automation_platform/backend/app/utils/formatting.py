def format_currency(amount: float, currency_code: str = "USD") -> str:
    """
    Formats a raw float amount into a localized currency string.
    
    Args:
        amount: The float value.
        currency_code: ISO-4217 standard currency code.
        
    Returns:
        str: Human-readable currency string.
    """
    symbol = "$" if currency_code == "USD" else "€"
    return f"{symbol}{amount:,.2f}"
