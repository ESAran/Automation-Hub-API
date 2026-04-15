from fastapi import APIRouter, HTTPException
from schemas.automation import AutomationCreate, AutomationUpdate, AutomationResponse, ErrorResponse
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

# CREATE
@router.post("", response_model=AutomationResponse, status_code=201)
def create_automation_handler(data: AutomationCreate) -> AutomationResponse:
    """Create a new automation.

    Args:
        data: The request payload containing the automation data.

    Returns:
        The newly created automation.
    """
    automation = create_automation(data)
    return AutomationResponse(**automation)

# READ
@router.get("", response_model=list[AutomationResponse])
def get_automations_handler() -> list[AutomationResponse]:
    """Retrieve all automations.

    Returns:
        A list of all stored automations.
    """
    return list_automations()

# READ
@router.get("/{automation_id}", response_model=AutomationResponse, responses=AUTOMATION_NOT_FOUND_RESPONSES)
def get_automation_by_id_handler(automation_id: int) -> AutomationResponse:
    """Retrieve an automation by its identifier.

    Args:
        automation_id: The unique identifier of the automation.

    Returns:
        The automation that matches the provided identifier.

    Raises:
        HTTPException: If the identifier is invalid or the automation is not found.
    """
    try:
        automation = get_automation_by_id(automation_id)
        return AutomationResponse(**automation)
    except InvalidAutomationIdError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except AutomationNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

# UPDATE
@router.put("/{automation_id}", response_model=AutomationResponse, responses=AUTOMATION_NOT_FOUND_RESPONSES)
def update_automation_handler(automation_id: int, data: AutomationUpdate) -> AutomationResponse:
    """Update an existing automation.

    Args:
        automation_id: The unique identifier of the automation to update.
        data: The request payload containing the fields to update.

    Returns:
        The updated automation.

    Raises:
        HTTPException: If the identifier is invalid or the automation is not found.
    """
    try:
        automation = update_automation(automation_id, data)
        return AutomationResponse(**automation)
    except InvalidAutomationIdError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except AutomationNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

# DELETE
@router.delete("/{automation_id}", status_code=204, responses=AUTOMATION_NOT_FOUND_RESPONSES)
def delete_automation_handler(automation_id: int) -> None:
    """Delete an automation by its identifier.

    Args:
        automation_id: The unique identifier of the automation to delete.

    Returns:
        None. The endpoint responds with HTTP 204 and no response body.

    Raises:
        HTTPException: If the identifier is invalid or the automation is not found.
    """
    try:
        delete_automation(automation_id)
        return None
    except InvalidAutomationIdError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except AutomationNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

