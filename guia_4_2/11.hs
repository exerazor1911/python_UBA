eAprox :: Int -> Float
eAprox n
  | n <= 0 = 1
  | otherwise = 1 / fromIntegral (factorial n) + eAprox (n - 1)

-- HELPER
factorial :: Int -> Int
factorial 0 = 1
factorial num = num * factorial (num - 1)

e :: Float
e = eAprox 10