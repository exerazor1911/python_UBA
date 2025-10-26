esDivisible :: Int -> Int -> Bool
esDivisible a b
  | a < b = False
  | a == b = True
  | otherwise = esDivisible (a - b) b