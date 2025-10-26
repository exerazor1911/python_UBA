divisoresPropios :: Int -> [Int]
divisoresPropios n = divisoresPropiosDesde 1 n

-- HELPER
divisoresPropiosDesde :: Int -> Int -> [Int]
divisoresPropiosDesde _ 0 = [1]
divisoresPropiosDesde desde num
  | desde == num = []
  | mod num desde == 0 = desde : divisoresPropiosDesde (desde + 1) num
  | otherwise = divisoresPropiosDesde (desde + 1) num

--

sonAmigos :: Int -> Int -> Bool
sonAmigos n m = sumatoriaDivisoresPropios n == m && sumatoriaDivisoresPropios m == n

-- HELPER
sumatoriaDivisoresPropios :: Int -> Int
sumatoriaDivisoresPropios n = sumarDivisores (divisoresPropios n)

sumarDivisores :: [Int] -> Int
sumarDivisores [] = 0
sumarDivisores (x : xs) = x + sumarDivisores xs

--

losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos n = primerosNPerfectosDesde 1 n

-- HELPER
primerosNPerfectosDesde :: Int -> Int -> [Int]
primerosNPerfectosDesde _ 0 = []
primerosNPerfectosDesde desde contador
  | sumatoriaDivisoresPropios desde == desde = desde : primerosNPerfectosDesde (desde + 1) (contador - 1)
  | otherwise = primerosNPerfectosDesde (desde + 1) contador

--

listaDeAmigos :: [Int] -> [(Int, Int)]
listaDeAmigos [] = []
listaDeAmigos [x] = []
listaDeAmigos (x : xs) = buscarAmigosDeX x xs ++ listaDeAmigos xs

-- HELPER
buscarAmigosDeX :: Int -> [Int] -> [(Int, Int)]
buscarAmigosDeX _ [] = []
buscarAmigosDeX x (y : ys)
  | sonAmigos x y = (x, y) : buscarAmigosDeX x ys
  | otherwise = buscarAmigosDeX x ys