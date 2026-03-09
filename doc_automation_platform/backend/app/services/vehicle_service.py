from typing import Dict, Any

async def register_vehicle(vin: str, make: str, model: str, year: int) -> Dict[str, Any]:
    """
    Registers a new vehicle in the system database.

    Args:
        vin: Vehicle Identification Number.
        make: The manufacturer.
        model: The car model.
        year: The manufacturing year.

    Returns:
        dict: The registered vehicle data with a success status.
    """
    return {
        "status": "success",
        "vehicle": {
            "vin": vin,
            "make": make,
            "model": model,
            "year": year
        }
    }
