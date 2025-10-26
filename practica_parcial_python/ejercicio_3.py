def contar_cantidad_promedio_de_salas_en_rango(tiempos : list[int]) -> tuple[int,float]:
    cantidad : int = 0
    acum : int = 0

    for tiempo in tiempos:
        if tiempo > 0 and tiempo < 61:
            cantidad += 1
            acum += tiempo

    if cantidad == 0:
        return 0, 0.0

    return cantidad, acum / cantidad

def promedio_de_salidas(registro : dict[str,list[int]]) -> dict[str,tuple[int,float]]:
    nombre_cant_salas_promedio_salas_en_rango : dict[str,tuple[int,float]] = {}
    for amigo, tiempos in registro.items():
        nombre_cant_salas_promedio_salas_en_rango[amigo] = contar_cantidad_promedio_de_salas_en_rango(tiempos)

    return nombre_cant_salas_promedio_salas_en_rango

print(promedio_de_salidas({
    "a": [61,60,59,58],
    "b": [1,2,3,0],
    "c": [0,61,0,61],
    "d": [0,0,0,0],
    "e": [61,61,61,61]
}))