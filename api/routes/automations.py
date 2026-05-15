from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from schemas.automation import (
    AutomationCreate,
    AutomationUpdate,
    AutomationResponse,
    ErrorResponse,
)
from services.exceptions import InvalidAutomationIdError, AutomationNotFoundError
from services.automation_service import (
    create_automation,
    list_automations,
    get_automation_by_id,
    update_automation,
    delete_automation,
)

AUTOMATION_NOT_FOUND_RESPONSES = {
    400: {"model": ErrorResponse, "description": "Invalid automation ID"},
    404: {"model": ErrorResponse, "description": "Automation not found"},
}

router = APIRouter(prefix="/automations", tags=["Automations"])


@router.post(
    "",
    response_model=AutomationResponse,
    status_code=201,
    summary="Create automation",
    description="Create a new automation and persist it in the database.",
    response_description="Created automation",
)
def create_automation_handler(
    data: AutomationCreate,
    db: Session = Depends(get_db),
) -> AutomationResponse:
    """Create automation."""
    automation = create_automation(db, data)
    return AutomationResponse.model_validate(automation)


@router.get(
    "",
    response_model=list[AutomationResponse],
    summary="List automations",
    description="Return all automations stored in the database.",
    response_description="List of automations",
)
def get_automations_handler(
    db: Session = Depends(get_db),
) -> list[AutomationResponse]:
    """List automations."""
    automations = list_automations(db)
    return [AutomationResponse.model_validate(item) for item in automations]


@router.get(
    "/{automation_id}",
    response_model=AutomationResponse,
    responses=AUTOMATION_NOT_FOUND_RESPONSES,
    summary="Get automation by id",
    description="Retrieve a single automation by its identifier.",
    response_description="Automation details",
)
def get_automation_by_id_handler(
    automation_id: int,
    db: Session = Depends(get_db),
) -> AutomationResponse:
    """Get automation by id."""
    try:
        automation = get_automation_by_id(db, automation_id)
        return AutomationResponse.model_validate(automation)
    except InvalidAutomationIdError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except AutomationNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.patch(
    "/{automation_id}",
    response_model=AutomationResponse,
    responses=AUTOMATION_NOT_FOUND_RESPONSES,
    summary="Update automation",
    description="Partially update an existing automation by its identifier.",
    response_description="Updated automation",
)
def update_automation_handler(
    automation_id: int,
    data: AutomationUpdate,
    db: Session = Depends(get_db),
) -> AutomationResponse:
    """Update automation."""
    try:
        automation = update_automation(db, automation_id, data)
        return AutomationResponse.model_validate(automation)
    except InvalidAutomationIdError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except AutomationNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.delete(
    "/{automation_id}",
    status_code=204,
    responses=AUTOMATION_NOT_FOUND_RESPONSES,
    summary="Delete automation",
    description="Delete an automation by its identifier.",
    response_description="Automation deleted successfully",
)
def delete_automation_handler(
    automation_id: int,
    db: Session = Depends(get_db),
) -> None:
    """Delete automation."""
    try:
        delete_automation(db, automation_id)
        return None
    except InvalidAutomationIdError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except AutomationNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

