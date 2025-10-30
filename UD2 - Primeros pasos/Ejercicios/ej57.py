cambios = [
{"fecha": "01-03-2025", "descripcion": "Añado archivo1"},
{"fecha": "01-03-2025", "descripcion": "Modifico archivo1"},
{"fecha": "02-03-2025", "descripcion": "Añado archivo2"},
{"fecha": "04-03-2025", "descripcion": "Modifico archivo2"},
]

cambios_resumen = {
    "01-03-2025": 2,
}

for cambio in cambios:
    fecha = cambio["fecha"]
    if fecha not in cambios_resumen:
        cambios_resumen[fecha] = 0
    cambios_resumen[fecha] += 1

print(cambios_resumen)

print(sorted(cambios, key=lambda x: x["fecha"]))