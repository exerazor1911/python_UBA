#notas tiene al menos un elemento
#notas va de 0 a 10
#res = 1 si todas las notas son >= 4 y el promedio es >= 7
#res = 2 si notas >= 4 y promedio >=4 y < 7
#res = 3 si alguna nota es < 4 o el promedio < 4

def hayNotaDesaprobada(notas:list[int]) -> bool:
    for nota in notas:
        if nota < 4: 
            return True
    return False

def calcularPromedio(notas:list[int]) -> float:
    acum : float = 0
    for nota in notas:
        acum += nota
    return acum / len(notas)

def resultadoMateria(notas:list[int]) -> int:
    promedio : float = calcularPromedio(notas)
    if hayNotaDesaprobada(notas) or promedio < 4:
        return 3
    if promedio >= 7:
        return 1
    else:
        return 2