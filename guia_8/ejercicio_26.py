def es_legible(caracter : str) -> bool:
    if caracter.isalnum() or caracter == ' ' or caracter == '_':
        return True
    return False

def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:
    palabra : list[str] = ""
    textos : list[str] = []

    with open(nombre_archivo, 'rb') as archivo:
        contenido : list[bytes] = archivo.read()
        for item in contenido:
            char : str = chr(item)
            if es_legible(char):
                palabra = palabra + char
            else:
                if len(palabra) >= 5:
                    textos.append(palabra)
                palabra = ""

    return textos
        
    
# ver de implementar con ASCII

print(listar_textos_de_archivo('guia_8/test_strings.bin'))