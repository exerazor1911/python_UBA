from queue import Queue 
import random

def armar_secuencia_de_bingo() -> Queue[int]:
    lista_numeros : list[int] = []
    cola : Queue[int] = Queue()

    for i in range(100):
        lista_numeros.append(i)
    random.shuffle(lista_numeros)

    for num in lista_numeros:
        cola.put(num)

    return cola

# cola = armar_secuencia_de_bingo()
# while not cola.empty():
#     print(cola.get())

def jugar_carton_de_bingo(carton : list[int], bolillero : Queue[int]) -> int:
    contador : int = len(carton)
    jugadas : int = 0
    bolillero_aux : Queue[int] = Queue()

    while contador > 0:
        bolilla : int = bolillero.get()

        if bolilla in carton:
            contador -= 1

        jugadas += 1
        bolillero_aux.put(bolilla)

    return jugadas

bolillero = armar_secuencia_de_bingo()
carton = [0,1,2,3,4,5,6,7,8,9,10,11]

print(jugar_carton_de_bingo(carton,bolillero))


    




