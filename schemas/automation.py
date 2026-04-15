from pydantic import BaseModel, Field, field_validator, model_validator
from core.constants import (
    MIN_DESCRIPTION_LENGTH,
    MAX_DESCRIPTION_LENGTH,
    MIN_NAME_LENGTH,
    MAX_NAME_LENGTH,
)
from schemas.validators import validate_text_field


class AutomationCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=MIN_NAME_LENGTH,
        max_length=MAX_NAME_LENGTH,
        description="Automation name",
    )
    description: str = Field(
        ...,
        min_length=MIN_DESCRIPTION_LENGTH,
        max_length=MAX_DESCRIPTION_LENGTH,
        description="Automation description",
    )
    is_active: bool = Field(..., description="Whether the automation is active")

    @field_validator("name", "description", mode="before")
    @classmethod
    def validate_required_text_fields(cls, value: str, info):
        min_length = (
            MIN_NAME_LENGTH if info.field_name == "name" else MIN_DESCRIPTION_LENGTH
        )
        return validate_text_field(
            value=value,
            field_name=info.field_name,
            min_length=min_length,
        )


class AutomationUpdate(BaseModel):
    name: str | None = Field(
        None,
        min_length=MIN_NAME_LENGTH,
        max_length=MAX_NAME_LENGTH,
    )
    description: str | None = Field(
        None,
        min_length=MIN_DESCRIPTION_LENGTH,
        max_length=MAX_DESCRIPTION_LENGTH,
    )
    is_active: bool | None = Field(None)

    @field_validator("name", "description", mode="before")
    @classmethod
    def validate_optional_text_fields(cls, value: str | None, info):
        min_length = (
            MIN_NAME_LENGTH if info.field_name == "name" else MIN_DESCRIPTION_LENGTH
        )
        return validate_text_field(
            value=value,
            field_name=info.field_name,
            min_length=min_length,
        )

    @model_validator(mode="before")
    @classmethod
    def reject_null_for_non_nullable_fields(cls, values: dict):
        non_nullable_on_update = {"name", "description", "is_active"}
        null_fields = [
            key for key, value in values.items()
            if key in non_nullable_on_update and value is None
        ]
        if null_fields:
            fields_label = "field" if len(null_fields) == 1 else "fields"
            raise ValueError(
                f"The following {fields_label} do not accept null values on update: "
                f"{', '.join(null_fields)}"
            )
        return values


class AutomationResponse(BaseModel):
    id: int = Field(..., description="Automation unique identifier")
    name: str = Field(..., description="Automation name")
    description: str = Field(..., description="Automation description")
    is_active: bool = Field(..., description="Whether the automation is active")


class ErrorResponse(BaseModel):
    detail: str = Field(..., description="Error message")

