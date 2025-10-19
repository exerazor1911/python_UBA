def invertir_lineas(nombre_archivo_entrada, nombre_archivo_salida : str):
    with open(nombre_archivo_entrada, 'r') as archivo_entrada:
        lineas = archivo_entrada.readlines()
        lineas.reverse()

        if not lineas[0].endswith("\n"):
            lineas[0] = lineas[0] + "\n"

        with open(nombre_archivo_salida, 'w') as archivo_salida:
            archivo_salida.writelines(lineas)


invertir_lineas('guia_8/invertir_lineas_entrada.txt','guia_8/invertir_lineas_salida.txt')