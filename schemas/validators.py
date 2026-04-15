def validate_text_field(value: str | None, field_name: str, min_length: int) -> str | None:
    if value is None:
        return None

    normalized = value.strip()

    if not normalized:
        raise ValueError(
            f"The '{field_name}' field cannot be empty or contain only whitespace."
        )

    if len(normalized) < min_length:
        raise ValueError(
            f"The '{field_name}' field must have at least {min_length} characters."
        )

    return normalized