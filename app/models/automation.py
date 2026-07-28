from sqlalchemy import Boolean, Column, Integer, String

from app.db.base import Base
from core.constants import MAX_DESCRIPTION_LENGTH, MAX_NAME_LENGTH

class Automation(Base):
    __tablename__ = "automations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(MAX_NAME_LENGTH), nullable=False)
    description = Column(String(MAX_DESCRIPTION_LENGTH), nullable=False)
    is_active = Column(Boolean, nullable=False)