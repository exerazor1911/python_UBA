matrizIdentidad :: Integer -> [[Integer]]
matrizIdentidad 0 = []
matrizIdentidad dim = generarMatrizIdentidad dim dim

generarMatrizIdentidad :: Integer -> Integer -> [[Integer]]
generarMatrizIdentidad 0 _ = []
generarMatrizIdentidad fil col = generarIdentidadPorColumna fil col : generarMatrizIdentidad (fil - 1) col

generarIdentidadPorColumna :: Integer -> Integer -> [Integer]
generarIdentidadPorColumna _ 0 = []
generarIdentidadPorColumna fil col
  | fil == col = 1 : generarIdentidadPorColumna fil (col - 1)
  | otherwise = 0 : generarIdentidadPorColumna fil (col - 1)