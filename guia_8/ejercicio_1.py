from queue import LifoQueue as Pila
from random import randint

def generar_nros_al_azar(cantidad, desde, hasta :int) -> Pila[int]:
    pila : Pila[int] = Pila() 

    for _ in range(cantidad):
        pila.put(randint(desde,hasta))

    return pila

# pila = generar_nros_al_azar(10,1,10)
# while not pila.empty():
#     print(pila.get())


def buscar_el_maximo(p: Pila[int]) -> int:
    maximo: int = p.get()
    pila : Pila[int] = Pila()
    pila.put(maximo)
    while not p.empty():
        elem = p.get()
        pila.put(elem)
        if elem > maximo:
            maximo = elem

    while not pila.empty():
        p.put(pila.get())

    return maximo

p = Pila()
p.put(1000)
p.put(30)
p.put(100)
print("maximo: ", buscar_el_maximo(p))
while not p.empty():
    print(p.get())

#recordar meter los elementos a la pila de nuevo

