def clonar_sin_comentarios(nombre_archivo_entrada, nombre_archivo_salida : str):
    with open(nombre_archivo_entrada, 'r') as archivo_entrada:
        lineas : list[str] = archivo_entrada.readlines()
        lineas_sin_comentarios : list[str] = [linea for linea in lineas if linea[0] != '#']
        with open(nombre_archivo_salida, 'w') as archivo_salida:
            archivo_salida.writelines(lineas_sin_comentarios)

clonar_sin_comentarios('guia_8/clonar_sin_comentarios_entrada.txt','guia_8/clonar_sin_comentarios_salida.txt')