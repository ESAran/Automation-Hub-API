from schemas.automation import AutomationCreate, AutomationUpdate


automations: list[dict] = []
next_id = 1

def create_automation(data: AutomationCreate) -> dict:

    global next_id
    automation = {
        "id": next_id,
        "name": data.name,
        "description": data.description,
        "is_active": data.is_active
    }

    automations.append(automation)
    next_id += 1
    
    return automation

def list_automations() -> list[dict]:
    return automations

def get_automation_by(automation_id: int) -> dict:
    for automation in automations:
        if automation["id"] == automation_id:
            return automation
    raise ValueError(f"Automation with id {automation_id} not found")

def update_automation(automation_id: int, data: AutomationUpdate) -> dict:
    automation = get_automation_by(automation_id)
    update_data = data.dict(exclude_unset=True)

    if "name" in update_data:
        automation["name"] = update_data["name"]
    if "description" in update_data:
        automation["description"] = update_data["description"]
    if "is_active" in update_data:
        automation["is_active"] = update_data["is_active"]

    return automation

def delete_automation(automation_id: int) -> None:
    automation = get_automation_by(automation_id)
    automations.remove(automation)
