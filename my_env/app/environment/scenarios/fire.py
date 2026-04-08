from app.utils.randomizer import SeededRandomizer


def generate_fire_case(rng: SeededRandomizer) -> dict:
    variants = [
        {
            "scenario_name": "Apartment Fire (Smoke Inhalation)",
            "difficulty": "easy",
            "patient_condition": "serious",
            "required_specialization": "general",
            "critical_time_limit_minutes": 18.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (2.0, 5.0),
                    "specialization": "general",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.75,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (7.0, 10.0),
                    "specialization": "trauma",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.6,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (5.0, 7.0),
                    "specialization": "general",
                    "traffic_options": ["medium", "low"],
                    "icu_true_probability": 0.65,
                },
            ],
        },
        {
            "scenario_name": "Factory Fire (Chemical Exposure)",
            "difficulty": "medium",
            "patient_condition": "critical",
            "required_specialization": "general",
            "critical_time_limit_minutes": 15.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (3.0, 6.0),
                    "specialization": "general",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.65,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (8.0, 12.0),
                    "specialization": "trauma",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.7,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (5.0, 9.0),
                    "specialization": "general",
                    "traffic_options": ["high", "medium"],
                    "icu_true_probability": 0.55,
                },
                {
                    "hospital_id": "H4",
                    "distance_range": (4.0, 8.0),
                    "specialization": "trauma",
                    "traffic_options": ["low", "medium"],
                    "icu_true_probability": 0.58,
                },
            ],
        },
        {
            "scenario_name": "Wildfire Front (Evacuation Gridlock)",
            "difficulty": "hard",
            "patient_condition": "critical",
            "required_specialization": "general",
            "critical_time_limit_minutes": 11.0,
            "hospitals": [
                {
                    "hospital_id": "H1",
                    "distance_range": (4.0, 7.0),
                    "specialization": "general",
                    "traffic_options": ["high", "high", "medium"],
                    "icu_true_probability": 0.45,
                },
                {
                    "hospital_id": "H2",
                    "distance_range": (9.0, 13.0),
                    "specialization": "trauma",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.5,
                },
                {
                    "hospital_id": "H3",
                    "distance_range": (6.0, 10.0),
                    "specialization": "general",
                    "traffic_options": ["high", "medium"],
                    "icu_true_probability": 0.4,
                },
                {
                    "hospital_id": "H4",
                    "distance_range": (8.0, 12.0),
                    "specialization": "trauma",
                    "traffic_options": ["medium", "high"],
                    "icu_true_probability": 0.33,
                },
            ],
        },
    ]
    return rng.choice(variants)
