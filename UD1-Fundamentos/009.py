# Conversión de tipos en Python
x=6
y="3"
# z=x+y  TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Para evitar el error de tipo, debemos convertir 'y' a un entero
z=x+int(y)
print(z)
