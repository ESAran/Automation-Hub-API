from pydantic import BaseModel, Field


class AutomationCreate(BaseModel):
    """Input schema for creating an automation."""

    name: str = Field(..., description="Automation name")
    description: str = Field(..., description="Automation description")
    is_active: bool = Field(..., description="Whether the automation is active")


class AutomationUpdate(BaseModel):
    """Input schema for partially updating an automation."""

    name: str | None = Field(None, description="Automation name")
    description: str | None = Field(None, description="Automation description")
    is_active: bool | None = Field(None, description="Whether the automation is active")


class AutomationResponse(BaseModel):
    """Output schema containing the full automation data."""

    id: int = Field(..., description="Automation unique identifier")
    name: str = Field(..., description="Automation name")
    description: str = Field(..., description="Automation description")
    is_active: bool = Field(..., description="Whether the automation is active")


class ErrorResponse(BaseModel):
    """Standard error response schema."""

    detail: str = Field(..., description="Error message")

