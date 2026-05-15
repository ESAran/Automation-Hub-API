from sqlalchemy.orm import Session

from app.models.automation import Automation
from schemas.automation import AutomationCreate, AutomationUpdate
from services.exceptions import InvalidAutomationIdError, AutomationNotFoundError


def create_automation(db: Session, data: AutomationCreate) -> Automation:
    """Create and persist a new automation."""
    automation = Automation(
        name=data.name,
        description=data.description,
        is_active=data.is_active,
    )
    db.add(automation)
    db.commit()
    db.refresh(automation)
    return automation


def list_automations(db: Session) -> list[Automation]:
    """Return all stored automations."""
    return db.query(Automation).all()


def _find_automation_by_id(db: Session, automation_id: int) -> Automation:
    """Return an automation by id or raise a domain error."""
    if automation_id <= 0:
        raise InvalidAutomationIdError("Automation id must be a positive integer")

    automation = db.query(Automation).filter(Automation.id == automation_id).first()
    if not automation:
        raise AutomationNotFoundError(f"Automation with id {automation_id} not found")

    return automation


def get_automation_by_id(db: Session, automation_id: int) -> Automation:
    """Retrieve an automation by its identifier."""
    return _find_automation_by_id(db, automation_id)


def update_automation(
    db: Session,
    automation_id: int,
    data: AutomationUpdate,
) -> Automation:
    """Update an existing automation and persist the changes."""
    automation = _find_automation_by_id(db, automation_id)
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(automation, field, value)

    db.commit()
    db.refresh(automation)
    return automation


def delete_automation(db: Session, automation_id: int) -> None:
    """Delete an automation by its identifier."""
    automation = _find_automation_by_id(db, automation_id)
    db.delete(automation)
    db.commit()
