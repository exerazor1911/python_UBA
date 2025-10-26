def fabs ( x : int ) -> int :
 if x < 0:
    return -x
 else :
    return x

def multByAbs ( x : int , y : int ) -> int :
    abs_y : int = fabs ( y ); # ejercicio anterior
    if abs_y < 0:
        return -1
    else :
        result : int = 0
        i : int = 0
        while i < abs_y :
            result = result + x 
            i += 1
    return result

print(multByAbs(10,-2))