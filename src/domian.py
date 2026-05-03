from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
import identifiers

def utc_field_now(): # TODO: Could be moved to seprate file like fields.py
    return Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)

class User(BaseModel):
    id: identifiers.UserId
    name: str
    created_date: datetime = utc_field_now()


