from queue import Queue
import random

def generar_nros_al_azar(cantidad, desde, hasta : int) -> Queue[int]:
    res : Queue[int] = Queue()

    for _ in range(cantidad):
        num : int = random.randint(desde,hasta)
        res.put(num)

    return res

cola = generar_nros_al_azar(3,1,10)
while not cola.empty():
    print(cola.get())