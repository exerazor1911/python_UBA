def agregar_frase_al_principio(nombre_archivo, frase : str):
    lineas : list[str]

    with open(nombre_archivo, 'r') as archivo:
        lineas  = archivo.readlines()

    lineas.reverse()
    lineas.append(frase + '\n')
    lineas.reverse()

    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(lineas)
        
agregar_frase_al_principio('guia_8/agregar_frase_al_principio.txt', 'anterior a primera frase 0')