from typing import Literal

from pydantic import BaseModel, Field


class HospitalObservation(BaseModel):
    hospital_id: str
    distance_km: float = Field(ge=0)
    icu: Literal["unknown", "available"]
    specialization: Literal["cardiac", "trauma", "general"]
    traffic: Literal["low", "medium", "high"]


class ArrivalOutcomeObservation(BaseModel):
    """What happened when ambulance arrived at hospital"""
    status: Literal["accepted", "partial", "rejected"]
    reason: str
    suitability_score: float = Field(ge=0.0, le=1.0)


class Observation(BaseModel):
    episode_id: int
    seed: int
    task_id: Literal["acde_easy", "acde_medium", "acde_hard"]
    task_objective: str
    scenario_type: Literal["medical", "accident", "fire"]
    scenario_name: str
    scenario_difficulty: Literal["easy", "medium", "hard"]
    patient_condition: str
    required_specialization: Literal["cardiac", "trauma", "general"]
    initial_critical_time_limit_minutes: float = Field(gt=0)
    critical_time_limit_minutes: float = Field(gt=0)
    remaining_time_minutes: float = Field(ge=0)
    step: int = Field(ge=1)
    max_steps: int = 3
    hospitals: list[HospitalObservation]
    previous_action: str | None = None
    ambulance_status: Literal["en_route", "in_transit", "arrived", "admitted", "rerouting"] = "en_route"
    current_location_context: str = "incident_site"
    visited_hospitals: list[str] = Field(default_factory=list)
    failed_hospitals: list[str] = Field(default_factory=list)
    recent_failed_hospitals: list[str] = Field(default_factory=list)
    failed_reasons: dict[str, str] = Field(default_factory=dict)
    total_time_spent_minutes: float = Field(default=0.0, ge=0.0)
    rerouting_reason: str | None = None
    # New fields for arrival outcome visibility
    last_arrival_outcome: ArrivalOutcomeObservation | None = None
    explanation: list[str] = Field(default_factory=list)
    memory_snapshot: dict[str, dict[str, float | int]] = Field(default_factory=dict)
