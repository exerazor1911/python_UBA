def contar_lineas (nombre_archivo : str) -> int:
    with open(nombre_archivo, 'r') as archivo:
        lineas: list[str] = archivo.readlines()
        return len(lineas)
    
#print(contar_lineas("guia_8/contar_lineas.txt"))

def existe_palabra(nombre_archivo, palabra : str) -> bool:
    with open (nombre_archivo, 'r') as archivo:
        lineas : list[str] = archivo.readlines()
        for linea in lineas:
            linea = linea.strip()
            if palabra in linea:
                return True
    return False

#print(existe_palabra("guia_8/existe_palabra.txt", "palabra"))

def cantidad_de_apariciones(nombre_archivo, palabra : str) -> int:
    with open (nombre_archivo, 'r') as archivo:
        contenido : str = archivo.read()
        contenido = contenido.replace('\n',' ')
        return contenido.count(palabra)

print(cantidad_de_apariciones("guia_8/cantidad_de_apariciones_palabra.txt", "palabra"))