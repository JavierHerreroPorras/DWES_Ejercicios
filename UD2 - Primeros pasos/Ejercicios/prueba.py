from functools import reduce

# MAP --> 4. Calcular la longitud de cada palabra de una lista siempre que la longitud sea mayor que 4.
'''lista = ["hola", "manolo", "una", "cosa", "tengo", "que", "decirte"]

def get_length(n):
    return len(n)

print(lista)
l2 = list(map(get_length, lista))
print(l2)

# FILTER --> 4. Filtra una lista de edades para quedarte con los mayores de edad.
lista = [18, 44, 16, 12, 55]

def is_adult(n):
    return n >= 18

print()
print(lista)
l2 = list(filter(is_adult, lista))
print(l2)'''

# REDUCE --> 7
numero = 8
lista = list(range(1, numero+1))
print(lista)

def factorial(a, b):
    return a*b

print(reduce(factorial, lista, 1))
print(reduce(lambda x, y: x*y, lista, 1))

# reduce --> 8
numero = 5321

def suma(a, b):
    return int(a) + int(b)

print(reduce(suma, str(numero)))
print(reduce(lambda x,y: int(x) + int(y), str(numero)))

# zip --> 2
nombres = ["Manuela", "Daniela", "Carla"]
edades = [22, 34, 55, 66]

print(list(zip(nombres, edades)))

# zip --> 3
nombres = ["Papel", "Fregona", "Tomate"]
precios = [15.45, 12.33, 7.66, 4.88]
d = {}

for nombre, precio in zip(nombres, precios):
    d[nombre] = precio

print(d)

# any y all --> 3
palabras = ["Casa", "Zapato", "Perro", "Gato"]

resultados = []
for palabra in palabras:
    resultados.append("z" in palabra.lower())

resultado_final = any(resultados)

print("\nAlguna palabra contiene z? ", palabras)
print(resultado_final)

# any y all --> 6
cadenas = ["hola", "Python", "Mundo"]

resultados = []
for cadena in cadenas:
    resultados.append(cadena[0].isupper())

resultado_final = all(resultados)

print("\n", cadenas)
print("Empiezan en mayúscula?:", resultado_final)

# enumerate --> 4
lista = ["Hola", "Python", "Mundo"]
d = {}

for index, value in enumerate(lista):
    d[index] = value

print("\nNuevo diccionario a partir de la lista: ", lista)
print(d)



lista = [18, 44, 16, 12, 55]

def is_adult(n):
    return n >= 18

print()
print(lista)

print([l+10 for l in lista])

# Lambda --> 10
lista = [18, 44, 16, 12, 55]
print("\n", lista)
print(list(map(lambda x: x*2, filter(lambda x: x%2==0, lista))))
[n*2 for n in lista if n%2==0]

# Compresion --> 4
frase = "¿Cuántas personas están trabajando en este momento?"
print([p for p in frase.split() if len(p)>5])

# Compresion --> 8
print([len(p) for p in frase.split()])







