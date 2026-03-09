# app.models.ecommerce.inventory.stock

::: app.models.ecommerce.inventory.stock

## Database Fields

Detailed breakdown for this model file.

### Entity: InventoryItem

An item stored in the warehouse.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `sku` | `str` | Stock Keeping Unit. | `<lambda>()` |
| `name` | `str` | Product name. | *Required* |
| `status` | `Literal` | Current stock status. | `available` |
| `location` | `Optional` | Where the item is physically located. | `None` |
| `weight_kg` | `Union` | Weight of the item in kilograms (testing Union). | *Required* |

### Entity: WarehouseLocation

A physical storage location.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `aisle` | `str` | Aisle identifier. | *Required* |
| `shelf` | `str` | Shelf level. | *Required* |
| `bin` | `str` | Specific bin number. | *Required* |

