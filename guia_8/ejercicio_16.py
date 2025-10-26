
def calcular_promedio_por_estudiante(notas : list[tuple[str,float]]) -> dict[str,float]:
    diccionario_notas : dict[str,float] = dict()
    diccionario_occurencias : dict[str,int] = dict()
    diccionario_promedios : dict[str,float] = dict()

    for nombre,nota in notas:
        if nombre in diccionario_notas:
            diccionario_notas[nombre] += nota
            diccionario_occurencias[nombre] += 1
        else :
            diccionario_notas[nombre] = nota
            diccionario_occurencias[nombre] = 1

    for nombre,sumatoria_notas in diccionario_notas.items():
        diccionario_promedios[nombre] = sumatoria_notas / diccionario_occurencias[nombre]

    return diccionario_promedios

print(calcular_promedio_por_estudiante([("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]))