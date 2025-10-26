def cambiar_fila(fila: list[int]):
    primer_elem : int = fila[0]
    for i in range(len(fila)):
        if i == len(fila) - 1:
            fila [i] = primer_elem
        else:
            fila[i] = fila[i+1]

def cambiar_matriz(a : list[list[int]]):
    for fila in a:
        cambiar_fila(fila)
    primera_fila : list[int] = a[0]

    for i in range (len(a)):
        if i == len(a)-1:
            a[i] = primera_fila
        else:
            a[i] = a[i+1]


a = [[1,2],[3,4],[5,6]]
b = [[1,2,3],[4,5,6]]
c = [[1,2]]
d = [[1],[2],[3]]
cambiar_matriz(a)
cambiar_matriz(b)
cambiar_matriz(c)
cambiar_matriz(d)
print(a)
print(b)
print(c)
print(d)

