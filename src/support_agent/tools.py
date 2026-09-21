def get_customer_status(customer_id: str) -> str:
    customers = {
        "C001": "active",
        "C002": "active",
        "C003": "suspended",
    }

    return customers.get(customer_id, "unknown")


CUSTOMER_STATUS_TOOL = {
    "name": "get_customer_status",
    "description": (
        "Get the current account status of a customer. "
        "Use this when you need to verify whether a customer "
        "account is active, suspended, or unknown."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "customer_id": {
                "type": "string",
                "description": "The unique customer identifier.",
            }
        },
        "required": ["customer_id"],
    },
}


TOOL_SCHEMAS = [
    CUSTOMER_STATUS_TOOL,
]


TOOL_REGISTRY = {
    "get_customer_status": get_customer_status,
}