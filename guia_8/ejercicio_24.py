def agregar_frase_al_final(nombre_archivo, frase : str):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write("\n" + frase)

agregar_frase_al_final('guia_8/agregar_frase_al_final.txt',"frase final")