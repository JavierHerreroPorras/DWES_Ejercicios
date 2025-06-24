#Strings o cadenas de caracteres
triple=""" esto es una linea
 y esta es otra linea"""
print(triple)  # Imprime el texto con saltos de línea
# Concatenación de cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2
print(cadena_concatenada)  # Imprime 'Hola Mundo'
# Repetición de cadenas
cadena_repetida = cadena1 * 3
print(cadena_repetida)  # Imprime 'HolaHolaHola'
# Longitud de una cadena
longitud_cadena = len(cadena1)


# Python ofrece la posibilidad de usar f-string. Estas son cadenas de
# caracteres con el prefijo f o F. Estas cadenas pueden incluir pares de llaves
# con expresiones cuyo valor puede ser sustituido en tiempo de ejecución.
# Dentro de los pares de llaves también podemos especificar detalles del
# tipo de dato que se espera y la anchura del campo entre otros.
nombre: str = 'Juan'
telefono: int = 678900123
altura: float = 182.3
print(f'{nombre*2:10s} ==> {telefono:10d} => {altura:.2f}')
# En este caso, el nombre se repetirá dos veces, el teléfono se mostrará como un
# número entero de 10 dígitos y la altura se mostrará con dos decimales.
# También podemos usar el método format() para formatear cadenas de manera similar.
print('{} {} {}'.format(nombre, telefono, altura))
# Python también permite el uso de cadenas multilínea utilizando comillas triples.
# Estas cadenas pueden abarcar varias líneas y conservar los saltos de línea.
# Ejemplo de cadena multilínea
cadena_multilinea = """Esta es una cadena
multilínea
que conserva los saltos de línea
y los espacios."""
print(cadena_multilinea)
# Otra alternativa para formatear cadenas es el operador %. Este operador
# compone una cadena de texto donde aparecen %, posiblemente seguidos
# por especificadores de tipo como antes, con una tupla de parámetros. El
# resultado es la sustitución de cada % junto con la especificación de tipo
# por el valor del parámetro correspondiente.
print('fruit:%10s, price:%8.2f' % ('apple', 6.056))