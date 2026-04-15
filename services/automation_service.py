from services.exceptions import InvalidAutomationIdError, AutomationNotFoundError
from schemas.automation import AutomationCreate, AutomationUpdate

automations: list[dict] = []
next_id = 1

def create_automation(data: AutomationCreate) -> dict:
    """Create a new automation and store it in memory.

    Args:
        data: The input data used to create the automation.

    Returns:
        A dictionary containing the newly created automation.
    """

    global next_id
    automation = {
        "id": next_id,
        "name": data.name,
        "description": data.description,
        "is_active": data.is_active
    }

    automations.append(automation)
    next_id += 1
    
    return automation.copy()

def list_automations() -> list[dict]:
    """Return the list of all stored automations.

    Returns:
        A list containing all automation dictionaries currently in memory.
    """
    return [automation.copy() for automation in automations]

def get_automation_by_id(automation_id: int) -> dict:
    """Retrieve an automation by its identifier.

    Args:
        automation_id: The unique identifier of the automation.

    Returns:
        The automation dictionary that matches the given identifier.

    Raises:
        InvalidAutomationIdError: If the automation id is invalid.
        AutomationNotFoundError: If no automation with the given identifier is found.
    """
    if automation_id <= 0:
        raise InvalidAutomationIdError("Automation id must be a positive integer")

    for automation in automations:
        if automation["id"] == automation_id:
            return automation.copy()

    raise AutomationNotFoundError(f"Automation with id {automation_id} not found")

def update_automation(automation_id: int, data: AutomationUpdate) -> dict:
    """Update the fields of an existing automation.

    Args:
        automation_id: The unique identifier of the automation to update.
        data: The partial data used to update the automation.

    Returns:
        The updated automation dictionary.

    Raises:
        InvalidAutomationIdError: If the automation id is invalid.
        AutomationNotFoundError: If the automation does not exist.
    """
    automation = get_automation_by_id(automation_id)
    update_data = data.dict(exclude_unset=True)

    if "name" in update_data:
        automation["name"] = update_data["name"]
    if "description" in update_data:
        automation["description"] = update_data["description"]
    if "is_active" in update_data:
        automation["is_active"] = update_data["is_active"]

    return automation.copy()

def delete_automation(automation_id: int) -> None:
    """Delete an automation from in-memory storage.

    Args:
        automation_id: The unique identifier of the automation to delete.

    Raises:
        InvalidAutomationIdError: If the automation id is invalid.
        AutomationNotFoundError: If the automation does not exist.
    """
    automation = get_automation_by_id(automation_id)
    automations.remove(automation)
