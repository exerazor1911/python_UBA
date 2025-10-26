sumaImpares :: Int -> Int
sumaImpares n = sumaImparesDesde 1 n

sumaImparesDesde :: Int -> Int -> Int
sumaImparesDesde _ 0 = 0
sumaImparesDesde n contador
  | esImpar n = n + sumaImparesDesde (n + 1) (contador - 1)
  | otherwise = sumaImparesDesde (n + 1) contador

esImpar :: Int -> Bool
esImpar n = mod n 2 /= 0