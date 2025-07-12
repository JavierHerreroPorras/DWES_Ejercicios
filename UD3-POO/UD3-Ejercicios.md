# UD3 - Programación Orientada a Objetos
Ejercicios de Programación Orientada a Objetos

## Ejercicio 1: Clase `Coche`
Crea una clase `Coche` que tenga los siguientes atributos:
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
Crea un método mágico `__clone__`que