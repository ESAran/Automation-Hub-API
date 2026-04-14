from pydantic import BaseModel, Field, model_validator


class AutomationCreate(BaseModel):
    """Input schema for creating an automation."""

    name: str = Field(..., description="Automation name")
    description: str = Field(..., description="Automation description")
    is_active: bool = Field(..., description="Whether the automation is active")


class AutomationUpdate(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)
    is_active: bool | None = Field(None)
    # notes: str | None = Field(None)  # exemplo: esse pode ser null

    @model_validator(mode="before")
    @classmethod
    def reject_null_for_non_nullable_fields(cls, values: dict):
        non_nullable_on_update = {"name", "description", "is_active"}
        null_fields = [
            key for key, value in values.items()
            if key in non_nullable_on_update and value is None
        ]
        if null_fields:
            raise ValueError(f"Fields cannot be null: {', '.join(null_fields)}")
        return values


class AutomationResponse(BaseModel):
    """Output schema containing the full automation data."""

    id: int = Field(..., description="Automation unique identifier")
    name: str = Field(..., description="Automation name")
    description: str = Field(..., description="Automation description")
    is_active: bool = Field(..., description="Whether the automation is active")


class ErrorResponse(BaseModel):
    """Standard error response schema."""

    detail: str = Field(..., description="Error message")

