#1
def pertenece(fila:list[int], e:int) -> bool:
    for elem in fila:
        if elem == e:
            return True
    return False
    
def pertenece_a_cada_uno_version_1(s:list[list[int]],e:int,res:list[bool]):
    for fila in s:
        res.append(pertenece(fila,e))

# res = []
# pertenece_a_cada_uno_version_1([[1,2,3],[4,5,6]],5,res)
# print(res)
#TODO: Preguntar en que caso la longitud de res seria mas grande, no entendi eso

#2
def pertenece_a_cada_uno_version_2(s:list[list[int]],e:int,res:list[bool]):
    for fila in s:
        res.append(pertenece(fila,e))

#3
def pertenece_a_cada_uno_version_3(s:list[list[int]],e:int) -> list[bool]:
    res : list[bool] = []
    for fila in s:
        res.append(pertenece(fila,e))
    return res

#yo creo que se puede tranquilamente usar la especificacion del 1 en el 2 y viceversa, ya que no tendria sentido tener una longiutd de res mas grande que la longitud de s

