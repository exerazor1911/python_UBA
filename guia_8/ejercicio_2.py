from queue import LifoQueue 

def cantidad_elementos(p: LifoQueue[int]) -> int:
    elems : int = 0
    aux_lifo_queue : LifoQueue[int] = LifoQueue()

    while not p.empty():
        aux_lifo_queue.put(p.get())
        elems += 1

    while not aux_lifo_queue.empty():
        p.put(aux_lifo_queue.get())
    
    return elems

# pila = LifoQueue()
# pila.put(1)
# pila.put(1)
# pila.put(1)
# pila.put(13)
# print(cantidad_elementos(pila))
