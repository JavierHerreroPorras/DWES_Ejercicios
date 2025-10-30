# 34. Simula una agenda de contactos.
# El usuario puede introducir pares nombre-teléfono hasta escribir "fin".
# Guarda los datos en un diccionario.
# Al final, permite buscar el número de una persona por su nombre.

# Pedir nombres hasta que se escriba "fin"
d = {}
nombre = ""
telefono = ""

while True:
    nombre = input("Introduce el nombre (o 'fin' para terminar): ").lower()
    if nombre == "fin":
        break
    telefono = input("Introduce el telefono: ").lower()

    d[nombre] = telefono

nombre_buscar = input("Introduce el nombre de la persona a buscar: ").lower()

if nombre_buscar in d:
    print(f"El telefono es {d.get(nombre_buscar)}.")
else:
    print("El telefono no existe.")