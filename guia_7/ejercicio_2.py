#1
def CerosEnPosicionesPares(s:list[int]):
    for i in range(1,len(s),2):
        s[i] = 0

# s = [1,2,3,4,5]
# CerosEnPosicionesPares(s)
# print(s)

#2
def CerosEnPosicionesPares2(s:list[int]) -> list[int]:
    res = s.copy()
    for i in range(1,len(res),2):
        res[i] = 0
    return res

# s = [1,2,3,4,5]
# res = CerosEnPosicionesPares2(s)
# print(res)
# print(s)

#3
def sin_vocales(s:list[chr]) -> list[chr]:
    sin_vocales : list[chr] = []
    for letra in s:
        if letra not in ['a','e','i','o','u']:
            sin_vocales.append(letra)
    return sin_vocales

# s = ['a','b','c','d','e']
# sin_vocales = sin_vocales(s)
# print(s)
# print(sin_vocales)

#4
def reemplaza_vocales(s:list[chr]) -> list[chr]:
    vocales_reemplazadas : list[chr] = []
    for letra in s:
        if letra not in ['a','e','i','o','u']:
            vocales_reemplazadas.append(letra)
        else:
            vocales_reemplazadas.append('-')
    return vocales_reemplazadas

# s = ['a','b','c','d','e']
# vocales_reemplazadas = reemplaza_vocales(s)
# print(s)
# print(vocales_reemplazadas)

#5
def da_vuelta_str(s:list[chr]) -> list[chr]:
    lista_copia: list[chr] = s.copy()
    lista_copia.reverse()
    return lista_copia

# s = ['a','b','c','d','e']
# dada_vuelta = da_vuelta_str(s)
# print(s)
# print(dada_vuelta)

#6
def pertenece(c : chr, s : list[chr]) -> bool:
    for char in s:
        if char == c:
            return True
    return False

def eliminar_repetidos(s:list[chr]) -> list[chr]:
    sin_repetidos : list[chr] = []
    for i in range(len(s)):
        if not pertenece(s[i],s[i+1::]):
            sin_repetidos.append(s[i])
    return sin_repetidos

# s = ['a','b','c','d','a','a']
# sin_repetidos = eliminar_repetidos(s)
# print(s)
# print(sin_repetidos)
