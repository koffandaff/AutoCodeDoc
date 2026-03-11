# Features Connection

How the platform's core features connect through the service layer. Each service encapsulates business logic for a specific domain.

**Total Services Detected**: 4


---


## Org Service

**Module**: `app.services.org_service`

| Function | Description |
|----------|-------------|
| `🔄 create_organization(name, account_type, contact_emails)` | Creates a new enterprise organization in the system. |

::: app.services.org_service


---


## Payment Service

**Module**: `app.services.payment_service`

| Function | Description |
|----------|-------------|
| `🔄 create_transaction(amount, currency)` | Create a payment transaction record in the simulated gateway. |

::: app.services.payment_service


---


## User Service

**Module**: `app.services.user_service`

| Function | Description |
|----------|-------------|
| `🔄 fetch_user_by_id(user_id)` | Retrieve a user from the simulated database by ID. |
| `🔄 create_user(user_id, username, email, bio)` | Create a new user and add to the database. |
| `🔄 deactivate_user(user_id)` | Mark a user as inactive in the database. |

::: app.services.user_service


---


## Vehicle Service

**Module**: `app.services.vehicle_service`

| Function | Description |
|----------|-------------|
| `🔄 register_vehicle(vin, make, model, year)` | Registers a new vehicle in the system database. |

::: app.services.vehicle_service


---
