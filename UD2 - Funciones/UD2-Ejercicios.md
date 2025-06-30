# UD2 - Ejercicios de Funciones en Python

### ⚠️ Aunque no te lo diga explícitamente, todos los ejercicios deben ser resueltos utilizando funciones.

1. **Conversión de Temperaturas**  
   Escribe una función que convierta grados Celsius a Fahrenheit y viceversa. Prueba la función con varios valores.

2. **Validación de Emails**  
   Implementa una función que reciba un string y devuelva `True` si es un email válido (contiene `@` y un punto), y `False` en caso contrario.

3. **Cálculo de Media y Mediana**  
   Crea una función que reciba una lista de números y devuelva la media y la mediana.

4. **Contador de Palabras**  
   Escribe una función que cuente cuántas palabras hay en un texto recibido como parámetro.

5. **Generador de Contraseñas Aleatorias**  
   Implementa una función que genere una contraseña aleatoria de una longitud dada, usando letras, números y símbolos.

6. **Filtrado de Números Pares**  
   Crea una función que reciba una lista de números y devuelva una nueva lista solo con los números pares.

7. **Conversión de Fechas**  
   Escribe una función que reciba una fecha en formato `dd/mm/yyyy` y la devuelva en formato `yyyy-mm-dd`.

8. **Búsqueda de Palabra en Texto**  
   Implementa una función que indique si una palabra dada aparece en un texto (ignorando mayúsculas/minúsculas).

9. **Cálculo de Factorial**  
   Escribe una función recursiva que calcule el factorial de un número.

10. **Formateo de Nombres**  
    Crea una función que reciba un nombre completo y lo devuelva en formato
11. **Buscar 4 ambulancias** 
Diseña una función en Python que, dados cinco puntos en el plano cartesiano, 
determine cuál de los últimos cuatro es el más cercano al primero.**
Cada punto se representará mediante dos variables: una para la coordenada **x** (abscisa)
y otra para la coordenada **y** (ordenada). Para calcular la distancia entre dos puntos,
utilizarás la fórmula euclidiana:
$$
\text{distancia} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$
Imagina que el primer punto representa la ubicación de un accidente, 
y los otros cuatro son las posiciones actuales de cuatro ambulancias. 
Tu función debe identificar cuál es la ambulancia más cercana al lugar del incidente, 
basándose en la distancia mínima.
12. **Buscar Ambulancias**
Refactoriza el ejercicio anterior para que la función reciba una lista de puntos en lugar de cinco variables individuales,
ya que habrá más o menos de cuatro ambulancias.

13. **Ordenar por la suma de cifras**
Dada una lista de números enteros positivos, ordénalos de menor a mayor según la suma de sus cifras utilizando sorted() y una función lambda.
Ejemplo de entrada:
`numeros = [91, 43, 12, 85, 34]`
Salida esperada:
`[12, 21, 34, 91, 85]`  # ordenados por suma de cifras: 3, 6, 7, 10, 13

14. **Filtrar palíndromos**
Dada una lista de palabras, utiliza filter() y una función lambda para quedarte solo con aquellas que son palíndromos (se leen igual al derecho que al revés).
Ejemplo de entrada:
`palabras = ['oso', 'python', 'reconocer', 'casa', 'radar']`
Salida esperada:
`['oso', 'reconocer', 'radar']`

15. **Reducir a la cadena más larga**
Utiliza functools.reduce() y una función lambda para encontrar la cadena más larga de una lista de strings.
Ejemplo de entrada:
`nombres = ['Ana', 'Cristina', 'Luis', 'Beatriz']`
Salida esperada:
`'Cristina'`

16. **Transformar y filtrar con map + filter**
Dada una lista de números enteros, usa map() con lambda para elevarlos al cuadrado, y luego filter() con lambda para quedarte solo con los que sean mayores que 100.
Ejemplo de entrada:
`valores = [4, 10, 11, 5, 13]`
Salida esperada:
`[121, 169]`

17. **Ranking por eficiencia**
Dada una lista de tuplas (nombre_empleado, tiempo_en_segundos), 
crea un ranking usando sorted() y lambda por eficiencia (menos tiempo primero). 
Si empatan, ordena alfabéticamente.
`tiempos = [('Luis', 320), ('Ana', 300), ('Carlos', 300), ('Bea', 400)]`
Salida esperada: 
`[('Ana', 300), ('Carlos', 300), ('Luis', 320), ('Bea', 400)]`

18. **Sistema de votación ponderada por antigüedad**
Enunciado:
Crea una función que reciba un diccionario donde las claves son nombres de empleados y 
los valores son listas de tuplas (años_antigüedad, voto), donde voto es "sí" o "no". 
La función debe calcular el resultado de una votación interna ponderando cada voto 
por los años de antigüedad del empleado.
Devuelve "sí" si el total ponderado de votos a favor supera al de votos en contra.

```python
votos = {
    'Luis': [(5, 'sí'), (2, 'sí')],
    'Ana': [(3, 'no')],
    'Bea': [(10, 'sí')],
    'Carlos': [(7, 'no'), (1, 'no')]
}
# Resultado esperado: "sí"
```
19. **Sistema de gestión de inventario**
Crea una función que reciba un diccionario representando un inventario de productos,
donde las claves son nombres de productos y los valores son tuplas (cantidad, precio_unitario).
La función debe devolver una lista de tuplas ordenada por el valor total del inventario de cada producto (cantidad * precio_unitario) de mayor a menor.
```python
inventario = {
    'manzanas': (50, 0.5),
    'naranjas': (30, 0.8),
    'plátanos': (20, 0.6),
    'uvas': (10, 1.2)
}  
# Resultado esperado: [('manzanas', 25.0), ('naranjas', 24.0), ('plátanos', 12.0), ('uvas', 12.0)]
```
20. **Comparación de vocabularios con conjuntos**
Dadas dos cadenas de texto, escribe una función que devuelva:
Las palabras únicas de cada texto.
Las palabras en común entre ambos textos.
Todas las palabras ordenadas alfabéticamente (sin duplicados).
Usa set() y sorted() para resolverlo.
```python
texto1 = "Python es un lenguaje de programación"    
texto2 = "Java es otro lenguaje de programación popular"
```