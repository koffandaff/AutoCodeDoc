# app.models.vehicle

::: app.models.vehicle

## Database Fields

Detailed breakdown for this model file.

### Entity: Vehicle

A motorized vehicle registered in the system.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `vin` | `str` | The unique Vehicle Identification Number. | *Required* |
| `make` | `str` | The manufacturer (e.g., Toyota, Ford). | *Required* |
| `model` | `str` | The specific car model. | *Required* |
| `year` | `int` | The manufacturing year. | *Required* |

### Entity: VehicleCreate

Payload to register a new vehicle.

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `vin` | `str` | The unique Vehicle Identification Number. | *Required* |
| `make` | `str` | The manufacturer (e.g., Toyota, Ford). | *Required* |
| `model` | `str` | The specific car model. | *Required* |
| `year` | `int` | The manufacturing year. | *Required* |

