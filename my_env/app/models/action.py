from pydantic import BaseModel, Field


class Action(BaseModel):
    """Action provided by the policy for the current step."""

    step: int = Field(ge=1)
    hospital_id: str = Field(min_length=1)
    rationale: str | None = None
