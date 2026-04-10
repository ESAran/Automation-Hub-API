class AutomationError(Exception):
    """Base exception for automation domain errors."""


class InvalidAutomationIdError(AutomationError):
    """Raised when the automation id is invalid."""


class AutomationNotFoundError(AutomationError):
    """Raised when the automation is not found."""