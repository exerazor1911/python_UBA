type Fila = [Int]

type Tablero = [Fila]

type Posicion = (Int, Int)

type Camino = [Posicion]

--

maximo :: Tablero -> Int
maximo [] = 0
maximo (fila : filas)
  | elementoMax fila > maximo filas = elementoMax fila
  | otherwise = maximo filas

-- HELPER
elementoMax :: Fila -> Int
elementoMax [elem] = elem
elementoMax (elemA : elemB : elems)
  | elemA > elemB = elementoMax (elemA : elems)
  | otherwise = elementoMax (elemB : elems)

--
masRepetido :: Tablero -> Int
masRepetido tablero = numeroMasRepetido 0 0 (unificarFilas tablero)

-- HELPER
unificarFilas :: Tablero -> Fila
unificarFilas [] = []
unificarFilas (fila : filas) = fila ++ unificarFilas filas

numeroMasRepetido :: Int -> Int -> Fila -> Int
numeroMasRepetido masRepetido _ [] = masRepetido
numeroMasRepetido masRepetido apariciones (elem : filas)
  | contarApariciones elem (elem : filas) > apariciones = numeroMasRepetido elem (contarApariciones elem (elem : filas)) filas
  | otherwise = numeroMasRepetido masRepetido apariciones filas

contarApariciones :: Int -> Fila -> Int
contarApariciones _ [] = 0
contarApariciones num (elem : filas)
  | num == elem = 1 + contarApariciones num filas
  | otherwise = contarApariciones num filas

--

valoresDeCamino :: Tablero -> Camino -> Fila
valoresDeCamino _ [] = []
valoresDeCamino tablero (posicion : posiciones) = obtenerValorDePosicionDelTablero posicion tablero : valoresDeCamino tablero posiciones

-- HELPER
obtenerValorDePosicionDelTablero :: Posicion -> Tablero -> Int
obtenerValorDePosicionDelTablero (x, y) tablero = obtenerValorPosicion y 1 (obtenerFila x 1 tablero)

obtenerFila :: Int -> Int -> Tablero -> Fila
obtenerFila nroFila repeticiones (fila : filas)
  | nroFila == repeticiones = fila
  | otherwise = obtenerFila nroFila (repeticiones + 1) filas

obtenerValorPosicion :: Int -> Int -> Fila -> Int
obtenerValorPosicion nroPosicion repeticiones (elem : elems)
  | nroPosicion == repeticiones = elem
  | otherwise = obtenerValorPosicion nroPosicion (repeticiones + 1) elems

-- NOTA: el primer arrar de ints es = posiciones que forman un camino
esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo (x : xs) num = x == num && esFibo (x : xs) num

esFibo :: [Int] -> Int -> Bool
esFibo [] _ = True
esFibo (x:xs) num = fibonacci num == x && esFibo xs (num+1)

fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)