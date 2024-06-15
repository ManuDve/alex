import csv

lista_de_datos = []
suma_promedios = 0
cant_personas = 0
nota_alumno_mateo = 0
alumno_mas_mateo = None

with open('estudiantes.csv', 'r', newline='', encoding='utf-8') as archivo:

    lista_de_datos = csv.reader(archivo)
    for fila in lista_de_datos:
        if fila[6] == "asistencia_final":
            continue
        else:
            nombre_alumno = f"{fila[0]} {fila[1]}"
            nota_promedio_alumno = (float(fila[3])+float(fila[4])+float(fila[5]))/3
            if nota_promedio_alumno > nota_alumno_mateo:
                nota_alumno_mateo = nota_promedio_alumno
                alumno_mas_mateo = [nombre_alumno, nota_alumno_mateo]
            suma_promedios += int(fila[6])
            cant_personas += 1
            print(f"El promedio de {nombre_alumno}, {nota_promedio_alumno}")
    
    print("El promedio es", suma_promedios/cant_personas)
    print(f"El alumno más mateo es {alumno_mas_mateo}")
