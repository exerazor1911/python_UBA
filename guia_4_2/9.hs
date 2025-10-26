-- HELPER
iesimoDigito :: Int -> Int -> Int
iesimoDigito num digito = mod (div num (10 ^ (cantDigitos num - digito))) 10

cantDigitos :: Int -> Int
cantDigitos n
  | n < 10 = 1
  | otherwise = 1 + cantDigitos (div n 10)

--
esCapicua :: Int -> Bool
esCapicua n = esCapicuaRango (iesimoDigito n 1) (cantDigitos n) n

esCapicuaRango :: Int -> Int -> Int -> Bool
esCapicuaRango desde hasta num
  | desde == hasta = True
  | otherwise = iesimoDigito num desde == iesimoDigito num hasta && esCapicuaRango (desde + 1) (hasta - 1) num