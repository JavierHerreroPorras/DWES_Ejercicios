orders = [
    {
        "id": 501,
        "customer": {"id": 1, "email": "ana@example.com", "tier": "gold"},
        "created_at": "2025-03-10T09:30:00",
        "status": "paid",
        "items": [
            {"sku": "A1", "qty": 2, "price": 19.90, "discounts": [{"type": "coupon", "value": 5.00}]},
            {"sku": "B2", "qty": 1, "price": 5.50, "discounts": []}
        ],
        "tax": {"rate": 0.21, "region": "ES"},
        "payments": [
            {"method": "card", "amount": 30.00, "auth_code": "X1"},
            {"method": "wallet", "amount": 12.30, "auth_code": "W9"}
        ],
        "shipments": [
            {
                "warehouse": "MAD-1",
                "carrier": "PackGo",
                "packages": [
                    {"tracking": "PG-1001", "items": [{"sku": "A1", "qty": 1}], "status": "delivered"},
                    {"tracking": "PG-1002", "items": [{"sku": "A1", "qty": 1}, {"sku": "B2", "qty": 1}], "status": "in_transit"}
                ]
            }
        ]
    },
    {
        "id": 502,
        "customer": {"id": 2, "email": "borja@example.com", "tier": "standard"},
        "created_at": "2025-03-10T10:10:00",
        "status": "paid",
        "items": [
            {"sku": "C3", "qty": 3, "price": 7.00, "discounts": [{"type": "tier", "value": 2.00}]}
        ],
        "tax": {"rate": 0.10, "region": "PT"},
        "payments": [
            {"method": "card", "amount": 18.70, "auth_code": "X2"}
        ],
        "shipments": [
            {
                "warehouse": "LIS-2",
                "carrier": "IberShip",
                "packages": [
                    {"tracking": "IB-2001", "items": [{"sku": "C3", "qty": 2}], "status": "delivered"}
                ]
            },
            {
                "warehouse": "LIS-2",
                "carrier": "IberShip",
                "packages": [
                    {"tracking": "IB-2002", "items": [{"sku": "C3", "qty": 1}], "status": "label_created"}
                ]
            }
        ]
    },
    {
        "id": 503,
        "customer": {"id": 1, "email": "ana@example.com", "tier": "gold"},
        "created_at": "2025-03-11T08:05:00",
        "status": "pending",
        "items": [
            {"sku": "A1", "qty": 1, "price": 19.90, "discounts": []}
        ],
        "tax": {"rate": 0.21, "region": "ES"},
        "payments": [],
        "shipments": []
    },
    {
        "id": 504,
        "customer": {"id": 3, "email": "carla@example.com", "tier": "premium"},
        "created_at": "2025-03-12T15:45:00",
        "status": "paid",
        "items": [
            {"sku": "D4", "qty": 1, "price": 100.00, "discounts": [{"type": "promo", "value": 10.00}]},
            {"sku": "A1", "qty": 2, "price": 19.90, "discounts": []}
        ],
        "tax": {"rate": 0.21, "region": "ES"},
        "payments": [
            {"method": "card", "amount": 129.18, "auth_code": "X3"}
        ],
        "shipments": [
            {
                "warehouse": "VAL-1",
                "carrier": "FastShip",
                "packages": [
                    {"tracking": "FS-3001", "items": [{"sku": "D4", "qty": 1}, {"sku": "A1", "qty": 1}], "status": "in_transit"}
                ]
            }
        ]
    }
]

def emails_clientes(informacion):
    return list(set([x.get("customer").get("email") for x in informacion]))

def pedidos_pagados(ordenes):
    return list([x for x in ordenes if x.get("status")=="paid"])

def clientes_por_nivel(ordenes):
    d = {"gold": ["ana@example.com"]}
    d = {}
    for orden in ordenes:
        nivel = orden.get("customer").get("tier")
        email = orden.get("customer").get("email")
        if not d.get(nivel):
            d[nivel] = {email}
        else:
            d[nivel].add(email)

    return d

def unidades_enviadas_por_sku(ordenes):
# d = {"A1": 5, "B2", 7, "C3": 1}
    d = {}
    for orden in ordenes:
        for item in orden.get("items"):
            if not d.get(item.get("sku")):
                d[item.get("sku")] = item.get("qty")
            else:
                d[item.get("sku")] = d.get(item.get("sku")) + item.get("qty")

    return d

print(emails_clientes(orders))
print(pedidos_pagados(orders))
print(clientes_por_nivel(orders))
print(unidades_enviadas_por_sku(orders))