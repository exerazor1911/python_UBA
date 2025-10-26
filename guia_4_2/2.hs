parteEntera :: Float -> Int
parteEntera n
  | n >= 1 = 1 + parteEntera (n - 1)
  | otherwise = 0