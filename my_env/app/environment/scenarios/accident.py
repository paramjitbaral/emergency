from app.utils.randomizer import SeededRandomizer


def generate_accident_case(rng: SeededRandomizer) -> dict:
    variants = [
        {
            "scenario_name": "Highway Collision (Severe)",
            "difficulty": "easy",
            "patient_condition": "serious",
            "required_specialization": "trauma",
            "critical_time_limit_minutes": 20.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (3.0, 5.0),
                    "specialization": "trauma",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.8,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (6.0, 9.0),
                    "specialization": "general",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.65,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (10.0, 14.0),
                    "specialization": "trauma",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.7,
                },
            ],
        },
        {
            "scenario_name": "Urban Pile-up (Rush Hour)",
            "difficulty": "medium",
            "patient_condition": "serious",
            "required_specialization": "trauma",
            "critical_time_limit_minutes": 17.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (2.0, 4.0),
                    "specialization": "general",
                    "traffic_options": ["high", "high", "medium"],
                    "icu_true_probability": 0.7,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (7.0, 10.0),
                    "specialization": "trauma",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.7,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (5.0, 8.0),
                    "specialization": "trauma",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.55,
                },
                {
                    "hospital_id": "H4",
                    "distance_range": (4.0, 7.0),
                    "specialization": "general",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.6,
                },
            ],
        },
        {
            "scenario_name": "Bridge Crash (Infrastructure Blocked)",
            "difficulty": "hard",
            "patient_condition": "critical",
            "required_specialization": "trauma",
            "critical_time_limit_minutes": 13.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (3.0, 6.0),
                    "specialization": "general",
                    "traffic_options": ["high", "high", "medium"],
                    "icu_true_probability": 0.5,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (8.0, 12.0),
                    "specialization": "trauma",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.55,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (6.0, 9.0),
                    "specialization": "trauma",
                    "traffic_options": ["high", "medium"],
                    "icu_true_probability": 0.45,
                },
                {
                    "hospital_id": "H4",
                    "distance_range": (4.0, 8.0),
                    "specialization": "general",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.38,
                },
            ],
        },
    ]
    return rng.choice(variants)
