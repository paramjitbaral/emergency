from app.utils.randomizer import SeededRandomizer


def generate_medical_case(rng: SeededRandomizer) -> dict:
    variants = [
        {
            "scenario_name": "Heart Attack (Critical)",
            "difficulty": "easy",
            "patient_condition": "critical",
            "required_specialization": "cardiac",
            "critical_time_limit_minutes": 16.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (2.0, 4.0),
                    "specialization": "cardiac",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.85,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (6.0, 9.0),
                    "specialization": "cardiac",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.7,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (4.0, 7.0),
                    "specialization": "general",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.6,
                },
            ],
        },
        {
            "scenario_name": "Heart Attack (Unstable)",
            "difficulty": "medium",
            "patient_condition": "critical",
            "required_specialization": "cardiac",
            "critical_time_limit_minutes": 14.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (2.0, 5.0),
                    "specialization": "general",
                    "traffic_options": ["high", "medium"],
                    "icu_true_probability": 0.65,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (7.0, 11.0),
                    "specialization": "cardiac",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.75,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (5.0, 8.0),
                    "specialization": "cardiac",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.55,
                },
                {
                    "hospital_id": "H4",
                    "distance_range": (4.0, 7.0),
                    "specialization": "general",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.5,
                },
            ],
        },
        {
            "scenario_name": "Mass Cardiac Event (Overload)",
            "difficulty": "hard",
            "patient_condition": "critical",
            "required_specialization": "cardiac",
            "critical_time_limit_minutes": 12.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (3.0, 6.0),
                    "specialization": "general",
                    "traffic_options": ["high", "high", "medium"],
                    "icu_true_probability": 0.45,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (8.0, 12.0),
                    "specialization": "cardiac",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.55,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (6.0, 9.0),
                    "specialization": "cardiac",
                    "traffic_options": ["high", "medium"],
                    "icu_true_probability": 0.4,
                },
                {
                    "hospital_id": "H4",
                    "distance_range": (9.0, 13.0),
                    "specialization": "general",
                    "traffic_options": ["high", "high", "medium"],
                    "icu_true_probability": 0.35,
                },
            ],
        },
    ]
    return rng.choice(variants)
