import numpy as np

def multiplicar_matriz(m:np.ndarray) -> np.ndarray:
    multiplied_array = np.zeros_like(m)
    for i in range (len(m)):
        for j in range (len(m)):
            multiplied_array[i,j] = np.dot(m[i],m[:, j])
    return multiplied_array


def exponenciacion_matriz(d,p:int) -> np.ndarray:
    m = np.random.randint(0,10,(d,d))

    for i in range(1,p):
       m = multiplicar_matriz(m)

    return m


print(exponenciacion_matriz(3,2))
