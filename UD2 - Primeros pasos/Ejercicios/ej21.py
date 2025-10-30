# 21. Solicita al usuario los nombres de personas que entran a un edificio.
# Finaliza cuando se introduzca "fin".
# Guarda los nombres en una lista.
# Luego, indica cuántos nombres únicos hay, cuántos se repiten y muestra los que se repiten.

nombres = []

# Pedir nombres hasta que se escriba "fin"
while True:
    nombre = input("Introduce el nombre (o 'fin' para terminar): ").lower()
    if nombre == "fin":
        break
    if nombre:  # Evitar cadenas vacías
        nombres.append(nombre)

# Calcular nombres únicos y repetidos
unicos = set(nombres)
repetidos = [n for n in unicos if nombres.count(n) > 1]

# [Juan, Pedro, Pedro, Ana]
repetidos = []
for n in unicos:
    if nombres.count(n) > 1:
        repetidos.append(n)

print("\n--- Resultados ---")
print(f"Total de nombres introducidos: {len(nombres)}")
print(f"Nombres únicos: {len(unicos)}")
print(f"Nombres repetidos: {len(repetidos)}")

if repetidos:
    print("Los nombres repetidos son:")
    for n in repetidos:
        print(f"  - {n} (aparece {nombres.count(n)} veces)")
else:
    print("No hay nombres repetidos.")
