from app.models.state import LearningEntry

TRAFFIC_FACTOR = {
    "low": 1.0,
    "medium": 0.6,
    "high": 0.3,
}


def compute_speed_kmh(base_speed_kmh: float, traffic: str) -> float:
    return base_speed_kmh * TRAFFIC_FACTOR[traffic]


def compute_travel_time_minutes(distance_km: float, speed_kmh: float) -> float:
    if speed_kmh <= 0:
        return float("inf")
    return (distance_km / speed_kmh) * 60.0


def score_distance(distance_km: float, max_distance_km: float = 20.0) -> float:
    return max(0.0, min(1.0, 1.0 - (distance_km / max_distance_km)))


def score_traffic(traffic: str) -> float:
    return TRAFFIC_FACTOR[traffic]


def score_icu(display_icu: str) -> float:
    return 1.0 if display_icu == "available" else 0.55


def score_memory(entry: LearningEntry | None) -> float:
    if entry is None:
        return 0.5
    total = entry.success + entry.fail
    if total == 0:
        return 0.5
    success_rate = entry.success / total
    fail_bias = max(0.0, (entry.fail - entry.success) / total)
    raw = (0.7 * entry.avg) + (0.3 * success_rate) - (0.4 * fail_bias)
    return max(0.0, min(1.0, raw))


def decision_score(
    icu_score: float,
    distance_score: float,
    traffic_score: float,
    memory_score: float,
) -> float:
    weighted = (
        (icu_score * 0.4)
        + (distance_score * 0.3)
        + (traffic_score * 0.2)
        + (memory_score * 0.3)
    )
    return max(0.0, min(1.0, weighted / 1.2))


def compute_reward(
    survived: bool,
    travel_time: float,
    critical_limit: float,
    specialization_match: bool,
) -> float:
    survival_component = 1.0 if survived else 0.0
    time_efficiency = max(0.0, min(1.0, critical_limit / max(critical_limit + travel_time, 1e-6)))
    specialization_component = 1.0 if specialization_match else 0.0
    delay_penalty = max(0.0, min(1.0, travel_time / max(critical_limit + travel_time, 1e-6)))

    reward = (
        (survival_component * 0.45)
        + (time_efficiency * 0.25)
        + (specialization_component * 0.2)
        - (delay_penalty * 0.1)
    )
    return max(0.0, min(1.0, reward))


def compute_reward_with_breakdown(
    survived: bool,
    travel_time: float,
    critical_limit: float,
    specialization_match: bool,
    survival_score: float | None = None,
    capability_score: float | None = None,
    adaptability_score: float | None = None,
) -> tuple[float, dict[str, float]]:
    survival_component = (
        max(0.0, min(1.0, survival_score))
        if survival_score is not None
        else (1.0 if survived else 0.0)
    )
    time_efficiency = max(0.0, min(1.0, critical_limit / max(critical_limit + travel_time, 1e-6)))
    specialization_component = (
        max(0.0, min(1.0, capability_score))
        if capability_score is not None
        else (1.0 if specialization_match else 0.0)
    )
    delay_penalty = max(0.0, min(1.0, travel_time / max(critical_limit + travel_time, 1e-6)))
    adapt_component = (
        max(0.0, min(1.0, adaptability_score))
        if adaptability_score is not None
        else 0.5
    )

    reward = (
        (survival_component * 0.4)
        + (time_efficiency * 0.2)
        + (specialization_component * 0.2)
        + (adapt_component * 0.2)
        - (delay_penalty * 0.12)
    )
    reward = max(0.0, min(1.0, reward))
    return reward, {
        "survival_component": survival_component,
        "time_efficiency_component": time_efficiency,
        "specialization_component": specialization_component,
        "delay_penalty": delay_penalty,
    }
