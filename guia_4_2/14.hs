sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q 1 m = sumaPotenciasInterna q 1 m
sumaPotencias q n m = sumaPotenciasInterna q n m + sumaPotencias q (n - 1) m

sumaPotenciasInterna :: Integer -> Integer -> Integer -> Integer
sumaPotenciasInterna q n 1 = q ^ (n + 1)
sumaPotenciasInterna q n m = q ^ (n + m) + sumaPotenciasInterna q n (m - 1)