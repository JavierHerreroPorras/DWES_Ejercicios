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
21. **Gestionar ingresos y gastos**
Realizar un programa que gestione los ingresos y gastos mensuales en un año. 
Crea una función para leer del teclado los ingresos y gastos de cada mes del año. 
Crea otra función que a partir de los ingresos y gastos de un año, calcule el balance de cada mes.
Las funciones no deben escribir nada por pantalla.
El programa debe leer los datos con la primera función, 
realizar los cálculos con la segunda 
y finalmente mostrar los resultados.

22. **Gestionar ingresos y gastos por ubicación** 
Ampliar la funcionalidad del programa del problema 21 permitiendo gestionar los ingresos y gastos 
anuales por ciudad y código postal. 
Modificar la función de lectura de datos convenientemente, así como la función de cálculo de balances
Además, realizar una tercera función que recibe los balances por ciudad, código postal y mes y 
devuelve los balances con valor mínimo y máximo, 
así como a qué ciudades, códigos postales y meses corresponden. 
Modifica el programa para que lea los datos, realice los cálculos y presente todos los resultados descritos. 

23. **Jugar al Monopoly** 
Escribir un programa descompuesto convenientemente en base a funciones que, para una suma de dinero 
dada, indique cómo descomponerla en billetes y monedas corrientes. Se debe utilizar el mínimo posible de billetes y 
monedas. No existen limitaciones respecto al número de billetes y monedas disponibles.

24. **Dar la campanada**
Crear un programa que lea del teclado dos valores que indican hora de comienzo y hora de fin (ej: 16:30 
y 19:17), y presente por pantalla la cantidad de veces que un reloj emite campanadas (las campanas se producen en los 
minutos: 0, 15, 30 y 45). Se supone que la hora de comienzo es menor que la hora de final y ambas pertenecen al mismo 
día. 
Por ejemplo, si la hora de comienzo es 9:44 y la hora de fin es 10:01, hay que informar de 2 campanadas. 
Si la hora de comienzo es 8:00 y la hora de fin es 10:07, el programa debe indicar que sonaron 8 campanadas.

25. **Tiempo entre dos fechas**  
    Escribe una función que reciba dos fechas en formato `dd/mm/yyyy` y calcule cuántos días han pasado entre ambas. Valida que la segunda fecha sea posterior a la primera.

26. **Gestión de notas con condiciones**  
    Implementa una función que reciba una lista de calificaciones (entre 0 y 10) y devuelva un resumen con: cuántos suspensos, cuántos aprobados, la media y la nota más repetida.

27. **Descomposición de importe en billetes y monedas**  
    Crea una función que reciba una cantidad de dinero en euros (por ejemplo, 186.73) y devuelva cuántos billetes y monedas de cada tipo serían necesarios para representar esa cantidad usando el menor número de unidades.

28. **Estadísticas de temperaturas por semana**  
    Diseña una función que reciba un diccionario con semanas como claves (por ejemplo, `"Semana 1"`, `"Semana 2"`, etc.) y listas de temperaturas diarias como valores. La función debe devolver un resumen con la temperatura media por semana y la semana más cálida.

29. **Análisis de actividad horaria**  
    Recibe una lista de horas en las que se ha producido actividad en un sistema (por ejemplo, `[9, 10, 10, 11, 14, 9, 17]`). Devuelve el rango horario con más actividad (hora y cantidad de ocurrencias).

30. **Resumen de texto con estadísticas**  
    Implementa una función que reciba un texto y devuelva un resumen con el número total de palabras, número total de frases, palabra más larga, y cuántas veces aparece cada palabra (ignorando mayúsculas y signos de puntuación).

31. **Clasificación de productos por categoría**  
    Escribe una función que reciba una lista de productos, donde cada producto es una tupla (nombre, categoría, precio). Devuelve un diccionario que agrupe los productos por categoría y calcule el precio medio por cada una.

32. **Agrupación de resultados deportivos**  
    Crea una función que reciba una lista de resultados de partidos con el formato `(equipo1, equipo2, goles1, goles2)` y devuelva una tabla con puntos por equipo (3 por victoria, 1 por empate).

33. **Control de acceso con intentos limitados**  
    Escribe una función que simule un sistema de login con nombre de usuario y contraseña. Solo se permiten tres intentos. La función debe devolver `True` si se accede correctamente y `False` si se exceden los intentos.

34. **Conversor horario con validación**  
    Crea una función que reciba una hora en formato `hh:mm` y devuelva la hora equivalente en formato de 12 horas con "am" o "pm". Valida que el formato sea correcto.

35. **Ranking de ventas por empleado**  
    Dado un diccionario con empleados como claves y listas de importes de ventas como valores, implementa una función que devuelva un ranking de mayor a menor venta total, con nombre y total acumulado.

36. **Sistema de matrícula de vehículos**  
    Diseña una función que valide si una matrícula española es correcta (formato: cuatro dígitos y tres letras, sin vocales). Luego, otra función que reciba una lista de matrículas y devuelva cuáles son válidas.

37. **Mapa de calor de asistencia**  
    Crea una función que reciba un diccionario con días de la semana como claves y número de asistentes como valores. Devuelve un gráfico textual de barras (`*`) proporcional a la cantidad de asistentes por día.

38. **Informe de stock de tienda**  
    Escribe una función que reciba un diccionario con productos como claves y tuplas `(stock, precio_unitario)` como valores. Devuelve una lista de productos agotados, el valor total del inventario y el producto más valioso.

39. **Simulación de lanzamientos de dado**  
    Crea una función que simule lanzar un dado n veces y devuelva un diccionario con la frecuencia de cada cara (del 1 al 6). Luego, genera una tabla con porcentajes de aparición.

40. **Control horario de fichajes**  
    Diseña una función que reciba una lista de horas de entrada y salida (tuplas `("08:45", "17:15")`) y calcule el número total de horas trabajadas al día y la media semanal. Valida los formatos.

41. **Análisis de tráfico por tramo horario**  
    Recibe un diccionario donde las claves son tramos horarios (`"08-09"`, `"09-10"`, etc.) y los valores son listas con el número de vehículos registrados por día. Calcula la media por tramo y señala los picos de tráfico.

42. **Clasificación de películas por género**  
    Crea una función que reciba una lista de películas en formato `(título, género, duración)` y devuelva un diccionario agrupado por género, con la media de duración y la lista de títulos ordenados alfabéticamente.

43. **Calendario de eventos**  
    Diseña una función que reciba una lista de eventos (cada uno como tupla: `("nombre", "fecha", "hora")`) y devuelva un calendario ordenado cronológicamente. Valida el formato de fechas y horas.

44. **Compresión de texto básica**  
    Crea una función que reciba un texto y lo comprima sustituyendo repeticiones consecutivas de caracteres por el carácter seguido del número de repeticiones (`"aaabbbc"` → `"a3b3c"`). Si no hay repeticiones, se devuelve igual.

45. **Histograma de calificaciones**  
    Dada una lista de notas entre 0 y 10, implementa una función que construya un histograma textual con intervalos de 2 puntos (0–1, 2–3, ...). Cada barra del histograma se representa con `*`.

46. **Analizador de respuestas de encuesta**  
    Recibe un diccionario donde las claves son preguntas y los valores listas de respuestas. La función debe mostrar para cada pregunta la respuesta más común y cuántas veces se repite.

47. **Conversor numérico a texto**  
    Escribe una función que convierta un número entre 0 y 999 en su representación textual en castellano (`145` → `"ciento cuarenta y cinco"`).

48. **Validación y análisis de DNI español**  
    Diseña una función que valide un DNI (8 dígitos + letra) y devuelva si es correcto. Otra función debe indicar el número de DNI válidos en una lista.

49. **Monitor de sensores**  
    Recibe un diccionario con identificadores de sensores como claves y listas de medidas como valores. La función devuelve para cada sensor la media, el máximo, el mínimo y detecta si hay valores atípicos (fuera de 2 desviaciones estándar).

50. **Resumen financiero por trimestre**  
    Dado un diccionario con meses como claves (`"Enero"`, `"Febrero"`, ...) y valores con ingresos y gastos, agrupa los datos por trimestre y devuelve el balance total por trimestre y el mes más rentable.

51. **Buscador de coincidencias parciales**  
    Implementa una función que reciba una lista de nombres y un texto de búsqueda. Devuelve los nombres que contienen el texto buscado, sin importar mayúsculas o acentos.

52. **Control de versiones de documentos**  
    Crea una función que reciba una lista de nombres de archivo con versión (`"informe_v1"`, `"informe_v2"`, etc.) y devuelva el nombre del documento con la versión más reciente.

53. **Simulador de votos con validación**  
    Diseña una función que reciba votos (strings) y un conjunto de opciones válidas. Devuelve un recuento de votos por opción e ignora los no válidos, mostrando advertencias.

54. **Tablero de puntuaciones de jugadores**  
    Recibe un diccionario donde las claves son jugadores y los valores listas de puntuaciones. La función debe devolver el ranking medio y el top 3 de mejores puntuaciones individuales.

55. **Gestión de pedidos con descuentos**  
    Dado un carrito con productos en formato `(nombre, cantidad, precio_unitario)`, implementa una función que calcule el total, aplicando descuentos por cantidad si corresponde (por ejemplo, 10% a partir de 5 unidades).

56. **Sistema de recomendaciones por afinidad**  
    Crea una función que reciba dos diccionarios: uno con usuarios y sus películas favoritas, y otro con películas recomendadas por género. Devuelve sugerencias personalizadas por usuario según sus gustos.

57. **Control de cambios en un proyecto**  
    Recibe una lista de cambios en un proyecto, cada uno con una fecha y descripción. Crea una función que los ordene y resuma por semana, indicando cuántos cambios hubo cada una.

58. **Agrupación de datos climáticos**  
    Dado un CSV (simulado como lista de tuplas) con fecha, ciudad y temperatura, agrupa los datos por ciudad y devuelve la temperatura media, mínima y máxima por ciudad.

59. **Validador y formateador de IBAN**  
    Escribe una función que reciba un número de cuenta bancaria en formato IBAN (por ejemplo, `"ES7620770024003102575766"`) y verifique si cumple con el formato español (22 caracteres: empieza por `"ES"`, seguido de 20 dígitos).  
    Si es válido, devuelve el IBAN formateado en bloques de 4 caracteres separados por espacio.  
    Si no es válido, muestra un mensaje de error claro indicando el problema (longitud incorrecta, prefijo erróneo o caracteres no numéricos).

60. **Resumen de asistencia por código QR**  
    Simula un sistema de control de asistencia mediante escaneos de códigos QR.  
    Crea una función que reciba una lista de tuplas con el formato `(nombre, fecha, hora)` representando cada escaneo.  
    La función debe generar un resumen por persona que indique:  
    - Cuántos días ha asistido.  
    - La fecha del primer y del último día en que asistió.  
    - El número total de escaneos registrados.  
    Ordena el resultado alfabéticamente por nombre y presenta los datos en un formato legible.

61. **Usuarios y roles (autenticación)**
```
users = [
    {"id": 1, "email": "ana@example.com",   "is_active": True,  "roles": ["admin", "editor"]},
    {"id": 2, "email": "borja@example.com", "is_active": False, "roles": ["viewer"]},
    {"id": 3, "email": "carla@example.com", "is_active": True,  "roles": ["editor", "viewer"]},
    {"id": 4, "email": "david@example.com", "is_active": True,  "roles": ["viewer"]},
    {"id": 5, "email": "eva@example.com",   "is_active": True,  "roles": ["editor", "editor"]}
]
```
    **Tareas**
    1. `emails_activos` → Devuelve una lista con los correos electrónicos de los usuarios activos, ordenados alfabéticamente.  
    2. `roles_unicos` → Devuelve el conjunto de todos los roles distintos presentes en el sistema.  
    3. `conteo_usuarios_por_rol` → Devuelve un diccionario que indique cuántos usuarios tienen cada rol, sin contar duplicados por persona.  
    4. `existe_inactivo_con_rol` → Devuelve un valor booleano indicando si hay algún usuario inactivo con el rol “editor”.  
    5. `activos_con_al_menos_un_rol` → Devuelve un valor booleano indicando si todos los usuarios activos tienen al menos un rol asignado.

62. **Pedidos de e-commerce**
```
orders = [
    {"id": 101, "date": "2025-01-06", "status": "paid",     "items": [{"sku": "A1", "qty": 2, "price": 19.9}, {"sku": "B2", "qty": 1, "price": 5.5}]},
    {"id": 102, "date": "2025-01-06", "status": "refunded", "items": [{"sku": "A1", "qty": 1, "price": 19.9}]},
    {"id": 103, "date": "2025-01-07", "status": "paid",     "items": [{"sku": "C3", "qty": 3, "price": 7.0}]},
    {"id": 104, "date": "2025-01-07", "status": "paid",     "items": [{"sku": "A1", "qty": 1, "price": 19.9}, {"sku": "C3", "qty": 2, "price": 7.0}]},
    {"id": 105, "date": "2025-01-10", "status": "pending",  "items": []}
]
```

**Tareas**
1. `total_pedido` → Devuelve el importe total de un pedido, calculado a partir de las cantidades y precios.  
2. `ingreso_total_pagados` → Devuelve el importe total ingresado considerando solo los pedidos con estado “paid”.  
3. `sku_top_unidades_pagados` → Devuelve el identificador de producto (SKU) con mayor número total de unidades vendidas en pedidos pagados.  
4. `ordenar_pedidos_por_total_desc` → Devuelve la lista de pedidos ordenada por importe total descendente.  
5. `ingreso_por_fecha_pagados` → Devuelve un diccionario con las fechas y el ingreso total registrado cada día para pedidos pagados.


63. **Pedidos multi-almacén con pagos y envíos (e-commerce avanzado)**

```
orders = [
    {
        "id": 501,
        "customer": {"id": 1, "email": "ana@example.com", "tier": "gold"},
        "created_at": "2025-03-10T09:30:00",
        "status": "paid",
        "items": [
            {"sku": "A1", "qty": 2, "price": 19.90, "discounts": [{"type": "coupon", "value": 5.00}]},
            {"sku": "A1", "qty": 1, "price": 5.50, "discounts": []}
        ],
        "tax": {"rate": 0.21, "region": "ES"},
        "payments": [
            {"method": "card", "amount": 30.00, "auth_code": "X1"},
            {"method": "wallet", "amount": 12.30, "auth_code": "W9"}
        ],
        "shipments": [
            {
                "warehouse": "MAD-1",
                "carrier": "PackGo",
                "packages": [
                    {"tracking": "PG-1001", "items": [{"sku": "A1", "qty": 1}], "status": "delivered"},
                    {"tracking": "PG-1002", "items": [{"sku": "A1", "qty": 1}, {"sku": "B2", "qty": 1}], "status": "in_transit"}
                ]
            }
        ]
    },
    {
        "id": 502,
        "customer": {"id": 2, "email": "borja@example.com", "tier": "standard"},
        "created_at": "2025-03-10T10:10:00",
        "status": "paid",
        "items": [
            {"sku": "C3", "qty": 3, "price": 7.00, "discounts": [{"type": "tier", "value": 2.00}]}
        ],
        "tax": {"rate": 0.10, "region": "PT"},
        "payments": [
            {"method": "card", "amount": 18.70, "auth_code": "X2"}
        ],
        "shipments": [
            {
                "warehouse": "LIS-2",
                "carrier": "IberShip",
                "packages": [
                    {"tracking": "IB-2001", "items": [{"sku": "C3", "qty": 2}], "status": "delivered"}
                ]
            },
            {
                "warehouse": "LIS-2",
                "carrier": "IberShip",
                "packages": [
                    {"tracking": "IB-2002", "items": [{"sku": "C3", "qty": 1}], "status": "label_created"}
                ]
            }
        ]
    },
    {
        "id": 503,
        "customer": {"id": 1, "email": "ana@example.com", "tier": "gold"},
        "created_at": "2025-03-11T08:05:00",
        "status": "pending",
        "items": [
            {"sku": "A1", "qty": 1, "price": 19.90, "discounts": []}
        ],
        "tax": {"rate": 0.21, "region": "ES"},
        "payments": [],
        "shipments": []
    },
    {
        "id": 504,
        "customer": {"id": 3, "email": "carla@example.com", "tier": "premium"},
        "created_at": "2025-03-12T15:45:00",
        "status": "paid",
        "items": [
            {"sku": "D4", "qty": 1, "price": 100.00, "discounts": [{"type": "promo", "value": 10.00}]},
            {"sku": "A1", "qty": 2, "price": 19.90, "discounts": []}
        ],
        "tax": {"rate": 0.21, "region": "ES"},
        "payments": [
            {"method": "card", "amount": 129.18, "auth_code": "X3"}
        ],
        "shipments": [
            {
                "warehouse": "VAL-1",
                "carrier": "FastShip",
                "packages": [
                    {"tracking": "FS-3001", "items": [{"sku": "D4", "qty": 1}, {"sku": "A1", "qty": 1}], "status": "in_transit"}
                ]
            }
        ]
    }
]
```

**Tareas**

1. `emails_clientes` → Devuelve la lista de direcciones de correo de todos los clientes que han realizado al menos un pedido (sin duplicados).  
2. `pedidos_pagados` → Devuelve la lista de pedidos cuyo estado sea `"paid"`.  
3. `skus_distintos` → Devuelve el conjunto de todos los códigos de producto (`sku`) presentes en los pedidos.  
4. `total_descuentos_por_pedido` → Devuelve un diccionario con la suma total de descuentos aplicados por pedido.  
5. `importe_neto_por_pedido` → Devuelve un diccionario que asocia cada pedido con su importe neto (precio × cantidad − descuentos).  
6. `importe_total_con_impuestos` → Devuelve un diccionario que asocia cada pedido con el total final aplicando el IVA correspondiente (`tax["rate"]`).  
7. `recaudado_por_metodo_pago` → Devuelve un diccionario con el total recaudado por cada método de pago.  
8. `promedio_ticket_por_cliente` → Devuelve un diccionario que asocia cada cliente con el promedio de importe total de sus pedidos pagados.  
9. `productos_mas_vendidos` → Devuelve un diccionario con las unidades totales vendidas por SKU en todos los pedidos pagados.  
10. `unidades_enviadas_por_sku` → Devuelve un diccionario con las unidades enviadas por SKU, sumando todos los paquetes de todos los envíos.  
11. `estado_envio_por_pedido` → Devuelve un diccionario que resume el estado global de envío de cada pedido según el progreso de sus paquetes (`delivered`, `in_transit`, `label_created`, `no_shipping`).  
12. `ingreso_bruto_por_region_fiscal` → Devuelve un diccionario que agrupa por región fiscal (`tax["region"]`) y acumula el ingreso bruto antes de impuestos.  
13. `clientes_por_nivel` → Devuelve un diccionario donde cada nivel de cliente (`tier`) contiene el conjunto de emails de los clientes de ese nivel.  
14. `sku_mas_frecuente_en_envios` → Devuelve el código de producto (`sku`) que aparece en más paquetes de envío, sin importar el pedido.  
15. `pedidos_con_anomalias_pago` → Devuelve una lista de los pedidos donde la suma de los pagos registrados no coincide con el importe total esperado (considerando descuentos e impuestos).

---

64. **API del tiempo (pronóstico diario y horario)**

```
weather = [
    {
        "city": "Madrid",
        "coords": {"lat": 40.4168, "lon": -3.7038},
        "alerts": [{"code": "UV", "level": "moderate"}],
        "daily": [
            {
                "date": "2025-03-10",
                "temp": {"min": 6.0, "max": 17.5},
                "humidity": 55,
                "wind_kmh": 18,
                "precip_mm": 0.0,
                "condition": "Clear",
                "hourly": [
                    {"time": "2025-03-10T09:00", "temp": 10.2, "pop": 0.05},
                    {"time": "2025-03-10T12:00", "temp": 16.8, "pop": 0.00},
                    {"time": "2025-03-10T18:00", "temp": 14.1, "pop": 0.10}
                ]
            },
            {
                "date": "2025-03-11",
                "temp": {"min": 7.5, "max": 16.0},
                "humidity": 62,
                "wind_kmh": 22,
                "precip_mm": 1.6,
                "condition": "Rain",
                "hourly": [
                    {"time": "2025-03-11T09:00", "temp": 9.8, "pop": 0.60},
                    {"time": "2025-03-11T12:00", "temp": 14.5, "pop": 0.70},
                    {"time": "2025-03-11T18:00", "temp": 12.2, "pop": 0.40}
                ]
            },
            {
                "date": "2025-03-12",
                "temp": {"min": 8.0, "max": 18.2},
                "humidity": 50,
                "wind_kmh": 19,
                "precip_mm": 0.0,
                "condition": "Partly Cloudy",
                "hourly": [
                    {"time": "2025-03-12T09:00", "temp": 11.2, "pop": 0.10},
                    {"time": "2025-03-12T12:00", "temp": 17.2, "pop": 0.10},
                    {"time": "2025-03-12T18:00", "temp": 15.0, "pop": 0.05}
                ]
            }
        ]
    },
    {
        "city": "Barcelona",
        "coords": {"lat": 41.3874, "lon": 2.1686},
        "alerts": [],
        "daily": [
            {
                "date": "2025-03-10",
                "temp": {"min": 9.0, "max": 18.0},
                "humidity": 60,
                "wind_kmh": 28,
                "precip_mm": 0.0,
                "condition": "Clear",
                "hourly": [
                    {"time": "2025-03-10T09:00", "temp": 12.5, "pop": 0.00},
                    {"time": "2025-03-10T12:00", "temp": 17.1, "pop": 0.05}
                ]
            },
            {
                "date": "2025-03-11",
                "temp": {"min": 10.2, "max": 19.3},
                "humidity": 58,
                "wind_kmh": 35,
                "precip_mm": 0.0,
                "condition": "Windy",
                "hourly": [
                    {"time": "2025-03-11T09:00", "temp": 13.0, "pop": 0.10},
                    {"time": "2025-03-11T12:00", "temp": 18.6, "pop": 0.10}
                ]
            },
            {
                "date": "2025-03-12",
                "temp": {"min": 11.0, "max": 17.0},
                "humidity": 70,
                "wind_kmh": 20,
                "precip_mm": 3.4,
                "condition": "Rain",
                "hourly": [
                    {"time": "2025-03-12T09:00", "temp": 12.0, "pop": 0.65},
                    {"time": "2025-03-12T12:00", "temp": 15.2, "pop": 0.75}
                ]
            }
        ]
    }
]
```
**Tareas**

1. `ciudades_disponibles` → Devuelve el conjunto de nombres de ciudad presentes en los datos.  
2. `fechas_por_ciudad` → Devuelve un diccionario que asocia cada ciudad con la lista de fechas disponibles en su pronóstico diario.  
3. `dias_con_lluvia` → Devuelve una lista de tuplas con ciudad y fecha donde `precip_mm` sea mayor que 0.  
4. `max_temp_por_ciudad` → Devuelve un diccionario que asocia cada ciudad con su temperatura máxima global (el mayor `temp["max"]` de sus días).  
5. `min_temp_por_ciudad` → Devuelve un diccionario que asocia cada ciudad con su temperatura mínima global (el menor `temp["min"]`).  
6. `dias_despejados_por_ciudad` → Devuelve un diccionario con el número de días cuyo `condition` sea `"Clear"` por ciudad.  
7. `viento_fuerte_por_ciudad` → Devuelve una lista con las ciudades que tengan al menus un `wind_kmh` mayor o igual que 30.  
8. `alertas_por_ciudad` → Devuelve un diccionario donde cada ciudad se asocia con el conjunto de códigos de alerta activos.  
9. `horas_con_alta_prob_precipitacion` → Devuelve una lista de tuplas con ciudad, fecha y hora para todas las horas con `pop` mayor o igual que 0.6.  
10. `resumen_diario_simple` → Devuelve un diccionario que asocia cada ciudad con una lista de resúmenes por día (cada resumen con `date`, `min`, `max`, `condition`).
