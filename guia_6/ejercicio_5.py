from ejercicio_2 import es_multiplo_de

#1
def es_par(num:int) -> bool:
    return num % 2 == 0

def devolver_el_doble_si_es_par(num:int) -> int:
    if es_par(num):
        num *= 2
    return num

# print(devolver_el_doble_si_es_par(2))
# print(devolver_el_doble_si_es_par(3))

def devolver_valor_si_es_par_sino_el_que_sigue(num:int) -> int:
    if not es_par(num):
        num +=1
    return num

# print(devolver_valor_si_es_par_sino_el_que_sigue(2))
# print(devolver_valor_si_es_par_sino_el_que_sigue(3))

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(num:int) -> int:
    if es_multiplo_de(num,9):
        num *=3
    elif es_multiplo_de(num,3):
        num*=2
    
    return num

# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(12))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(4))

def lindo_nombre(nom:str) -> str:
    res : str
    if len(nom) >= 5:
        res = "Tu nombre tiene muchas letras!"
    else:
        res = "Tu nombre tiene menos de 5 caracteres"
    return res

# print(lindo_nombre("eze"))
# print(lindo_nombre("ezequiel"))

def elRango(num:int):
    if num < 5:
        print("Menor a 5")
    elif num >= 10 and num <= 20:
        print("Entre 10 y 20")
    elif num > 20:
        print("Mayor a 20")  

# elRango(4)
# elRango(11)
# elRango(21)

def vacaciones_o_laburo(sexo:chr,edad:int):
    if sexo == 'F':
        if edad >= 60:
            print("Anda de vacaciones")
        else:
            print("Te toca trabajar")
    elif sexo == 'M':
        if edad >= 65:
            print("Anda de vacaciones")
        else:
            print("Te toca trabajar")

# vacaciones_o_laburo("M",65)
# vacaciones_o_laburo("M",64)
# vacaciones_o_laburo("F",60)
# vacaciones_o_laburo("F",59)
