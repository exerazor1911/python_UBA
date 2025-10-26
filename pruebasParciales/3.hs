mediaMovilN :: [Int] -> Int -> Float
mediaMovilN lista n = mediaMovilHelper lista n (longitud lista - n)

-- HELPER
longitud :: [Int] -> Int
longitud [] = 0
longitud (x : xs) = 1 + longitud xs

mediaMovilHelper :: [Int] -> Int -> Int -> Float
mediaMovilHelper lista cantElem 0 = fromIntegral (sumarElemLista lista) / fromIntegral cantElem
mediaMovilHelper (x : xs) cantElem sacar = mediaMovilHelper xs cantElem (sacar - 1)

sumarElemLista :: [Int] -> Int
sumarElemLista [] = 0
sumarElemLista (x : xs) = x + sumarElemLista xs

--

esAtractivo :: Int -> Bool
esAtractivo n = esPrimo (contarFactoresPrimos n (sacarPrimos (factores n n)))

contarFactoresPrimos :: Int -> [Int] -> Int
contarFactoresPrimos _ [] = 0
contarFactoresPrimos num (factorPrimo : factoresPrimos)
  | mod num factorPrimo == 0 = 1 + contarFactoresPrimos (div num factorPrimo) (factorPrimo : factoresPrimos)
  | otherwise = contarFactoresPrimos num factoresPrimos

sacarPrimos :: [Int] -> [Int]
sacarPrimos [] = []
sacarPrimos (num : nums)
  | esPrimo num = num : sacarPrimos nums
  | otherwise = sacarPrimos nums

esPrimo :: Int -> Bool
esPrimo 1 = False
esPrimo n = esPrimoHelper n 2

esPrimoHelper :: Int -> Int -> Bool
esPrimoHelper num hasta
  | hasta == num = True
  | mod num hasta == 0 = False
  | otherwise = esPrimoHelper num (hasta + 1)

factores :: Int -> Int -> [Int]
factores _ 1 = [1]
factores num cont
  | mod num cont == 0 = cont : factores num (cont - 1)
  | otherwise = factores num (cont - 1)

--

palabraOrdenada :: [Char] -> Bool
palabraOrdenada [] = True
palabraOrdenada [x] = True
palabraOrdenada (x : y : xs)
  | x == ' ' = palabraOrdenada (y : xs)
  | y == ' ' = palabraOrdenada xs
  | x > y = False
  | otherwise = palabraOrdenada (y : xs)

--

similAnagrama :: [Char] -> [Char] -> Bool
similAnagrama palabra1 palabra2 = similAnagramaAux palabra1 palabra1 palabra2 && chequearPosiciones palabra1 palabra2

similAnagramaAux :: [Char] -> [Char] -> [Char] -> Bool
similAnagramaAux [] _ _ = True
similAnagramaAux (letra : palabra) palabra1 palabra2
  | letra == ' ' = similAnagramaAux palabra palabra1 palabra2
  | otherwise = cantidadApariciones letra palabra1 == cantidadApariciones letra palabra2 && similAnagramaAux palabra palabra1 palabra2

cantidadApariciones :: Char -> [Char] -> Int
cantidadApariciones _ [] = 0
cantidadApariciones c (x : xs)
  | c == x = 1 + cantidadApariciones c xs
  | otherwise = cantidadApariciones c xs

chequearPosiciones :: [Char] -> [Char] -> Bool
chequearPosiciones [] _ = False
chequearPosiciones (p1 : p1s) (p2 : p2s)
  | p1 /= p2 = True
  | otherwise = chequearPosiciones p1s p2s
