from queue import LifoQueue

def buscar_nota_maximo(p: LifoQueue[(str,int)]) -> tuple[str,int]:
    nota_max : tuple[str,int] = p.get()
    aux_p : LifoQueue[(str,int)] = LifoQueue()
    aux_p.put(nota_max)

    while not p.empty():
        materia : str
        nota : int
        materia,nota = p.get()
        if nota > nota_max[1]:
            nota_max = (materia,nota)
        aux_p.put((materia,nota))

    while not aux_p.empty():
        p.put(aux_p.get())
    
    return nota_max

pila = LifoQueue()
pila.put(("mate", 10))
pila.put(("leng", 9))
pila.put(("geo", 4))
pila.put(("alg", 8))
pila.put(("music", 11))
print(buscar_nota_maximo(pila))