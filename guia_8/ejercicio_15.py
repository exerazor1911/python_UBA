from queue import Queue

def atencion_a_clientes(c: Queue[tuple[str,int,bool,bool]]) -> Queue[tuple[str,int,bool,bool]]:
    c_aux : Queue[tuple[str,int,bool,bool]] = Queue()
    res : Queue[tuple[str,int,bool,bool]] = Queue()

    cola_prioridad : Queue[tuple[str,int,bool,bool]] = Queue()
    cola_banca_preferencial : Queue[tuple[str,int,bool,bool]] = Queue()
    cola_resto : Queue[tuple[str,int,bool,bool]] = Queue()

    nombre: str
    dni : int
    tipo_cuenta : bool
    prioridad : bool

    while not c.empty():
        nombre, dni, tipo_cuenta, prioridad = c.get()

        if prioridad:
            cola_prioridad.put((nombre, dni, tipo_cuenta, prioridad))
        elif tipo_cuenta:
            cola_banca_preferencial.put((nombre, dni, tipo_cuenta, prioridad))
        else:
            cola_resto.put((nombre, dni, tipo_cuenta, prioridad))

        c_aux.put((nombre, dni, tipo_cuenta, prioridad))

    while not c_aux.empty():
        c.put(c_aux.get())

    while not cola_prioridad.empty():
        res.put(cola_prioridad.get())

    while not cola_banca_preferencial.empty():
        res.put(cola_banca_preferencial.get())

    while not cola_resto.empty():
        res.put(cola_resto.get())

    return res

clientes = Queue()
clientes.put(("a",3,False,False))
clientes.put(("b",4,True,False))
clientes.put(("c",5,False,True))
clientes.put(("d",6,False,False))
clientes.put(("e",7,True,False))
clientes.put(("f",8,False,False))
clientes.put(("g",9,False,True))
clientes.put(("h",0,False,False))

#rta: c,g,b,e,a,d,f,h
orden = atencion_a_clientes(clientes)
while not orden.empty():
    print(orden.get())


        
