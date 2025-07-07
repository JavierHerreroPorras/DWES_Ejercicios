# Lectura y escritura simultáneas
with open("miarchivo.txt", "r+") as f:
    datos = f.read()
    f.seek(0)
    f.write("Encabezado añadido\n")
#Añade al principio del archivo sin borrarlo