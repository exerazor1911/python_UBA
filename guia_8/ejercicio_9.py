from queue import Queue

def cantidad_elementos(c : Queue) -> int:
    cola_aux : Queue = Queue()
    contador : int = 0

    while not c.empty():
        contador += 1
        cola_aux.put(c.get())

    while not cola_aux.empty():
        c.put(cola_aux.get())

    return contador

cola = Queue()
cola.put(1)
cola.put(2)
cola.put(3)

print(cantidad_elementos(cola))
