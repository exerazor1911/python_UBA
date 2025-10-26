parteEntera :: Float -> Integer
parteEntera x
    | x < 1.0 = 0
    | otherwise = 1 + parteEntera (x - 1.0) 