#1
import random


def estudiantes() -> list[str]:
    estudiantes : list[str] = []
    opcion : str = input("Ingrese los nombres de los estudiantes / seleccionar 'listo' o dar ENTER para terminar: ")
    while opcion != '' and opcion != 'listo':
        estudiantes.append(opcion)
        opcion = input("Ingrese los nombres de los estudiantes / seleccionar 'listo' o dar ENTER para terminar: ")
    return estudiantes

#print(estudiantes())

#2
def historial_monedero() -> list[chr,float]:
    historial : list[chr,float] = []
    opcion : str = input("Ingrese 'C' para cargar creditos, 'D' para descontar creditos y 'X' para finalizar: ")
    while opcion != 'X':
        monto : int = int(input("Ingrese el monto: "))
        historial.append((opcion,monto))
        opcion = input("Ingrese 'C' para cargar creditos, 'D' para descontar creditos y 'X' para finalizar: ")
    return historial

#print(historial_monedero())

#3
def siete_y_medio() -> list[int]:
    print("Inicio del juego")
    numero_generado : int = random.randint(1,12)
    acum : int = 0
    cartas : list[int] = []

    while numero_generado >= 8 and numero_generado <= 9:
        numero_generado = random.randint(1,12)

    if numero_generado > 10:
        acum += 0.5
    else:
        acum += numero_generado
    cartas.append(numero_generado)

    eleccion : str = input("Desea seguir sacando otra carta? S/N: ")
    while eleccion != 'N':
        numero_generado : int = random.randint(1,12)
        while numero_generado >= 8 and numero_generado <= 9:
            numero_generado = random.randint(1,12)
        if numero_generado > 10:
            acum += 0.5
        else:
            acum += numero_generado
        cartas.append(numero_generado)

        if acum > 7.5:
            print("Ha perdido, supero 7.5")
            return cartas

        eleccion : str = input("Desea seguir sacando otra carta? S/N: ")
    
    print("Has ganado")
    return cartas

#print(siete_y_medio())

#4
contrasenia: str = input("Ingrese su contrasenia: ")

def cumple_verde(contra:str) -> bool:
    tiene_minus : bool = False
    tiene_mayus : bool = False
    tiene_numerico : bool = False

    if len(contra) < 8:
        return False
    
    for caracter in contra:
        if caracter <= 'z' and caracter >= 'a':
            tiene_minus = True
        elif caracter <= 'Z' and caracter >= 'A':
            tiene_mayus = True
        elif caracter.isdigit():
            tiene_numerico = True
    
    return tiene_minus and tiene_mayus and tiene_numerico

    

def analizar_contrasenia(contra:str) -> str:
    if len(contra) < 5:
        return "ROJA"
    if cumple_verde(contra):
        return "VERDE"
    return "AMARILLA"

print(analizar_contrasenia(contrasenia))
