from queue import Queue

#(urgencia, nombre, especialidad_medica)
def pacientes_urgentes(c : Queue[(int,list[chr],list[chr])]) -> int:
    c_aux : Queue[(int,list[chr],list[chr])] = Queue()
    contador : int = 0

    while not c.empty():
        prioridad : int
        nombre : list[chr]
        esp_medica : list[chr]

        prioridad, nombre, esp_medica = c.get()

        if prioridad < 4:
            contador += 1

        c_aux.put((prioridad,nombre,esp_medica))

    while not c_aux.empty():
        c.put(c_aux.get())


    return contador

pacientes = Queue()
pacientes.put((1,"juan","urologia"))
pacientes.put((4,"silvana","cardiologia"))
pacientes.put((3,"matias","medicina general"))


print(pacientes_urgentes(pacientes))