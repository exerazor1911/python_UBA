#1 
import math

# Export specific functions
__all__ = ['es_multiplo_de']


def imprimir_saludo(nombre:str):
    print(nombre)
#2
def raiz_cuadrada_de(num:float) -> float:
    return math.sqrt(num)
#3
def fahrenheit_a_celsius(temp_far:float) -> float:
    return (temp_far-32) * 5/9
#4
def imprimir_dos_veces(estribillo:str):
    print(estribillo*2)
#5
def es_multiplo_de(n,m:int) -> bool:
    return n%m == 0
#6
def es_par(n:int) -> bool:
    return es_multiplo_de(n,2)
#7
def cantidad_de_pizzas(comensales,min_cant_de_porc:int) -> int:
    return math.ceil(comensales * min_cant_de_porc / 8)
