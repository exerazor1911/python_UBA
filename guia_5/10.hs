cantidadParesColumna :: Integer -> [[Integer]] -> Integer
cantidadParesColumna _ [] = 0
cantidadParesColumna pos (slice:sliceOfSlices) | esElementoPar pos slice = 1 + cantidadParesColumna pos sliceOfSlices
                                               | otherwise = cantidadParesColumna pos sliceOfSlices

esElementoPar :: Integer -> [Integer] -> Bool
esElementoPar pos (elem:slice) | pos == 0 = mod elem 2 == 0
                               | otherwise = esElementoPar (pos-1) slice
