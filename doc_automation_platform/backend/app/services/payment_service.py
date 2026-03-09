import uuid

async def create_transaction(amount: float, currency: str) -> dict:
    """
    Create a payment transaction record in the simulated gateway.

    Args:
        amount (float): The payment amount.
        currency (str): The currency used for the transaction.

    Returns:
        dict: The created transaction record including a unique UUID.
    """
    transaction_id = str(uuid.uuid4())
    return {
        "id": transaction_id,
        "amount": amount,
        "currency": currency,
        "status": "pending"
    }
