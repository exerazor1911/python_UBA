from queue import Queue

#preguntar si la definicion del problema esta ok
def buscar_nota_minima(c: Queue[(list[str],int)]) -> tuple[list[str],int]:
    nombre_materia_minima : list[str] 
    nota_minima : int

    nombre_materia_minima, nota_minima = c.get()
    c_aux : Queue[(list[str],int)] = Queue()
    c_aux.put((nombre_materia_minima,nota_minima))

    while not c.empty():
        nombre_materia : list[str]
        nota : int

        nombre_materia, nota = c.get()

        if nota < nota_minima:
            nombre_materia_minima = nombre_materia
            nota_minima = nota

        c_aux.put((nombre_materia,nota))
        
    while not c_aux.empty():
        c.put(c_aux.get())

    return nombre_materia_minima, nota_minima


cola = Queue()
cola.put(("mate",10))
cola.put(("leng",3))
cola.put(("geo",8))


nota_minima = buscar_nota_minima(cola)
print(type(nota_minima))
print(nota_minima)
