#1
def es_matriz(s:list[list[int]]) -> bool:
    if len(s) < 1 or len(s[0]) < 1:
        return False
    longitud_fila : int = len(s[0])
    for i in range (1,len(s)):
        if len(s[i]) != longitud_fila:
            return False
    return True
    
# print(es_matriz([]))
# print(es_matriz([[]]))
# print(es_matriz([[1,2],[3,4,5]]))

#2
def ordenados(s:list[int]) -> bool:
    for i in range(1,len(s)):
        if s[i] <= s[i-1]:
            return False
    return True

def filas_ordenadas(m:list[list[int]],res:list[bool]):
    for fila in m:
        res.append(ordenados(fila))

# res = []
# filas_ordenadas([[1,2,3],[8,5,6]],res)
# print(res)

#3
def columna(m:list[list[int]], c:int) -> list[int]:
    secuencia : list[int] = []
    for fila in m:
        secuencia.append(fila[c])
    return secuencia

#print(columna([[1,2,3],[4,5,6]],2))

#4
def columnas_ordenadas(m:list[list[int]]) -> list[bool]:
    columnas_ord : list[bool] = []
    for i in range(len(m[0])):
        columnas_ord.append(ordenados(columna(m,i)))
    return columnas_ord

#print(columnas_ordenadas([[1,6,3],[4,5,6]]))

#5
def transponer(m:list[list[int]]) -> list[list[int]]:
    traspuesta : list[list[int]] = []
    for i in range(len(m[0])):
        traspuesta.append(columna(m,i))
    return traspuesta

#print(transponer([[1,2,3],[4,5,6],[7,8,9]]))

#6
#matriz 3x3

def revisar_filas(m:list[list[chr]],c:chr) -> bool:
    for fila in m:
        if fila[0] == c and fila[0] == fila[1] == fila[2]:
            return True
    return False

def revisar_diagonal(m:list[list[chr]],c:chr) -> bool:
    for i in range(len(m)):
        if m[i][i] != c and m[i][len(m)-1-i] != c:
            return False
    return True

def revisar(m:list[list[chr]],c:chr) -> bool:
    filas : bool = revisar_filas(m,c)
    columnas : bool = revisar_filas(transponer(m),c)
    diagonal : bool = revisar_diagonal(m,c)

    return filas or columnas or diagonal

def quien_gana_tateti(m:list[list[chr]]) -> int:
    if revisar(m,'O'):
        return 0
    elif revisar(m,'X'):
        return 1
    return 2

# print(quien_gana_tateti([['O','O','X'],['O','X','O'],['X','O','O']]))
# print(quien_gana_tateti([['O','X','X'],['X','O','X'],['X','X','O']]))

#queda implementar el ejercicio 7 OPCIONAL el fin de semana
