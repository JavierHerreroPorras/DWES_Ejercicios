# 24. Define una lista de alumnos de primaria y otra de secundaria,
# introducidos por el usuario (finalizan con "x").
# Muestra qué nombres están en ambos niveles, cuáles son únicos y el conjunto total sin repeticiones.
nombres_primaria = []
nombres_secundaria = []

# Pedir nombres hasta que se escriba "x"
while True:
    nombre = input("Introduce el nombre (o 'x' para terminar): ").lower()
    if nombre == "x":
        break
    if nombre:  # Evitar cadenas vacías
        nombres_primaria.append(nombre)

# Pedir nombres hasta que se escriba "x"
while True:
    nombre = input("Introduce el nombre (o 'x' para terminar): ").lower()
    if nombre == "x":
        break
    if nombre:  # Evitar cadenas vacías
        nombres_secundaria.append(nombre)

print(nombres_primaria)
print(nombres_secundaria)

print(set(nombres_primaria))
print(set(nombres_secundaria))
print(set(nombres_primaria) | set(nombres_secundaria))


