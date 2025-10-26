def contar_camas_ocupadas(piso : list[bool]) -> int:
    contador : int = 0
    
    for cama in piso:
        if cama:
            contador += 1

    return contador


def nivel_de_ocupacion(camas_por_piso : list[list[bool]]) -> list[float]:
    res : list[float] = []

    for piso in camas_por_piso:
        res.append(contar_camas_ocupadas(piso)/len(piso))

    return res

print(nivel_de_ocupacion([[True, False, True], [False, False, True],
[True, True, True]]))

