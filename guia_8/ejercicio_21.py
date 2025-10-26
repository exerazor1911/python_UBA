def la_palabra_mas_frecuente(nombre_archivo : str) -> str:
    palabras_ocurrencias : dict[str,int] = dict()

    with open(nombre_archivo, 'r') as archivo:
        lineas : list[str] = archivo.readlines()

        for linea in lineas:
            palabras : list[str] = linea.split(" ")

            for palabra in palabras:
                palabra = palabra.strip()
                if palabra in palabras_ocurrencias:
                    palabras_ocurrencias[palabra] += 1
                else:
                    palabras_ocurrencias[palabra] = 1
            
    ocurrencias_maximas : int = 0
    palabra_maxima : str

    for palabra, ocurrencias in palabras_ocurrencias.items():
        if ocurrencias > ocurrencias_maximas:
            ocurrencias_maximas = ocurrencias
            palabra_maxima = palabra
    
    return palabra_maxima

print("mas frecuente: ",la_palabra_mas_frecuente('guia_8/la_palabra_mas_frecuente.txt'))