import json

lista_de_datos = []
suma_promedios = 0
cant_personas = 0
nota_alumno_mateo = 0
alumno_mas_mateo = None

try:
    archivo_json = 'archivo.json'
    with open(archivo_json, 'r', encoding='utf-8') as archivo:
        lista_de_datos = json.load(archivo)
        for dato in lista_de_datos:
            nombre_alumno = f"{dato['nombre']} {dato['apellido']}"
            nota_promedio_alumno = (float(dato['notas']['nota1'])+float(dato['notas']['nota2'])+float(dato['notas']['nota3']))/3
            if nota_promedio_alumno > nota_alumno_mateo:
                 nota_alumno_mateo = nota_promedio_alumno
                 alumno_mas_mateo = [nombre_alumno, nota_alumno_mateo]
            suma_promedios += int(dato['asistencia_final'])
            cant_personas += 1
            # print(f"El promedio de {nombre_alumno} es {nota_promedio_alumno}")

    print("El promedio de asistencia es", round(suma_promedios/cant_personas, 2))
    print(f"El alumno más mateo es {alumno_mas_mateo[0]} con un {round(alumno_mas_mateo[1], 2)}")

except Exception as e:
    print(e)