from queue import LifoQueue

def intercalar(p1, p2 : LifoQueue) -> LifoQueue:
    pila_general_aux_1 : LifoQueue = LifoQueue()
    res : LifoQueue = LifoQueue()

    while not p1.empty():
        pila_general_aux_1.put(p2.get())
        pila_general_aux_1.put(p1.get())

    while not pila_general_aux_1.empty():
        p1_item = pila_general_aux_1.get()
        p2_item = pila_general_aux_1.get()

        p1.put(p1_item)
        p2.put(p2_item)

        res.put(p1_item)
        res.put(p2_item)

    return res

pila_1 = LifoQueue()
pila_2 = LifoQueue()

pila_1.put('A')
pila_1.put('B')
pila_1.put('C')

pila_2.put(4)
pila_2.put(5)
pila_2.put(6)

pila_res = intercalar(pila_1, pila_2)
while not pila_res.empty():
    print(pila_res.get())