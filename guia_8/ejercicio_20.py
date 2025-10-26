def agrupar_por_longitud(nombre_archivo : str) -> dict[int,int]:
    diccionario_longitud_cantidad : dict[int,int] = {}

    with open(nombre_archivo, 'r') as archivo:
        lineas : list[str] = archivo.readlines()
        for linea in lineas:
            palabras_linea : list[str] = linea.split(' ')
            for palabra_linea in palabras_linea:
                palabra_linea = palabra_linea.strip()
                if len(palabra_linea) in diccionario_longitud_cantidad:
                    diccionario_longitud_cantidad[len(palabra_linea)] += 1
                else:
                    diccionario_longitud_cantidad[len(palabra_linea)] = 1

    return diccionario_longitud_cantidad


print(agrupar_por_longitud("guia_8/agrupar_por_longitud.txt"))