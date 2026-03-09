from typing import Optional, Union, Literal
from pydantic import BaseModel, Field
import uuid

class WarehouseLocation(BaseModel):
    """A physical storage location."""
    aisle: str = Field(description="Aisle identifier.")
    shelf: str = Field(description="Shelf level.")
    bin: str = Field(description="Specific bin number.")

class InventoryItem(BaseModel):
    """An item stored in the warehouse."""
    sku: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Stock Keeping Unit.")
    name: str = Field(description="Product name.")
    status: Literal["available", "reserved", "shipped"] = Field(default="available", description="Current stock status.")
    location: Optional[WarehouseLocation] = Field(default=None, description="Where the item is physically located.")
    weight_kg: Union[float, int] = Field(description="Weight of the item in kilograms (testing Union).")
