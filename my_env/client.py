"""OpenEnv client for the Adaptive Crisis Decision Environment."""

from typing import Dict

from openenv.core import EnvClient
from openenv.core.client_types import StepResult
from openenv.core.env_server.types import State

from .models import ACDEAction, ACDEObservation


class ACDEEnv(EnvClient[ACDEAction, ACDEObservation]):
    """HTTP client adapter for ACDE using the OpenEnv client protocol."""

    def _step_payload(self, action: ACDEAction) -> Dict:
        return {
            "step": action.step,
            "hospital_id": action.hospital_id,
            "rationale": action.rationale,
        }

    def _parse_result(self, payload: Dict) -> StepResult[ACDEObservation]:
        obs_data = payload.get("observation", {}) or {}
        observation = ACDEObservation(
            task_id=obs_data.get("task_id", ""),
            scenario_name=obs_data.get("scenario_name", ""),
            scenario_difficulty=obs_data.get("scenario_difficulty", ""),
            patient_condition=obs_data.get("patient_condition", ""),
            required_specialization=obs_data.get("required_specialization", ""),
            step=obs_data.get("step", 1),
            metadata=obs_data,
        )

        return StepResult(
            observation=observation,
            reward=payload.get("reward", 0.0),
            done=payload.get("done", False),
        )

    def _parse_state(self, payload: Dict) -> State:
        return State(
            episode_id=payload.get("episode_id"),
            step_count=payload.get("step", 0),
        )