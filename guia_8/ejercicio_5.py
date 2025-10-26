from queue import LifoQueue

def esta_bien_balanceada(s: list[str]) -> bool:
    elem_lifo_queue : LifoQueue[str] = LifoQueue()
    for elem in s:
        if elem == '(':
            elem_lifo_queue.put(elem)
        elif elem == ')':
            if elem_lifo_queue.empty() : return False
            elem_lifo_queue.get()

    return elem_lifo_queue.empty()

print(esta_bien_balanceada("1 + ( 2 x 3 = ( 2 0 / 5 ) )"))
print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( =1)))"))
print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))

