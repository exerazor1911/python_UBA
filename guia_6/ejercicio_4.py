def peso_pino(metros_pino:float) -> float:
    peso_pino : float
    if metros_pino <= 3:
        peso_pino = 3 * metros_pino * 100
    else:
        peso_pino = 900 + 2 * (metros_pino-3) * 100 
    return peso_pino

#print(peso_pino(2))
#print(peso_pino(5))

def es_peso_util(peso:float) -> bool:
    return peso >= 400 and peso <= 1000

# print(es_peso_util(399))
# print(es_peso_util(1001))
# print(es_peso_util(1000))
# print(es_peso_util(400))

def sirve_pino(altura:float) -> bool:
    return es_peso_util(peso_pino(altura))

# print(sirve_pino(5))
# print(sirve_pino(4))
# print(sirve_pino(3))