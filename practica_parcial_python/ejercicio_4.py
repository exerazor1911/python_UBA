from queue import Queue

def reordenar_cola_priorizando_vips(fila_clientes: Queue[tuple[str,str]]) -> Queue[str]:
    fila_clientes_aux : Queue[tuple[str,str]] = Queue()

    fila_clientes_vip : Queue[str] = Queue()
    fila_clientes_comun : Queue[str] = Queue()

    res : Queue[str] = Queue()

    while not fila_clientes.empty():
        nombre: str 
        tipo_afiliado : str

        nombre, tipo_afiliado = fila_clientes.get()

        if tipo_afiliado == 'vip':
            fila_clientes_vip.put(nombre)
        else:
            fila_clientes_comun.put(nombre)

        fila_clientes_aux.put((nombre, tipo_afiliado))

    while not fila_clientes_vip.empty():
        res.put(fila_clientes_vip.get())

    while not fila_clientes_comun.empty():
        res.put(fila_clientes_comun.get())

    while not fila_clientes_aux.empty():
        fila_clientes.put(fila_clientes_aux.get())

    return res
    
cola = Queue()

cola.put(("Ana","comun"))
cola.put(("Juli","vip"))
cola.put(("Fede","vip"))

reordenados = reordenar_cola_priorizando_vips(cola)
print(cola.queue)
print(reordenados.queue)
