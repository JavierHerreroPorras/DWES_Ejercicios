# UA3 - Programación Orientada a Objetos
Ejercicios de Programación Orientada a Objetos

## Ejercicios clase - POO
1. Crea una clase `Punto` con dos atributos (`x`, `y`) que:
- Imprima un mensaje al crearse (`__init__`) y al destruirse (`__del__`).
- Devuelva una representación legible con `__str__`.
- Permita sumar dos puntos con `+` mediante `__add__`.
- Permita comparar igualdad con `==` mediante `__eq__`.

Prueba creando varios puntos, mostrándolos, sumándolos y comparándolos.

---

2. Crea una clase `Persona` con atributos `nombre` y `edad`, y un método `presentarse()`.  
Crea `Empleado` que **herede** de `Persona`, añada `salario` y **sobrescriba** `presentarse()` para incluir el salario (puedes apoyarte en `super()`).

Crea instancias de ambas clases y muestra el comportamiento distinto de `presentarse()`.

---

3. Crea `CuentaBancaria` con atributo “privado” `__saldo`. Expón `saldo` exclusivamente mediante:
- `@property` (getter) para leer,
- `@saldo.setter` para asignar (rechaza saldos negativos),
- `@saldo.deleter` para dejar el saldo a 0 e informar.

Crea un objeto y prueba lectura, modificación y borrado lógico del saldo.

---
## Ejercicios clase - Excepciones
1. Crea un programa que pida dos números al usuario e intente dividirlos.

Pasos:
1. Usa `try` y `except` para **capturar divisiones por cero** y **errores de tipo** (por ejemplo, si el usuario escribe texto).  
2. Si la división es correcta, muestra el resultado dentro del bloque `else`.  
3. Usa un bloque `finally` para mostrar un mensaje de cierre, independientemente del resultado.

**Ejemplo esperado:**
```
Introduce el numerador: 10
Introduce el denominador: 0
Error: No se puede dividir entre cero.
Fin del programa.
```

---

2. Crea una lista con cinco números y pide al usuario un índice para mostrar un elemento.

Pasos: 
1. Captura los errores `IndexError` (índice fuera de rango) y `ValueError` (entrada no numérica).  
2. Usa `else` para imprimir el valor si la entrada es válida.  
3. Usa `finally` para mostrar el contenido completo de la lista antes de finalizar.

**Ejemplo esperado:**
```
Introduce el índice del elemento: 10
Error: El índice no existe.
Lista completa: [3, 8, 12, 5, 9]
```

---

3. Crea un programa que pida al usuario su edad y valide que sea un número positivo.

Pasos:
1. Lanza una excepción manual (`raise ValueError`) si la edad es negativa o cero.  
2. Captura los posibles errores (`ValueError`, `TypeError`, etc.) con `except`.  
3. Si la edad es válida, muestra un mensaje dentro de `else`.  
4. Usa `finally` para imprimir un mensaje de despedida, ocurra lo que ocurra.

**Ejemplo esperado:**
```
Introduce tu edad: -5
Error: La edad debe ser un número positivo.
Gracias por usar el programa.
```

---

## Ejercicios adicionales: POO

---
*Ejercicio introductorio* Crea una clase `Coche` que tenga los siguientes atributos:
- `marca`: cadena de texto que representa la marca del coche.
- `modelo`: cadena de texto que representa el modelo del coche.
- `año`: entero que representa el año de fabricación del coche.
- `color`: cadena de texto que representa el color del coche.
- `kilometraje`: flotante que representa el kilometraje del coche.
- `precio`: flotante que representa el precio del coche.
- `en_venta`: booleano que indica si el coche está en venta o no.
- `vendedor`: cadena de texto que representa el nombre del vendedor del coche.
- `fecha_publicacion`: cadena de texto que representa la fecha de publicación del anuncio del coche.
- `descripcion`: cadena de texto que representa una descripción del coche.
- `imagen`: cadena de texto que representa la URL de una imagen del coche.
- `ubicacion`: cadena de texto que representa la ubicación del coche.
- `contacto`: cadena de texto que representa el contacto del vendedor.
- `estado`: cadena de texto que representa el estado del coche (nuevo, usado, etc.).
- `transmision`: cadena de texto que representa el tipo de transmisión del coche (manual, automático, etc.).
- `combustible`: cadena de texto que representa el tipo de combustible del coche (gasolina, diésel, eléctrico, etc.).
- `numero_puertas`: entero que representa el número de puertas del coche.
- `numero_asientos`: entero que representa el número de asientos del coche.
- `potencia`: flotante que representa la potencia del coche en caballos de fuerza.
- `cilindrada`: flotante que representa la cilindrada del motor del coche.
- `consumo`: flotante que representa el consumo de combustible del coche en litros cada 100 km.
- `emisiones`: flotante que representa las emisiones de CO2 del coche en gramos por km.
- `garantia`: cadena de texto que representa la garantía del coche.
- `historial_mantenimiento`: lista de cadenas de texto que representa el historial de mantenimiento del coche.
- `numero_propietarios`: entero que representa el número de propietarios anteriores del coche.
- `numero_llaves`: entero que representa el número de llaves del coche.
- `numero_neumaticos`: entero que representa el número de neumáticos del coche.
- `fecha_ultima_revision`: cadena de texto que representa la fecha de la última revisión del coche.
- `fecha_proxima_revision`: cadena de texto que representa la fecha de la próxima revisión del coche.
- `fecha_ultima_itv`: cadena de texto que representa la fecha de la última ITV del coche.
- `fecha_proxima_itv`: cadena de texto que representa la fecha de la próxima ITV del coche.
- `fecha_ultima_seguro`: cadena de texto que representa la fecha del último seguro del coche.

Crea un método `mostrar_informacion` que imprima por consola toda la información del coche de forma legible.
Crea un método `actualizar_precio` que permita actualizar el precio del coche.
Crea un método `actualizar_kilometraje` que permita actualizar el kilometraje del coche.
Crea un método `actualizar_estado` que permita actualizar el estado del coche.
Crea un método `actualizar_fecha_publicacion` que permita actualizar la fecha de publicación del anuncio del coche.
Crea un método `actualizar_descripcion` que permita actualizar la descripción del coche.
Crea un método `actualizar_imagen` que permita actualizar la URL de la imagen del coche.
Crea un método `actualizar_ubicacion` que permita actualizar la ubicación del coche.
Crea un método `actualizar_contacto` que permita actualizar el contacto del vendedor.
Crea un método `actualizar_historial_mantenimiento` que permita añadir una entrada al historial de mantenimiento del coche.
Crea un método `actualizar_numero_propietarios` que permita actualizar el número de propietarios anteriores del coche.
Crea un método `actualizar_numero_llaves` que permita actualizar el número de llaves del coche.
Crea un método `actualizar_numero_neumaticos` que permita actualizar el número de neumáticos del coche.
Crea un método `actualizar_fecha_ultima_revision` que permita actualizar la fecha de la última revisión del coche.
Crea un método `actualizar_fecha_proxima_revision` que permita actualizar la fecha de la próxima revisión del coche.
Crea un método `actualizar_fecha_ultima_itv` que permita actualizar la fecha de la última ITV del coche.
Crea un método `actualizar_fecha_proxima_itv` que permita actualizar la fecha de la próxima ITV del coche.
Crea un método `actualizar_fecha_ultima_seguro` que permita actualizar la fecha del último seguro del coche.

Crea un método `mostrar_historial_mantenimiento` que imprima por consola el historial de mantenimiento del coche.
Crea un método `mostrar_estado` que imprima por consola el estado del coche.
Crea un método `mostrar_precio` que imprima por consola el precio del coche.
Crea un método `mostrar_kilometraje` que imprima por consola el kilometraje del coche.
Crea un método `mostrar_fecha_publicacion` que imprima por consola la fecha de publicación del anuncio del coche.
Crea un método `mostrar_descripcion` que imprima por consola la descripción del coche.
Crea un método `mostrar_imagen` que imprima por consola la URL de la imagen del coche.
Crea un método `mostrar_ubicacion` que imprima por consola la ubicación del coche.
Crea un método `mostrar_contacto` que imprima por consola el contacto del vendedor.
Crea un método `mostrar_numero_propietarios` que imprima por consola el número de propietarios anteriores del coche.
Crea un método `mostrar_numero_llaves` que imprima por consola el número de llaves del coche.
Crea un método `mostrar_numero_neumaticos` que imprima por consola el número de neumáticos del coche.
Crea un método `mostrar_fecha_ultima_revision` que imprima por consola la fecha de la última revisión del coche.
Crea un método `mostrar_fecha_proxima_revision` que imprima por consola la fecha de la próxima revisión del coche.
Crea un método `mostrar_fecha_ultima_itv` que imprima por consola la fecha de la última ITV del coche.
Crea un método `mostrar_fecha_proxima_itv` que imprima por consola la fecha de la próxima ITV del coche.

#Métodos mágicos:
Crea un método mágico `__str__` que devuelva una representación en cadena del coche.
Crea un método mágico `__repr__` que devuelva una representación en cadena del coche para depuración.
Crea un método mágico `__eq__` que compare dos coches por su marca, modelo y año.
Crea un método mágico `__lt__` que compare dos coches por su precio.
Crea un método mágico `__gt__` que compare dos coches por su kilometraje.
Crea un método mágico `__len__` que devuelva el número de atributos del coche.
Crea un método mágico `__getitem__` que permita acceder a los atributos del coche por su nombre.
Crea un método mágico `__setitem__` que permita modificar los atributos del coche por su nombre.
Crea un método mágico `__delitem__` que permita eliminar un atributo del coche por su nombre.
Crea un método mágico `__contains__` que permita comprobar si un atributo existe en el coche.


1. **Clase `Producto`**  
   Crea una clase que represente un producto con nombre, precio y stock.  
   Incluye métodos para vender, reponer y mostrar el estado del producto mediante `__str__`.

2. **Clase `Fracción`**  
   Define una clase para representar fracciones con numerador y denominador.  
   Permite sumar, restar, multiplicar y dividir fracciones usando operadores (`__add__`, etc.) y simplificarlas automáticamente.

3. **Clase `Persona` con validación**  
   Modela una persona con nombre, edad y DNI.  
   Usa `@property` para validar que la edad sea positiva, e incluye una excepción personalizada si no lo es.

4. **Clase `CajaFuerte` con métodos privados**  
   Representa una caja fuerte protegida por contraseña.  
   Solo puede accederse al contenido si se llama a un método que internamente verifique la contraseña correcta mediante un método privado.

5. **Clase `Moneda` ordenable y hasheable**  
   Crea una clase `Moneda` que se pueda comparar e insertar en estructuras como sets y diccionarios.  
   Usa `@total_ordering` para implementar `__lt__`, `__eq__`, y `__hash__`.

6. **Clase `CuentaBancaria` con control de errores y operadores**  
   Simula una cuenta bancaria con métodos `ingresar`, `retirar`, control de saldo insuficiente con excepciones, y la posibilidad de fusionar cuentas con `+`.

7. **Clase `Rectángulo` con `__len__` y validación**  
   Representa un rectángulo con atributos validados.  
   Al aplicar `len()` devuelve el área. Permite compararse por igualdad y representarse por pantalla.

8. **Clase `Cadena` con operadores sobrecargados**  
   Simula el comportamiento de una cadena.  
   Soporta concatenación (`+`), repetición (`*`), comparación (`==`) y representación (`__str__`).

9. **Clase `Contador` (Singleton)**  
   Implementa una clase contador compartido por todas las instancias.  
   Usa el patrón singleton con `__new__` para asegurar que solo haya una instancia global.

10. **Clase `Email` con validación y propiedad protegida**  
    Crea una clase que represente un correo electrónico.  
    Usa `@property` para validar el formato y lanza una excepción personalizada si es incorrecto.

11. **Clases `Animal` y `Perro` con herencia y polimorfismo**  
    Define una jerarquía donde cada animal puede emitir un sonido.  
    `Perro` sobreescribe el método base y añade un atributo propio.

12. **Clases `CuentaBancaria`, `CuentaCorriente`, `CuentaAhorro`**  
    Implementa una jerarquía bancaria.  
    Las subclases añaden comportamiento específico como comisiones o intereses.  
    Se debe poder instanciar cualquier cuenta y mostrarla con `__str__`.

13. **Clase `Matriz` con validaciones y operadores**  
    Representa matrices y permite sumarlas, restarlas y multiplicarlas.  
    Implementa validaciones de tamaño y una representación en varias líneas (`__str__`).

14. **Clase `Empleado` ordenable por salario**  
    Define empleados con nombre y sueldo.  
    Implementa ordenación usando `@total_ordering` y métodos mágicos (`__lt__`, `__eq__`).

15. **Clase `Vehículo` con encapsulación y destrucción**  
    Usa atributos privados y métodos para cambiar la velocidad.  
    El método `__del__` muestra un mensaje cuando el objeto es destruido.

16. **Clase `Triángulo` con validación de lados y métodos personalizados**  
    Verifica al crearse que los tres lados conformen un triángulo válido.  
    Incluye métodos como `es_equilatero`, `perímetro` y lanza una excepción si los lados no son válidos.

17. **Clases `DictSeguro` y `Protegido` con herencia múltiple**  
    Crea una clase diccionario que puede bloquearse o desbloquearse.  
    Al estar bloqueado no permite modificar sus valores.  
    Utiliza herencia múltiple para combinar el comportamiento.

18. **Clase `Fecha` con validación y operadores**  
    Modela fechas reales teniendo en cuenta los días de cada mes y años bisiestos.  
    Implementa comparación, representación y hashing.

19. **Clase `Ruta` con iteración personalizada**  
    Implementa una lista de puntos que pueden recorrerse paso a paso mediante un iterador (`__iter__`, `__next__`).  
    Permite reiniciar el recorrido.

20. **Clase `ArchivoTexto` con `with` y control de errores**  
    Gestiona la apertura, lectura y escritura de archivos.  
    Implementa `__enter__` y `__exit__` para integrarse con `with`.  
    Controla excepciones de apertura o escritura.

21. **Clases `Usuario`, `Moderador`, `Administrador` con herencia**  
    Crea diferentes tipos de usuarios con niveles de permiso.  
    Cada clase implementa métodos `ver`, `editar`, `eliminar`, sobrescribiéndolos según su rol.  
    Usa `NotImplementedError` en la clase base para métodos abstractos.

22. **Clase `ProductoClonable` con método `clone()`**  
    Representa productos que pueden duplicarse.  
    Implementa un método `clone()` que genera una copia exacta del objeto con sus atributos.

23. **Clase `Temperatura` convertible entre unidades**  
    Guarda la temperatura en una unidad base y permite consultarla y modificarla en otras (`Celsius`, `Fahrenheit`, `Kelvin`) usando `@property`.

24. **Clase `JuegoDeCartas` con baraja y excepciones**  
    Simula un mazo de cartas que puede barajarse y repartir.  
    Lanza una excepción personalizada `MazoVacioError` si se intenta repartir sin cartas.  
    Permite reiniciar la baraja.

25. **Sistema completo: Clases `Hotel`, `Habitación`, `Cliente`, `Reserva`**  
    Diseña un sistema de reservas donde:  
    - Las habitaciones tienen número, tipo y estado.  
    - Los clientes tienen nombre y DNI validado.  
    - Las reservas asocian un cliente con una habitación en una fecha.  
    - El hotel gestiona habitaciones, disponibilidad y permite listar reservas.  
    Usa propiedades, métodos especiales, herencia y excepciones (`HabitacionOcupadaError`, `ClienteInvalidoError`, etc.).  
    Este ejercicio integra múltiples clases y conceptos en un pequeño sistema orientado a objetos.
