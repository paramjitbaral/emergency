"""OpenEnv client-facing typed models for ACDE."""

from pydantic import Field

from openenv.core.env_server.types import Action, Observation


class ACDEAction(Action):
    """Action sent by the agent for each routing step."""

    step: int = Field(..., ge=1)
    hospital_id: str = Field(..., min_length=1)
    rationale: str | None = None


class ACDEObservation(Observation):
    """Observation returned by the ACDE server."""

    task_id: str = Field(default="")
    scenario_name: str = Field(default="")
    scenario_difficulty: str = Field(default="")
    patient_condition: str = Field(default="")
    required_specialization: str = Field(default="")
    step: int = Field(default=1, ge=1)
    metadata: dict = Field(default_factory=dict)