# API Routes Listing

Comprehensive list of all endpoints and their documentation, auto-detected from FastAPI routers.

**Total API Modules Detected**: 4


## Auth

**Module**: `app.api.auth`

| Endpoint | Description |
|----------|-------------|
| `⚡ login(username, password)` | Authenticate a user and return an access token. |

::: app.api.auth


## Inventory

**Module**: `app.api.inventory`

| Endpoint | Description |
|----------|-------------|
| `⚡ map_inventory_location(sku, aisle, shelf, bin_num)` | Map an inventory item to a specific physical warehouse location. |

::: app.api.inventory


## Organizations

**Module**: `app.api.organizations`

| Endpoint | Description |
|----------|-------------|
| `⚡ register_organization(name, account_type, emails)` | Register a new Organization. |

::: app.api.organizations


## Users

**Module**: `app.api.users`

| Endpoint | Description |
|----------|-------------|
| `⚡ get_user(user_id)` | Retrieve a user from the database by their unique ID. |
| `⚡ create_user(user_data)` | Create a new user within the system. |
| `⚡ delete_user(user_id)` | Deactivate a user account. |

::: app.api.users

---

