# Este código muestra cómo asignar múltiples valores
# a múltiples variables en Python.
def f(x, y):
    return x * 2, y * 2
a, b = f(1, 2)
# En este caso, 'a' será 2 y 'b' será 4.


# Ejemplo de función con parámetros por defecto y asignación de variables
def mi_funcion(param1="default1", param2="2"):
    """
    Esta función toma dos parámetros y devuelve el producto de ambos.
    Si no se proporcionan, usa los valores por defecto.
    :param param1: Primer parámetro, por defecto "default1".
    :param param2: Segundo parámetro, por defecto "default2".
    :return: Producto de los dos parámetros.
    """
    return param1 * param2
mi_funcion("hola",2)
print(mi_funcion)#holahola
mi_funcion(param2=2, param1="hola")