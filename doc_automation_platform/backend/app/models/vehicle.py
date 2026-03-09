from pydantic import BaseModel, Field

class Vehicle(BaseModel):
    """A motorized vehicle registered in the system."""
    vin: str = Field(description="The unique Vehicle Identification Number.")
    make: str = Field(description="The manufacturer (e.g., Toyota, Ford).")
    model: str = Field(description="The specific car model.")
    year: int = Field(description="The manufacturing year.")

class VehicleCreate(BaseModel):
    """Payload to register a new vehicle."""
    vin: str = Field(description="The unique Vehicle Identification Number.")
    make: str = Field(description="The manufacturer (e.g., Toyota, Ford).")
    model: str = Field(description="The specific car model.")
    year: int = Field(description="The manufacturing year.")
