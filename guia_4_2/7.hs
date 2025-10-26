iesimoDigito :: Int -> Int -> Int
iesimoDigito num digito = mod (div num (10 ^ (cantDigitos num - digito))) 10

cantDigitos :: Int -> Int
cantDigitos n
  | n < 10 = 1
  | otherwise = 1 + cantDigitos (div n 10)