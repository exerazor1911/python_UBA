sumatoria :: Int -> Int -> Int
sumatoria 1 m = sumatoriaInterna 1 m
sumatoria n m = sumatoriaInterna n m + sumatoria (n - 1) m

sumatoriaInterna :: Int -> Int -> Int
sumatoriaInterna n 1 = n
sumatoriaInterna n m = n ^ m + sumatoriaInterna n (m - 1)