# Ejercicios - Fundamentos de Python - 100 ejercicios resueltos
# =========================
# Ejercicios para practicar los fundamentos de Python, incluyendo variables, tipos de datos, estructuras de control y más.
# Ejercicios
# 1. **Hola Mundo**
#     Crea un programa que imprima "¡Hola, Mundo!" en la consola.
print("¡Hola, Mundo!")
# 2. **Variables y Tipos de Datos**
#     Crea variables de diferentes tipos de datos (entero, flotante, cadena, booleano) y muestra su tipo.
entero = 42
flotante = 3.14
cadena = "Python"
booleano = True
print(type(entero))    # <class 'int'>
print(type(flotante))  # <class 'float'>
print(type(cadena))    # <class 'str'>
print(type(booleano))  # <class 'bool'>
# 3. **Operaciones Aritméticas**
#     Crea un programa que realice las siguientes operaciones aritméticas y muestre los resultados:
#     - Suma de dos números
def suma(a, b):
    return a + b
print(suma(5, 3))  # Resultado: 8
#     - Resta de dos números
def resta(a, b):
    return a - b
print(resta(5, 3))  # Resultado: 2
#     - Multiplicación de dos números
def multiplicacion(a, b):
    return a * b
print(multiplicacion(5, 3))  # Resultado: 15
#     - División de dos números
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
print(division(5, 3))  # Resultado: 1.6666666666666667
# 4. **Condicionales**
#     Crea un programa que verifique si un número es par o impar.
def es_par(numero):
    return numero % 2 == 0
print(es_par(4))  # Resultado: True
print(es_par(5))  # Resultado: False
# 5. **Bucles**
#     Crea un programa que imprima los números del 1 al 10 utilizando un bucle `for`.
for i in range(1, 11):
    print(i)
# 6. **Listas**
#     Crea una lista de números y realiza las siguientes operaciones:
numeros = [1, 2, 3, 4, 5]
#     - Añadir un número al final de la lista
def añadir_numero(lista, numero):
    lista.append(numero)
    return lista
print(añadir_numero(numeros, 6))  # Resultado: [1, 2, 3, 4, 5, 6]
#     - Eliminar un número de la lista
def eliminar_numero(lista, numero):
    if numero in lista:
        lista.remove(numero)
    return lista
print(eliminar_numero(numeros, 3))  # Resultado: [1, 2, 4, 5, 6]
#     - Ordenar la lista
def ordenar_lista(lista):
    return sorted(lista)
print(ordenar_lista(numeros))  # Resultado: [1, 2, 4, 5, 6]
# 7. **Diccionarios**
#     Crea un diccionario con información de una persona (nombre, edad, ciudad) y muestra sus valores.
def crear_diccionario(nombre, edad, ciudad):
    return {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}
persona = crear_diccionario("Juan", 30, "Madrid")
print(persona)  # Resultado: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
# 8. **Funciones**
#     Crea una función que reciba dos números y retorne su máximo común divisor (MCD).
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(mcd(48, 18))  # Resultado: 6
# 9. **Excepciones**
#     Crea un programa que solicite un número al usuario y maneje la excepción si el usuario ingresa un valor no numérico.
def solicitar_numero():
    try:
        numero = int(input("Introduce un número: "))
        return numero
    except ValueError:
        return "Error: Debes introducir un número válido."
print(solicitar_numero())  # Si se introduce un número, lo mostrará; si no, mostrará el error.
# 10. **Sumar Elementos de una Lista**
#     Dada una lista de números, utiliza la función `sum()` para calcular la suma de todos sus elementos.
def sumar_lista(lista):
    return sum(lista)
numeros = [1, 2, 3, 4, 5]
print(sumar_lista(numeros))  # Resultado: 15
# 11. **Ordenar una Lista de Tuplas**
def ordenar_tuplas(tuplas):
    return sorted(tuplas, key=lambda x: x[1])  # Ordena por el segundo elemento de cada tupla
tuplas = [(1, 3), (2, 1), (3, 2)]
print(ordenar_tuplas(tuplas))  # Resultado: [(2, 1), (3, 2), (1, 3)]
# 12. **Contar Vocales en una Cadena**
def contar_vocales(cadena):
    return sum(1 for char in cadena.lower() if char in 'aeiou')
cadena = "Hola Mundo"
print(contar_vocales(cadena))  # Resultado: 4 (o, a, u, o)
# 13. **Invertir una Cadena**
def invertir_cadena(cadena):
    return cadena[::-1]
cadena = "Python"
print(invertir_cadena(cadena))  # Resultado: "nohtyP"
# 14. **Encontrar el Elemento Más Grande en una Lista**
def encontrar_mayor(lista):
    return max(lista)
lista_numeros = [1, 5, 3, 9, 2]
print(encontrar_mayor(lista_numeros))  # Resultado: 9
# 15. **Calcular el Factorial de un Número**
def factorial(n):
    if n < 0:
        return "Error: El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
print(factorial(5))  # Resultado: 120
# 16. **Comprobar si una Cadena es un Palíndromo**
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]
cadena = "Anita lava la tina"
print(es_palindromo(cadena))  # Resultado: True
# 17. **Generar una Lista de Números Pares**
def generar_pares(n):
    return [i for i in range(2, n + 1, 2)]
print(generar_pares(10))  # Resultado: [2, 4, 6, 8, 10]
# 18. **Contar Palabras en una Cadena**
def contar_palabras(cadena):
    return len(cadena.split())
cadena = "Hola mundo, ¿cómo estás?"
print(contar_palabras(cadena))  # Resultado: 5
# 19. **Encontrar el Índice de un Elemento en una Lista**
`def encontrar_indice(lista, elemento):
    try:
        return lista.index(elemento)
    except ValueError:
        return "Error: El elemento no está en la lista."
lista = [1, 2, 3, 4, 5]
print(encontrar_indice(lista, 3))  # Resultado: 2`

# 19. **Calcular la Media de una Lista de Números**
def calcular_media(lista):
    if not lista:
        return "Error: La lista está vacía."
    return sum(lista) / len(lista)
lista_numeros = [10, 20, 30, 40, 50]
print(calcular_media(lista_numeros))  # Resultado: 30.0
# 20. **Convertir una Lista de Cadenas a Mayúsculas**
def convertir_mayusculas(lista):
    return [cadena.upper() for cadena in lista]
lista_cadenas = ["hola", "mundo", "python"]
print(convertir_mayusculas(lista_cadenas))  # Resultado: ['HOLA', 'MUNDO', 'PYTHON']
# 21. **Eliminar Duplicados de una Lista**
def eliminar_duplicados(lista):
    return list(set(lista))
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
print(eliminar_duplicados(lista_con_duplicados))  # Resultado: [1, 2, 3, 4, 5]
# 22. **Encontrar el Elemento Común en Dos Listas**
def encontrar_comun(lista1, lista2):
    return list(set(lista1) & set(lista2))
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
print(encontrar_comun(lista1, lista2))  # Resultado: [3, 4]
# 23. **Crear una Lista de Números del 1 al 100**
def crear_lista_numeros():
    return list(range(1, 101))
print(crear_lista_numeros())  # Resultado: [1, 2, ..., 100]
# 24. **Contar la Frecuencia de Elementos en una Lista**
def contar_frecuencia(lista):
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia
lista_frecuencia = [1, 2, 2, 3, 3, 3]
print(contar_frecuencia(lista_frecuencia))  # Resultado: {1: 1, 2: 2, 3: 3}
# 25. **Crear una Lista de Números Aleatorios**
import random
def crear_lista_aleatoria(tamaño, rango):
    return [random.randint(1, rango) for _ in range(tamaño)]
print(crear_lista_aleatoria(10, 100))  # Resultado: Lista de 10 números aleatorios entre 1 y 100
# 26. **Encontrar el Mínimo y Máximo en una Lista**
def encontrar_min_max(lista):
    if not lista:
        return "Error: La lista está vacía."
    return min(lista), max(lista)
lista_min_max = [10, 20, 30, 40, 50]
print(encontrar_min_max(lista_min_max))  # Resultado: (10, 50)
# 27. **Crear una Lista de Números Fibonacci**
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]
print(fibonacci(10))  # Resultado: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# 28. **Convertir una Lista de Números a Cadenas**
def convertir_a_cadenas(lista):
    return [str(numero) for numero in lista]
lista_numeros = [1, 2, 3, 4, 5]
print(convertir_a_cadenas(lista_numeros))  # Resultado: ['1', '2', '3', '4', '5']
# 29. **Calcular el Producto de una Lista de Números**
def calcular_producto(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto
lista_productos = [1, 2, 3, 4, 5]
print(calcular_producto(lista_productos))  # Resultado: 120
# 30. **Crear una Lista de Números Primos**
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def crear_lista_primos(n):
    return [i for i in range(2, n + 1) if es_primo(i)]
print(crear_lista_primos(30))  # Resultado: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# 31. **Contar la Cantidad de Votos a Favor y en Contra**
def contar_votos(votos):
    a_favor = sum(1 for voto in votos if voto == 'sí')
    en_contra = sum(1 for voto in votos if voto == 'no')
    return a_favor, en_contra
votos = ['sí', 'no', 'sí', 'sí', 'no']
print(contar_votos(votos))  # Resultado: (3, 2)
# 32. **Crear una Lista de Palabras con Longitud Mayor a N**
def palabras_mayores_a(lista, n):
    return [palabra for palabra in lista if len(palabra) > n]
palabras = ['python', 'programación', 'hola', 'mundo', 'desarrollo']
print(palabras_mayores_a(palabras, 5))  # Resultado: ['programación', 'desarrollo']
# 33. **Encontrar el Elemento Más Pequeño en una Lista**
def encontrar_menor(lista):
    if not lista:
        return "Error: La lista está vacía."
    return min(lista)
lista_menor = [10, 20, 30, 40, 50]
print(encontrar_menor(lista_menor))  # Resultado: 10
# 34. **Crear una Lista de Números al Cuadrado**
def cuadrados(lista):
    return [numero ** 2 for numero in lista]
lista_numeros = [1, 2, 3, 4, 5]
print(cuadrados(lista_numeros))  # Resultado: [1, 4, 9, 16, 25]
# 35. **Contar la Cantidad de Elementos en una Lista**
def contar_elementos(lista):
    return len(lista)
lista_elementos = [1, 2, 3, 4, 5]
print(contar_elementos(lista_elementos))  # Resultado: 5
# 36. **Crear una Lista de Números Divisibles por 3**
def divisibles_por_tres(n):
    return [i for i in range(1, n + 1) if i % 3 == 0]
print(divisibles_por_tres(30))  # Resultado: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# 37. **Crear una Lista de Números Aleatorios Únicos**
def crear_aleatorios_unicos(tamaño, rango):
    return random.sample(range(1, rango + 1), tamaño)
print(crear_aleatorios_unicos(10, 100))  # Resultado: Lista de 10 números aleatorios únicos entre 1 y 100
# 38. **Contar la Cantidad de Vocales en una Cadena**
def contar_vocales_cadena(cadena):
    return sum(1 for char in cadena.lower() if char in 'aeiou')
cadena = "Hola Mundo"
print(contar_vocales_cadena(cadena))  # Resultado: 4 (o, a, u, o)
# 39. **Crear una Lista de Números Impares**
def crear_impares(n):
    return [i for i in range(1, n + 1) if i % 2 != 0]
print(crear_impares(10))  # Resultado: [1, 3, 5, 7, 9]
# 40. **Convertir una Lista de Cadenas a Minúsculas**
def convertir_a_minusculas(lista):
    return [cadena.lower() for cadena in lista]
lista_cadenas = ["HOLA", "MUNDO", "PYTHON"]
print(convertir_a_minusculas(lista_cadenas))  # Resultado: ['hola', 'mundo', 'python']
# 41. **Crear una Lista de Números del 1 al N**
def crear_lista_hasta_n(n):
    return list(range(1, n + 1))
print(crear_lista_hasta_n(10))  # Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 42. **Contar la Cantidad de Consonantes en una Cadena**
def contar_consonantes(cadena):
    return sum(1 for char in cadena.lower() if char.isalpha() and char not in 'aeiou')
cadena = "Hola Mundo"
print(contar_consonantes(cadena))  # Resultado: 6 (H, l, M, n, d)
# 43. **Crear una Lista de Números Pares del 1 al N**
def crear_pares_hasta_n(n):
    return [i for i in range(2, n + 1, 2)]
print(crear_pares_hasta_n(10))  # Resultado: [2, 4, 6, 8, 10]
# 44. **Crear una Lista de Números del 1 al N al Cuadrado**
def cuadrados_hasta_n(n):
    return [i ** 2 for i in range(1, n + 1)]
print(cuadrados_hasta_n(10))  # Resultado: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 45. **Contar la Cantidad de Palabras en una Cadena**
def contar_palabras_cadena(cadena):
    return len(cadena.split())
cadena = "Hola mundo, ¿cómo estás?"
print(contar_palabras_cadena(cadena))  # Resultado: 5
# 46. **Crear una Lista de Números del 1 al N al Cubo**
def cubos_hasta_n(n):
    return [i ** 3 for i in range(1, n + 1)]
print(cubos_hasta_n(10))  # Resultado: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# 47. **Crear una Lista de Números del 1 al N Divisibles por 5**
def divisibles_por_cinco(n):
    return [i for i in range(1, n + 1) if i % 5 == 0]
print(divisibles_por_cinco(50))  # Resultado: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# 48. **Crear una Lista de Números del 1 al N Divisibles por 3 y 5**
def divisibles_por_tres_y_cinco(n):
    return [i for i in range(1, n + 1) if i % 3 == 0 and i % 5 == 0]
print(divisibles_por_tres_y_cinco(100))  # Resultado: [15, 30, 45, 60, 75, 90]
# 49. **Crear una Lista de Números del 1 al N que no son Primos**
def no_primos_hasta_n(n):
    return [i for i in range(1, n + 1) if not es_primo(i)]
print(no_primos_hasta_n(30))  # Resultado: [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
# 50. **Crear una Lista de Números del 1 al N que son Primos**
def primos_hasta_n(n):
    return [i for i in range(2, n + 1) if es_primo(i)]
print(primos_hasta_n(30))  # Resultado: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# 51. **Crear una Lista de Números del 1 al N que son Múltiplos de 4**
def multiples_de_cuatro(n):
    return [i for i in range(1, n + 1) if i % 4 == 0]
print(multiples_de_cuatro(40))  # Resultado: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
# 52. **Crear una Lista de Números del 1 al N que son Múltiplos de 6**
def multiples_de_seis(n):
    return [i for i in range(1, n + 1) if i % 6 == 0]
print(multiples_de_seis(60))  # Resultado: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
# 53. **Crear una Lista de Números del 1 al N que son Múltiplos de 7**
def multiples_de_siete(n):
    return [i for i in range(1, n + 1) if i % 7 == 0]
print(multiples_de_siete(70))  # Resultado: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# 54. **Crear una Lista de Números del 1 al N que son Múltiplos de 8**
def multiples_de_ocho(n):
    return [i for i in range(1, n + 1) if i % 8 == 0]
print(multiples_de_ocho(80))  # Resultado: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
# 55. **Crear una Lista de Números del 1 al N que son Múltiplos de 9**
def multiples_de_nueve(n):
    return [i for i in range(1, n + 1) if i % 9 == 0]
print(multiples_de_nueve(90))  # Resultado: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
# 56. **Crear una Lista de Números del 1 al N que son Múltiplos de 10**
def multiples_de_diez(n):
    return [i for i in range(1, n + 1) if i % 10 == 0]
print(multiples_de_diez(100))  # Resultado: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# 57. **Crear una Lista de Números del 1 al N que son Múltiplos de 11**
def multiples_de_once(n):
    return [i for i in range(1, n + 1) if i % 11 == 0]
print(multiples_de_once(110))  # Resultado: [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
# 58. **Crear un Diccionario de Números del 1 al N con sus Cuadrados**
def diccionario_cuadrados(n):
    return {i: i ** 2 for i in range(1, n + 1)}
print(diccionario_cuadrados(10))  # Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# 59. **Crear un Diccionario de Números del 1 al N con sus Cubos**
def diccionario_cubos(n):
    return {i: i ** 3 for i in range(1, n + 1)}
print(diccionario_cubos(10))  # Resultado: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
# 60. **Crear un Diccionario de Números del 1 al N con sus Raíces Cuadradas**
def diccionario_raices(n):
    return {i: round(i ** 0.5, 2) for i in range(1, n + 1)}
print(diccionario_raices(10))  # Resultado: {1: 1.0, 2: 1.41, 3: 1.73, 4: 2.0, 5: 2.24, 6: 2.45, 7: 2.65, 8: 2.83, 9: 3.0, 10: 3.16}
# 61. **Crear una tupla de números del 1 al N**
def crear_tupla_hasta_n(n):
    return tuple(range(1, n + 1))
print(crear_tupla_hasta_n(10))  # Resultado: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 62. **Crear un Conjunto de Números del 1 al N**
def crear_conjunto_hasta_n(n):
    return set(range(1, n + 1))
print(crear_conjunto_hasta_n(10))  # Resultado: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 63. **Usar `enumerate()` para Iterar sobre una Lista**
def enumerar_lista(lista):
    for indice, valor in enumerate(lista):
        print(f"Índice: {indice}, Valor: {valor}")
lista = ['a', 'b', 'c', 'd']
enumerar_lista(lista)
# 64. **Usar `zip()` para Combinar Dos Listas**
def combinar_listas(lista1, lista2):
    return list(zip(lista1, lista2))
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
print(combinar_listas(lista1, lista2))  # Resultado: [(1, 'a'), (2, 'b'), (3, 'c')]
# 65. **Usar `map()` para Aplicar una Función a Cada Elemento de una Lista**
def aplicar_funcion(lista, funcion):
    return list(map(funcion, lista))
def cuadrado(x):
    return x ** 2
lista_numeros = [1, 2, 3, 4, 5]
print(aplicar_funcion(lista_numeros, cuadrado))  # Resultado: [1, 4, 9, 16, 25]
# 66. **Usar `filter()` para Filtrar Elementos de una Lista**
def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))
lista_numeros = [1, 2, 3, 4, 5, 6]
print(filtrar_pares(lista_numeros))  # Resultado: [2, 4, 6]
# 67. **Usar `reduce()` para Reducir una Lista a un Solo Valor**
from functools import reduce
def reducir_suma(lista):
    return reduce(lambda x, y: x + y, lista)
lista_numeros = [1, 2, 3, 4, 5] 
print(reducir_suma(lista_numeros))  # Resultado: 15
# 68. **Usar `sorted()` para Ordenar una Lista**
def ordenar_lista(lista):
    return sorted(lista)
lista_numeros = [5, 2, 9, 1, 5, 6]
print(ordenar_lista(lista_numeros))  # Resultado: [1, 2, 5, 5, 6, 9]
# 69. **Usar `any()` para Comprobar si Algún Elemento Cumple una Condición**
def tiene_elemento_par(lista):
    return any(x % 2 == 0 for x in lista)
lista_numeros = [1, 3, 5, 7, 8]
print(tiene_elemento_par(lista_numeros))  # Resultado: True
# 70. **Usar `all()` para Comprobar si Todos los Elementos Cumplen una Condición**
def todos_son_pares(lista):
    return all(x % 2 == 0 for x in lista)
lista_numeros = [2, 4, 6, 8]
print(todos_son_pares(lista_numeros))  # Resultado: True
# 71. **Usar `max()` para Encontrar el Elemento Máximo en una Lista**
def encontrar_maximo(lista):
    return max(lista)
lista_numeros = [1, 2, 3, 4, 5]
print(encontrar_maximo(lista_numeros))  # Resultado: 5
# 72. **Usar switch para Imprimir un Mensaje según el Día de la Semana**
def dia_de_la_semana(dia):
    switcher = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return switcher.get(dia, "Día no válido")
print(dia_de_la_semana(1))  # Resultado: "Lunes"
print(dia_de_la_semana(8))  # Resultado: "Día no válido"
# 73. **Usar `set()` para Eliminar Duplicados de una Lista**
def eliminar_duplicados_conjunto(lista):
    return list(set(lista))
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
print(eliminar_duplicados_conjunto(lista_con_duplicados))  # Resultado: [1, 2, 3, 4, 5]
# 74. **Usar `reversed()` para Invertir una Lista**
def invertir_lista(lista):
    return list(reversed(lista))
lista_numeros = [1, 2, 3, 4, 5]
print(invertir_lista(lista_numeros))  # Resultado: [5, 4, 3, 2, 1]
# 75. **Usar `join()` para Unir Elementos de una Lista en una Cadena**
def unir_lista(lista, separador):
    return separador.join(lista)
lista_cadenas = ['Hola', 'mundo', 'Python']
print(unir_lista(lista_cadenas, ' '))  # Resultado: "Hola mundo Python"
# 76. **Usar `split()` para Dividir una Cadena en una Lista**
def dividir_cadena(cadena, separador):
    return cadena.split(separador)
cadena = "Hola mundo Python"
print(dividir_cadena(cadena, ' '))  # Resultado: ['Hola', 'mundo', 'Python']
# 77. **Usar `strip()` para Eliminar Espacios en Blanco de una Cadena**
def eliminar_espacios(cadena):
    return cadena.strip()
cadena = "   Hola mundo Python   "
print(eliminar_espacios(cadena))  # Resultado: "Hola mundo Python"
# 78. **Usar `replace()` para Reemplazar Subcadenas en una Cadena**
def reemplazar_subcadena(cadena, viejo, nuevo):
    return cadena.replace(viejo, nuevo)
cadena = "Hola mundo Python"
print(reemplazar_subcadena(cadena, "Python", "Java"))  # Resultado: "Hola mundo Java"
# 79. **Usar `find()` para Encontrar la Posición de una Subcadena en una Cadena**
def encontrar_subcadena(cadena, subcadena):
    return cadena.find(subcadena)
cadena = "Hola mundo Python"
print(encontrar_subcadena(cadena, "mundo"))  # Resultado: 5
# 80. **Usar `count()` para Contar la Cantidad de Ocurrencias de una Subcadena en una Cadena**
def contar_ocurrencias(cadena, subcadena):
    return cadena.count(subcadena)
cadena = "Hola mundo Python, Python es genial"
print(contar_ocurrencias(cadena, "Python"))  # Resultado: 2
# 81. **Usar `startswith()` para Comprobar si una Cadena Comienza con una Subcadena**
def comienza_con(cadena, subcadena):
    return cadena.startswith(subcadena)
cadena = "Hola mundo Python"
print(comienza_con(cadena, "Hola"))  # Resultado: True
# 82. **Usar `endswith()` para Comprobar si una Cadena Termina con una Subcadena**
def termina_con(cadena, subcadena):
    return cadena.endswith(subcadena)
cadena = "Hola mundo Python"
print(termina_con(cadena, "Python"))  # Resultado: True
# 83. **Usar `capitalize()` para Capitalizar la Primera Letra de una Cadena**
def capitalizar_cadena(cadena):
    return cadena.capitalize()
cadena = "hola mundo python"
print(capitalizar_cadena(cadena))  # Resultado: "Hola mundo python"
# 84. **Usar `title()` para Capitalizar la Primera Letra de Cada Palabra en una Cadena**
def capitalizar_titulo(cadena):
    return cadena.title()
cadena = "hola mundo python"
print(capitalizar_titulo(cadena))  # Resultado: "Hola Mundo Python"
# 85. **Usar `upper()` para Convertir una Cadena a Mayúsculas**
def convertir_mayusculas(cadena):
    return cadena.upper()
cadena = "hola mundo python"
print(convertir_mayusculas(cadena))  # Resultado: "HOLA MUNDO PYTHON"
# 86. **Usar `lower()` para Convertir una Cadena a Minúsculas**
def convertir_minusculas(cadena):
    return cadena.lower()
cadena = "HOLA MUNDO PYTHON"
print(convertir_minusculas(cadena))  # Resultado: "hola mundo python"
# 87. **Usar `isalpha()` para Comprobar si una Cadena Contiene Solo Letras**    
def contiene_solo_letras(cadena):
    return cadena.isalpha()
cadena = "HolaMundo"
print(contiene_solo_letras(cadena))  # Resultado: True
# 88. **Usar `isdigit()` para Comprobar si una Cadena Contiene Solo Dígitos**
def contiene_solo_digitos(cadena):
    return cadena.isdigit()
cadena = "123456"
print(contiene_solo_digitos(cadena))  # Resultado: True
# 89. **Usar `isalnum()` para Comprobar si una Cadena Contiene Solo Letras y Dígitos**
def contiene_solo_letras_y_digitos(cadena):
    return cadena.isalnum()
cadena = "Hola123"
print(contiene_solo_letras_y_digitos(cadena))  # Resultado: True
# 90. **Usar `isupper()` para Comprobar si una Cadena Está en Mayúsculas**
def esta_en_mayusculas(cadena):
    return cadena.isupper()
cadena = "HOLA MUNDO"
print(esta_en_mayusculas(cadena))  # Resultado: True
# 91. **Usar `islower()` para Comprobar si una Cadena Está en Minúsculas**
def esta_en_minusculas(cadena):
    return cadena.islower()
cadena = "hola mundo"
print(esta_en_minusculas(cadena))  # Resultado: True
# 92. **Usar `isspace()` para Comprobar si una Cadena Contiene Solo Espacios en Blanco**
def contiene_solo_espacios(cadena):
    return cadena.isspace()
cadena = "   "
print(contiene_solo_espacios(cadena))  # Resultado: True
# 93. **Usar `swapcase()` para Intercambiar Mayúsculas y Minúsculas en una Cadena**
def intercambiar_mayusculas_minusculas(cadena):
    return cadena.swapcase()
cadena = "Hola Mundo"
print(intercambiar_mayusculas_minusculas(cadena))  # Resultado: "hOLA mUNDO"
# 94. **Usar `lstrip()` para Eliminar Espacios en Blanco al Inicio de una Cadena**
def eliminar_espacios_inicio(cadena):
    return cadena.lstrip()
cadena = "   Hola mundo Python"
print(eliminar_espacios_inicio(cadena))  # Resultado: "Hola mundo Python   "
# 95. **Usar `rstrip()` para Eliminar Espacios en Blanco al Final de una Cadena**
def eliminar_espacios_final(cadena):
    return cadena.rstrip()
cadena = "Hola mundo Python   "
print(eliminar_espacios_final(cadena))  # Resultado: "Hola mundo Python"
# 96. **Usar `partition()` para Dividir una Cadena en Tres Partes**
def dividir_cadena_particion(cadena, separador):
    return cadena.partition(separador)
cadena = "Hola mundo Python"
print(dividir_cadena_particion(cadena, "mundo"))  # Resultado: ('Hola ', 'mundo', ' Python')
# 97. **Usar `splitlines()` para Dividir una Cadena en Líneas**
def dividir_cadena_lineas(cadena):
    return cadena.splitlines()
cadena = "Hola mundo\nPython es genial"
print(dividir_cadena_lineas(cadena))  # Resultado: ['Hola mundo', 'Python es genial']
# 98. **Usar `format()` para Formatear una Cadena**
def formatear_cadena(nombre, edad):
    return "Mi nombre es {} y tengo {} años.".format(nombre, edad)
nombre = "Juan" 
edad = 30
print(formatear_cadena(nombre, edad))  # Resultado: "Mi nombre es Juan y tengo 30 años."
# 99. **Usar `f-strings` para Formatear una Cadena (Python 3.6+)**
def formatear_cadena_fstrings(nombre, edad):
    return f"Mi nombre es {nombre} y tengo {edad} años."
nombre = "Ana"
edad = 25
print(formatear_cadena_fstrings(nombre, edad))  # Resultado: "Mi nombre es Ana y tengo 25 años."
# 100. **Usar `str()` para Convertir un Objeto a Cadena**
def convertir_a_cadena(objeto):
    return str(objeto)
objeto = 12345
print(convertir_a_cadena(objeto))  # Resultado: "12345"

