def es_legible(linea : str) -> bool:
    if len(linea) < 5: return False

    for byte in linea:
        caracter = chr(byte)
        if not caracter.isalnum() or not caracter == ' ' or not caracter == '_':
            return False
    
    return True

def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:
    cadena : bytes
    with open(nombre_archivo, 'rb') as archivo:
        cadena = archivo.read()
    
    for item in cadena:
        caracter : chr = chr(item)


#TODO: terminar, no se entiende muy bien que es lo que se quiere

print(listar_textos_de_archivo('guia_8/listar_textos_de_archivo.mp3'))

