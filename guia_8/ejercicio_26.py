def es_legible(caracter : chr) -> bool:
    if caracter.isalnum() or caracter == ' ' or caracter == '_':
        return True
    return False

def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:
    palabra : list[chr] = ""
    textos : list[str] = []

    with open(nombre_archivo, 'rb') as archivo:
        contenido : list[bytes] = archivo.read()
        for item in contenido:
            char : chr = chr(item)
            if es_legible(char):
                palabra = palabra + char
            else:
                if len(palabra) >= 5:
                    textos.append(palabra)
                palabra = ""

    return textos
        
    
print(listar_textos_de_archivo('guia_8/test_strings.bin'))