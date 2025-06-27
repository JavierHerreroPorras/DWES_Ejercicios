#Tuplas
# Definición de una tupla:
t = (1, 2, True, "python")
# Tupla de un elemento:
t = (1,)
# Acceso: Igual que el de las listas.
mi_var= t[0] # mi_var es 1
mi_var= t[0:2] # mi_var es (1,2)

#Métodos de tuplas:
# Las tuplas son inmutables, por lo que no tienen métodos para modificar su contenido.
# Sin embargo, se pueden usar algunos métodos de las secuencias:
# Contar el número de ocurrencias de un elemento
t = (1, 2, 2, 3)
count_2 = t.count(2)  # count_2 vale 2
# Obtener el índice del primer elemento encontrado
index_3 = t.index(3)  # index_3 vale 3 (índice del primer 3)
# Concatenar dos tuplas
t1 = (1, 2)
t2 = (3, 4)
t_concat = t1 + t2  # t_concat vale (1, 2, 3, 4)
# Repetir una tupla
t_repeated = t1 * 3  # t_repeated vale (1, 2, 1, 2, 1, 2)
# Comprobar si un elemento está en la tupla
is_2_in_tuple = 2 in t  # is_2_in_tuple vale True
# Comprobar si un elemento no está en la tupla
is_5_not_in_tuple = 5 not in t  # is_5_not_in_tuple vale True
# Tuplas con un solo elemento
# Las tuplas con un solo elemento deben tener una coma al final para diferenciarlas de un valor entre paréntesis.
# Ejemplo de tupla con un solo elemento
t_single = (42,)  # Tupla con un solo elemento
# Acceso a elementos de una tupla
mi_var = t_single[0]  # mi_var es 42
# Tuplas anidadas
t_nested = (1, (2, 3), (4, 5))
# Acceso a elementos de una tupla anidada
mi_var = t_nested[1][0]  # mi_var es 2
# Tuplas y listas