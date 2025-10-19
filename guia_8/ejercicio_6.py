from queue import LifoQueue

def evaluar_expresion(s : list[chr]) -> float:
    operations : dict[chr,function] = {
        '+' : lambda x, y : x + y,
        '-' : lambda x, y : x - y,
        '*' : lambda x, y : x * y,
        '/' : lambda x, y : x / y,
    }


    pila_aux : LifoQueue[str] = LifoQueue()

    for elem in s:
        if elem == ' ': continue
        if elem in operations.keys():
            num_1 : float = float(pila_aux.get())
            num_2 : float = float(pila_aux.get())
            pila_aux.put(str(operations[elem](num_2,num_1)))
        else:
            pila_aux.put(elem)

    return float(pila_aux.get())


#print(evaluar_expresion("3 4 + 5 * 2 -"))
print(evaluar_expresion("5 3 + 4 * 4 - 4 /"))

            