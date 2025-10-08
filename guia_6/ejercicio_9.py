def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0

def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

#1. ¿Cuál es el resultado de evaluar tres veces seguidas ro(1)?
#da 2,3,4
#2. ¿Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?
# Da 3 veces lo mismo: 2
#3. En cada función, realizar la ejecución simbólica.
#4. Dar la especificación para cada función, rt y ro

