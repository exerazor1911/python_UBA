#1
def pertenece1(s:list[int],e:int) -> bool:
    return e in s
def pertenece2(s:list[int],e:int) -> bool:
    for elem in s:
        if elem == e:
            return True
    return False
def pertenece3(s:list[int],e:int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False
#2
def divide_a_todos(s:list[int],e:int) -> bool:
    for elem in s:
        if elem % e != 0:
            return False
    return True
#3
def suma_total(s:list[int]) -> int:
    acum : int = 0
    for elem in s:
        acum += elem
    return acum
#4
def maximo(s:list[int]) -> int:
    maximo = s[0]
    for elem in s[1:]:
        if elem > maximo:
            maximo = elem
    return maximo
#5
def minimo(s:list[int]) -> int:
    minimo = s[0]
    for elem in s[1:]:
        if elem < minimo:
            minimo = elem
    return minimo
#6
def ordenados(s:list[int]) -> bool:
    for i in range(1,len(s)):
        if s[i] <= s[i-1]:
            return False
    return True
#7
def pos_maximo(s:list[int]) -> int:
    if len(s) <= 0:
        return -1
    maximo: int = s[0]
    res: int = 0
    for i in range(1,len(s)):
        if s[i] > maximo:
            maximo = s[i]
            res = i
    return res
#8
def pos_minimo(s:list[int]) -> int:
    if len(s) <= 0:
        return -1
    res : int = 0
    minimo: int = s[0]
    for i in range(1,len(s)):
        if s[i] < minimo:
            minimo = s[i]
            res = i
    return res
#9
def long_mayorASiete(s:list[str]) -> bool:
    for palabra in s:
        if len(palabra) > 7:
            return True
    return False
#10
def es_palindroma(s:list[chr]) -> bool:
    reversed = s.copy()
    reversed.reverse()
    return s == reversed
#11
def iguales_consecutivos(s:list[int]) -> bool:
    if len(s) < 3:
        return False
    for i in range (2,len(s)):
        if s[i] == s[i-1] == s[i-2]:
            return True
    return False
#12
def vocales_distintas(s:list[chr]) -> bool:
    vocales : list[chr] = []
    for letra in s:
        if es_vocal(letra) and letra not in vocales:
            vocales.append(letra)
    return len(vocales) >= 3
#helper
def es_vocal(c:chr) -> bool:
    return c in ['a','e','i','o','u']
#13
def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int: 
    if len(s) <= 1:
        return 0

    longitud_maxima = 1   
    inicio_maximo = 0            

    longitud_actual = 1          
    inicio_actual = 0           

    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            longitud_actual += 1
        else:
            longitud_actual = 1
            inicio_actual = i  

        if longitud_actual > longitud_maxima:
            longitud_maxima = longitud_actual
            inicio_maximo = inicio_actual

    return inicio_maximo
#14
def dame_digitos(num:int) -> list[int]:
    if num == 0:
        return []
    else:
        return dame_digitos(num // 10) + [num % 10]
    
def contar_digitos_imp(num:int) -> int:
    contador_digitos_impares : int = 0
    for digito in dame_digitos(num):
        if digito % 2 != 0:
            contador_digitos_impares += 1
    return contador_digitos_impares

def cantidad_digitos_impares(s:list[int]) -> int:
    cantidad_impares :int = 0
    for num in s:
        cantidad_impares += contar_digitos_imp(num)
    return cantidad_impares