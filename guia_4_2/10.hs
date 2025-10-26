-- A
f1 :: Int -> Int
f1 n = f1DesdeHasta 0 n

f1DesdeHasta :: Int -> Int -> Int
f1DesdeHasta desde hasta
  | desde == hasta = 2 ^ desde
  | otherwise = 2 ^ desde + f1DesdeHasta (desde + 1) hasta

-- B
f2 :: Int -> Int -> Int
f2 n q = f2DesdeHasta 1 n q

f2DesdeHasta :: Int -> Int -> Int -> Int
f2DesdeHasta desde hasta num
  | desde == hasta = num ^ desde
  | otherwise = num ^ desde + f2DesdeHasta (desde + 1) hasta num

-- C
f3 :: Int -> Int -> Int
f3 n q = f2 (n * 2) q

-- D
f4 :: Int -> Int -> Int
f4 n q = f4DesdeHasta n (n * 2) q

f4DesdeHasta :: Int -> Int -> Int -> Int
f4DesdeHasta desde hasta num
  | desde == hasta = num ^ desde
  | otherwise = num ^ desde + f4DesdeHasta (desde + 1) hasta num