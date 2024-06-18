# Crear aplicación que realice lo siguiente:

# Transformar datos CSV a una lista de diccionarios
# Crear Menú que tengan las siguientes funcionalidades
# Obtener el mejor alumno por asignatura
# Obtener el mejor alumno por año
# Obtener la asignatura de cada año con mejor asistencia
import csv
bd_datos = []
try:
    archivo_csv = 'alumnos_detallado.csv'
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        datos = csv.reader(archivo)
        next(archivo)
        for dato in datos:
            lista_de_datos = {}
            lista_de_datos['rut'] = dato[0]
            lista_de_datos['nombre'] = dato[1]
            lista_de_datos['apellido'] = dato[2]
            lista_de_datos['curso'] = dato[3]
            lista_de_datos['asignatura'] = dato[4]
            # TODO
            lista_de_datos['nombre'] = dato[5]
            lista_de_datos['nombre'] = dato[6]
            lista_de_datos['nombre'] = dato[7]
            lista_de_datos['nombre'] = dato[8]
            bd_datos.append(lista_de_datos)
    
    print(bd_datos)
except Exception as e:
    print(e)