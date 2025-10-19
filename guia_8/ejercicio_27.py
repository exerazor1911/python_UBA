def promedio_estudiante(notas_de_estudiantes : list[str], lu : str) -> float:
    acum : float = 0
    contador : int = 0

    for nota in notas_de_estudiantes:
        csv : list[str] = nota.split(',')
        if csv[0] == lu:
            contador += 1
            acum += float(csv[3])
    
    return acum / contador



def calcular_promedio_por_estudiante(nombre_archivo_notas, nombre_archivo_promedios : str):
    notas : list[str]

    with open(nombre_archivo_notas, 'r') as archivo_notas:
        notas = archivo_notas.readlines()

    lu_promedios : dict[str,float] = {}

    for nota in notas:
        csv : list[str] = nota.split(',')
        lu : str = csv[0]
        if lu not in lu_promedios:
            lu_promedios[lu] = promedio_estudiante(notas, lu)

    with open(nombre_archivo_promedios, 'w') as archivo_promedios:
        for lu, promedio in lu_promedios.items():
            archivo_promedios.write(f"{lu},{promedio}\n")

calcular_promedio_por_estudiante('guia_8/calcular_promedio_por_estudiante_notas.csv','guia_8/calcular_promedio_por_estudiante_promedios.csv')