# Здесь мы описали, как будет выглядеть наш респонс, какие поля обязательные и какого типа они будут.

valid_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "uuid": {"type": "number"},
    },
    "required": ["message", "uuid"]
}