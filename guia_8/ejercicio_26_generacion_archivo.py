import os

def crear_archivo_binario_de_prueba(nombre_archivo="guia_8/test_strings.bin"):
    """
    Crea un archivo binario de prueba con strings legibles
    incrustados entre bytes no legibles (caracteres de control, etc.).
    """
    # Textos que cumplen la regla:
    # 1. Solo caracteres legibles (letras, números, _, espacio)
    # 2. Longitud >= 5
    textos_legibles = [
        "ESTE ES EL PRIMER TEXTO LEGIBLE con mas de 5 caracteres.", # Debe aparecer
        "Texto_2_Legible_y_Mas_Largo",                             # Debe aparecer
        "shor",                                                    # NO debe aparecer (Longitud < 5)
        "1234567890",                                              # Debe aparecer
        "Solo",                                                    # NO debe aparecer (Longitud < 5)
        "Final_Test_String_OK"                                     # Debe aparecer
    ]
    
    # Bytes que NO son legibles (ej: bytes de control, datos binarios típicos)
    datos_basura_1 = b'\x00\x01\x02\x03\x04\x05\x00\xff\xfe\xfd\xaa\xbb' # Caracteres de control/binarios
    datos_basura_2 = b'\x90\x80\x1A\x1B\x1C\x1D\x00\x00\x00\x00'
    
    # Abrir en modo de escritura binaria ('wb')
    with open(nombre_archivo, 'wb') as f:
        
        # 1. Escribir Basura
        f.write(datos_basura_1)
        
        # 2. Escribir el Primer Texto Legible
        # El método .encode('ascii') lo convierte a bytes
        f.write(textos_legibles[0].encode('ascii'))
        
        # 3. Escribir más Basura
        f.write(b'\x00\x00\x00\x00\x00') # 5 bytes nulos para romper la secuencia
        f.write(textos_legibles[1].encode('ascii'))
        
        # 4. Escribir texto demasiado corto (debe ser ignorado)
        f.write(b'\x00\x00')
        f.write(textos_legibles[2].encode('ascii')) # "short" (largo 5, OK)
        f.write(b'\x00\x00') # Lo rompemos
        
        # 5. Escribir el texto numérico
        f.write(textos_legibles[3].encode('ascii'))
        f.write(datos_basura_2)
        
        # 6. Escribir el texto corto y romperlo
        f.write(textos_legibles[4].encode('ascii')) # "Solo 4" (largo 6, OK)
        f.write(b'\x00\x00')
        
        # 7. Escribir el último texto
        f.write(textos_legibles[5].encode('ascii'))
        
        # 8. Un poco más de basura al final
        f.write(b'\x00\xAA\xBB\xCC')
        
    print(f"Archivo binario de prueba '{nombre_archivo}' creado con éxito.")

if __name__ == "__main__":
    crear_archivo_binario_de_prueba()