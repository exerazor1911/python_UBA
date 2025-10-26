from queue import Queue

def intercalar(c1, c2 : Queue) -> Queue:
    res : Queue = Queue()
    res_aux : Queue = Queue()

    while not c1.empty():
        elem_c1 = c1.get()
        elem_c2 = c2.get()

        res.put(elem_c1)
        res.put(elem_c2)

        res_aux.put(elem_c1)
        res_aux.put(elem_c2)

    while not res_aux.empty():
        c1.put(res_aux.get())
        c2.put(res_aux.get())

    return res


c1 = Queue()
c1.put(1)
c1.put(2)
c1.put(3)


c2 = Queue()
c2.put('A')
c2.put('B')
c2.put('C')


c3 = intercalar(c1,c2)
while not c3.empty():
    print(c3.get())

while not c2.empty():
    print("c1: ", c1.get())
    print("c2: ", c2.get())

