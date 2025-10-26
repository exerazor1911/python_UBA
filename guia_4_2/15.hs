sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 m = sumaRacionalesInterna 1 m
sumaRacionales n m = sumaRacionalesInterna n m + sumaRacionales (n - 1) m

sumaRacionalesInterna :: Integer -> Integer -> Float
sumaRacionalesInterna n 1 = fromIntegral n
sumaRacionalesInterna n m = fromIntegral n / fromIntegral m + sumaRacionalesInterna n (m - 1)