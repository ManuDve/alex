import csv

lista_de_datos = []

with open('estudiantes.csv', 'r', newline='', encoding='utf-8') as archivo:
    lista_de_datos = csv.reader(archivo)
    
    for fila in lista_de_datos:
        print(fila)