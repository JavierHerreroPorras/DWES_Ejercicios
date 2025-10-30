def emails_activos(users):
    return sorted([x["email"] for x in users if x["is_active"]])

def roles_unicos(users):
    roles = []
    for user in users:
        roles.extend(user["roles"])

    print("Roles presentes en los usuarios (no unicos)", roles)
    return set(roles)

users = [
    {"id": 1, "email": "ana@example.com",   "is_active": True,  "roles": ["admin", "editor"]},
    {"id": 2, "email": "borja@example.com", "is_active": False, "roles": ["viewer"]},
    {"id": 3, "email": "carla@example.com", "is_active": True,  "roles": ["editor", "viewer"]},
    {"id": 4, "email": "david@example.com", "is_active": True,  "roles": ["viewer"]},
    {"id": 5, "email": "eva@example.com",   "is_active": True,  "roles": ["editor", "editor"]}
]


print(emails_activos(users))
print(roles_unicos(users))










weather = [
    {
        "city": "Madrid",
        "coords": {"lat": 40.4168, "lon": -3.7038},
        "alerts": [{"code": "UV", "level": "moderate"}],
        "daily": [
            {
                "date": "2025-03-10",
                "temp": {"min": 6.0, "max": 17.5},
                "humidity": 55,
                "wind_kmh": 18,
                "precip_mm": 0.0,
                "condition": "Clear",
                "hourly": [
                    {"time": "2025-03-10T09:00", "temp": 10.2, "pop": 0.05},
                    {"time": "2025-03-10T12:00", "temp": 16.8, "pop": 0.00},
                    {"time": "2025-03-10T18:00", "temp": 14.1, "pop": 0.10}
                ]
            },
            {
                "date": "2025-03-11",
                "temp": {"min": 7.5, "max": 16.0},
                "humidity": 62,
                "wind_kmh": 22,
                "precip_mm": 1.6,
                "condition": "Rain",
                "hourly": [
                    {"time": "2025-03-11T09:00", "temp": 9.8, "pop": 0.60},
                    {"time": "2025-03-11T12:00", "temp": 14.5, "pop": 0.70},
                    {"time": "2025-03-11T18:00", "temp": 12.2, "pop": 0.40}
                ]
            },
            {
                "date": "2025-03-12",
                "temp": {"min": 8.0, "max": 18.2},
                "humidity": 50,
                "wind_kmh": 19,
                "precip_mm": 0.0,
                "condition": "Partly Cloudy",
                "hourly": [
                    {"time": "2025-03-12T09:00", "temp": 11.2, "pop": 0.10},
                    {"time": "2025-03-12T12:00", "temp": 17.2, "pop": 0.10},
                    {"time": "2025-03-12T18:00", "temp": 15.0, "pop": 0.05}
                ]
            }
        ]
    },
    {
        "city": "Barcelona",
        "coords": {"lat": 41.3874, "lon": 2.1686},
        "alerts": [],
        "daily": [
            {
                "date": "2025-03-10",
                "temp": {"min": 9.0, "max": 18.0},
                "humidity": 60,
                "wind_kmh": 28,
                "precip_mm": 0.0,
                "condition": "Clear",
                "hourly": [
                    {"time": "2025-03-10T09:00", "temp": 12.5, "pop": 0.00},
                    {"time": "2025-03-10T12:00", "temp": 17.1, "pop": 0.05}
                ]
            },
            {
                "date": "2025-03-11",
                "temp": {"min": 10.2, "max": 19.3},
                "humidity": 58,
                "wind_kmh": 35,
                "precip_mm": 10.0,
                "condition": "Windy",
                "hourly": [
                    {"time": "2025-03-11T09:00", "temp": 13.0, "pop": 0.10},
                    {"time": "2025-03-11T12:00", "temp": 18.6, "pop": 0.10}
                ]
            },
            {
                "date": "2025-03-12",
                "temp": {"min": 11.0, "max": 17.0},
                "humidity": 70,
                "wind_kmh": 20,
                "precip_mm": 3.4,
                "condition": "Rain",
                "hourly": [
                    {"time": "2025-03-12T09:00", "temp": 12.0, "pop": 0.65},
                    {"time": "2025-03-12T12:00", "temp": 15.2, "pop": 0.75}
                ]
            }
        ]
    }
]
