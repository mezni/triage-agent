BAD_CREATE_TICKET_TOOL = {
    "name": "create_ticket",
    "description": "Create a ticket.",
    "input_schema": {
        "type": "object",
        "properties": {
            "customer": {
                "type": "string",
            },
            "type": {
                "type": "string",
            },
            "level": {
                "type": "string",
            },
            "description": {
                "type": "string",
            },
        },
    },
}