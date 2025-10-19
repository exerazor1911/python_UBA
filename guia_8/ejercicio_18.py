def agregar_producto(inventario : dict[str,dict[str,int|float]], nombre : str, precio: float, cantidad : int):
    precio_cantidad : dict[str,int|float] = {} 
    
    precio_cantidad["precio"] = precio
    precio_cantidad["cantidad"] = cantidad

    inventario[nombre] = precio_cantidad

def actualizar_stock(inventario : dict[str,dict[str,int|float]], nombre : str, cantidad : int):
    inventario[nombre]["cantidad"] = cantidad

def actualizar_precio(inventario : dict[str,dict[str,int|float]], nombre : str, precio : float):
    inventario[nombre]["precio"] = precio

def calcular_valor_inventario(inventario : dict[str,dict[str,int|float]]) -> float:
    acum : float = 0

    for item in inventario.values():
        acum += item["precio"] * item["cantidad"]

    return acum

inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantal´on", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Deber´ıa imprimir 1100.0
