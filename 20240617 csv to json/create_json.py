import csv
import json

archivo_csv = 'estudiantes.csv'
archivo_json = 'archivo.json' 
lista_json = []

try:
    print(">>> Inicio del programa")
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        next(archivo)
        datos = csv.reader(archivo)
        for dato in datos:
            datos_json = {}
            datos_json['nombre'] = dato[0]
            datos_json['apellido'] = dato[1]
            datos_json['asignatura'] = dato[2]
            datos_json['notas'] = {}
            datos_json['notas']['nota1'] = dato[3]
            datos_json['notas']['nota2'] = dato[4]
            datos_json['notas']['nota3'] = dato[5]
            datos_json['asistencia_final'] = dato[6]
            lista_json.append(datos_json)
    with open(archivo_json, 'w', encoding='utf-8') as archivo:
        json.dump(lista_json, archivo, indent=4, ensure_ascii=False)    
except Exception as e:
    print(e)