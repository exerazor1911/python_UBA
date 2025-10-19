from queue import Queue

def buscar_el_maximo(c: Queue[int]) -> int:
    maximo : int = c.get()
    c_aux : Queue[int] = Queue()
    c_aux.put(maximo)

    while not c.empty():
        item : int = c.get()

        if item > maximo:
            maximo = item

        c_aux.put(item)

    while not c_aux.empty():
        c.put(c_aux.get())

    return maximo

cola = Queue()
cola.put(1)
cola.put(40)
cola.put(10)


print(buscar_el_maximo(cola))