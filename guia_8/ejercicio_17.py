from queue import LifoQueue

def visitar_sitio(historiales : dict[str,LifoQueue[str]], usuario, sitio : str):
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        historial : LifoQueue[str] = LifoQueue()
        historial.put(sitio)
        historiales[usuario] = historial

def navegar_atras(historiales : dict[str,LifoQueue[str]], usuario : str) -> str:
    return historiales[usuario].get()


historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")

for nombre, historial in historiales.items():
    print("nombre ", nombre)
    while not historial.empty():
        print(historial.get())