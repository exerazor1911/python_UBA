from queue import LifoQueue

def buscar_el_maximo(p: LifoQueue[int]) -> int:
    maximo : int = p.get()
    lifo_aux : LifoQueue[int] = LifoQueue()
    lifo_aux.put(maximo)

    while not p.empty():
        num : int = p.get()
        if num > maximo:
            maximo = num
        lifo_aux.put(num)

    while not lifo_aux.empty():
        p.put(lifo_aux.get())
    
    return maximo

# pila = LifoQueue()
# pila.put(100)
# pila.put(121)
# pila.put(0)
# print(buscar_el_maximo(pila))
# while not pila.empty():
#     print(pila.get())