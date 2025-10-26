def saldoActual(movimientos:list[(chr,int)]) -> int:
    acum : int = 0
    for (operacion,monto) in movimientos:
        if operacion == 'I':
            acum += monto
        else:
            acum -= monto
    return acum

#print(saldoActual([('I',2000),('R',20),('R',1000),('I',300)]))
