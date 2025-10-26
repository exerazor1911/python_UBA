sumaTotal :: [[Int]] -> Int
sumaTotal [] = 0
sumaTotal (x : xs) = sumaInterna x + sumaTotal xs

sumaInterna :: [Int] -> Int
sumaInterna [] = 0
sumaInterna (x : xs) = x + sumaInterna xs

cantidadDeApariciones :: Int -> [[Int]] -> Int
cantidadDeApariciones _ [] = 0
cantidadDeApariciones num (slice : slices) = cantidadDeAparicionesInternas num slice + cantidadDeApariciones num slices

cantidadDeAparicionesInternas :: Int -> [Int] -> Int
cantidadDeAparicionesInternas _ [] = 0
cantidadDeAparicionesInternas num (elem : slice)
  | num == elem = 1 + cantidadDeAparicionesInternas num slice
  | otherwise = cantidadDeAparicionesInternas num slice

contarPalabras :: String -> [[String]] -> Int
contarPalabras _ [] = 0
contarPalabras palabra (palSlice : palSliceOfSlices) = contarPalabrasInternas palabra palSlice + contarPalabras palabra palSliceOfSlices

contarPalabrasInternas :: String -> [String] -> Int
contarPalabrasInternas _ [] = 0
contarPalabrasInternas palabra (pal : pals)
  | pal == palabra = 1 + contarPalabrasInternas palabra pals
  | otherwise = contarPalabrasInternas palabra pals

cantidadDeApariciones2 :: (Eq a) => a -> [[a]] -> Int
cantidadDeApariciones2 _ [] = 0
cantidadDeApariciones2 elem (elemSlice : elemSliceOfSlices) = cantidadDeAparicionesInternas2 elem elemSlice + cantidadDeApariciones2 elem elemSliceOfSlices

cantidadDeAparicionesInternas2 :: (Eq a) => a -> [a] -> Int
cantidadDeAparicionesInternas2 _ [] = 0
cantidadDeAparicionesInternas2 elem (unit : units)
  | elem == unit = 1 + cantidadDeAparicionesInternas2 elem units
  | otherwise = cantidadDeAparicionesInternas2 elem units

multiplicarPorEscalar :: Int -> [[Int]] -> [[Int]]
multiplicarPorEscalar _ [] = []
multiplicarPorEscalar escalar (fila : matriz) = multiplicarFilaPorEscalar escalar fila : multiplicarPorEscalar escalar matriz

multiplicarFilaPorEscalar :: Int -> [Int] -> [Int]
multiplicarFilaPorEscalar _ [] = []
multiplicarFilaPorEscalar escalar (elem : elems) = (escalar * elem) : multiplicarFilaPorEscalar escalar elems

concatenarFilas :: [[String]] -> [String]
concatenarFilas [] = []
concatenarFilas (slice : sliceOfSlices) = concatenarInterno slice ++ concatenarFilas sliceOfSlices

concatenarInterno :: [String] -> [String]
concatenarInterno [] = []
concatenarInterno (str : strSlice) = str : concatenarInterno strSlice

iesimaFila :: Integer -> [[a]] -> [a]
iesimaFila _ [] = []
iesimaFila num (slice : sliceOfSlices)
  | num == 0 = slice
  | otherwise = iesimaFila (num - 1) sliceOfSlices

iesimaColumna :: Integer -> [[a]] -> [a]
iesimaColumna _ [] = []
iesimaColumna num (slice : sliceOfSlices) = iesimoElemento num slice : iesimaColumna num sliceOfSlices

iesimoElemento :: Integer -> [a] -> a
iesimoElemento 0 (elem : slice) = elem
iesimoElemento num (elem : slice) = iesimoElemento (num - 1) slice

