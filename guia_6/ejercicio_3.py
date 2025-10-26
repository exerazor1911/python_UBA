#1
def alguno_es_0(num1 ,num2 : float) -> bool:
    return num1 == 0 or num2 == 0

#print(alguno_es_0(2,3))
#print(alguno_es_0(0,3))
#print(alguno_es_0(0.0,3))

#2
def ambos_son_0(num1 ,num2 : float) -> bool:
    return num1 == 0 and num2 == 0

# print(ambos_son_0(2,3))
# print(ambos_son_0(0,3))
# print(ambos_son_0(0.0,3))
# print(ambos_son_0(0.0,0))

#3
def es_nombre_largo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

# print(es_nombre_largo("ernesto1"))
# print(es_nombre_largo("ern"))
# print(es_nombre_largo("er"))
# print(es_nombre_largo("ernesto12"))
