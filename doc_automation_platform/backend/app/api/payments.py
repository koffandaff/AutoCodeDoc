from fastapi import APIRouter, HTTPException
from app.services import payment_service

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/process")
async def process_payment(amount: float, currency: str = "USD") -> dict:
    """
    Process a new payment transaction.

    This endpoint initiates a payment process through our simulated gateway.
    It validates the amount and currency before proceeding.

    Args:
        amount (float): The total amount to be charged. Must be positive.
        currency (str): The ISO currency code (e.g., USD, EUR). Defaults to USD.

    Returns:
        dict: A confirmation message with the transaction_id and status.

    Raises:
        HTTPException:
            - **400**: If the amount is less than or equal to zero.
    """
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    
    transaction = await payment_service.create_transaction(amount, currency)
    return {"status": "success", "transaction_id": transaction["id"], "details": transaction}
