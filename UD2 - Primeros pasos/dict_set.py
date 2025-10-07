# Ejemplo básico de uso de SETS y DICCIONARIOS en Python

# --- SETS ---
print("=== CONJUNTOS (set) ===")

colores = {"rojo", "verde", "azul"}          # Crear un set
print("Set inicial:", colores)

colores.add("amarillo")                      # Añadir elemento
print("Tras añadir 'amarillo':", colores)

colores.discard("verde")                     # Eliminar sin error
print("Tras eliminar 'verde':", colores)

print("¿Está 'rojo' en el conjunto?", "rojo" in colores)  # Comprobar pertenencia
print("Tamaño del conjunto:", len(colores))

# Unión e intersección con otro conjunto
otros = {"negro", "azul", "blanco"}
print("Unión:", colores | otros)
print("Intersección:", colores & otros)


# --- DICCIONARIOS ---
print("\n=== DICCIONARIOS (dict) ===")

precios = {"pan": 1.5, "leche": 0.9, "huevos": 2.5}
print("Diccionario inicial:", precios)

precios["queso"] = 3.2                        # Añadir elemento
print("Tras añadir 'queso':", precios)

precios["leche"] = 1.0                        # Modificar valor
print("Precio de 'leche' actualizado:", precios["leche"])

precios.pop("pan")                            # Eliminar clave
print("Tras eliminar 'pan':", precios)

print("Claves:", list(precios.keys()))
print("Valores:", list(precios.values()))
print("Pares clave-valor:", list(precios.items()))

# Recorrido del diccionario
for producto, precio in precios.items():
    print(f"El producto {producto} cuesta {precio}€")

# Obtener valor de forma segura
print("Precio de 'mantequilla':", precios.get("mantequilla", "No disponible"))
