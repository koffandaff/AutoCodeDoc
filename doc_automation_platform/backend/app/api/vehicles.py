from fastapi import APIRouter
from app.models.vehicle import VehicleCreate, Vehicle
from app.services import vehicle_service

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.post("/", response_model=dict)
async def create_vehicle(vehicle: VehicleCreate) -> dict:
    """
    Register a new vehicle into the platform.

    This endpoint takes vehicle details and processes them through the
    vehicle service layer for permanent registration.

    Args:
        vehicle (VehicleCreate): The vehicle registration payload containing VIN, make, model, and year.

    Returns:
        dict: A confirmation message with registration status and vehicle details.
    """
    result = await vehicle_service.register_vehicle(
        vin=vehicle.vin,
        make=vehicle.make,
        model=vehicle.model,
        year=vehicle.year
    )
    return result
