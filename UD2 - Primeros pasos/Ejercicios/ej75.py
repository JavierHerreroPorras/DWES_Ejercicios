# 75. Crea un programa que registre productos con sus precios en un diccionario.
# Permite modificar precios, eliminar productos y consultar precios.

def modificar_precio(d, clave, nuevo_precio):
    d[clave] = nuevo_precio

def eliminar_producto(d, clave):
    d.pop(clave)

def consultar_precios(d, clave):
    return d.get(clave)

def imprimir_elementos(d):
    for key, value in d.items():
        print(f"El elemento {key} vale {value}")

diccionario = {"peras": 5, "manzanas": 4, "papel": 1}
imprimir_elementos(diccionario)
print("")
modificar_precio(diccionario, "peras", 6)
eliminar_producto(diccionario, "manzanas")
print(f"El producto peras tiene un precio de {consultar_precios(diccionario, "peras")}\n")
imprimir_elementos(diccionario)