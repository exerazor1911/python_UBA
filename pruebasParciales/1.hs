type Formulas = [(Presidente, VicePresidente)]

type Presidente = String

type VicePresidente = String

type Votos = [Int]

-- 1

votosEnBlanco :: Formulas -> Votos -> Int -> Int
votosEnBlanco _ [] cantidadDeVotos = cantidadDeVotos
votosEnBlanco formulas (voto : votos) cantidadDeVotos = votosEnBlanco formulas votos (cantidadDeVotos - voto)

-- 2

formulasValidas :: Formulas -> Bool
formulasValidas [] = True
formulasValidas (formula : formulas) = compararConElResto formula formulas && formulasValidas formulas

-- HELPER
compararConElResto :: (Presidente, VicePresidente) -> Formulas -> Bool
compararConElResto _ [] = True
compararConElResto (presidente, vicePresidente) ((presi, vice) : formulas)
  | presidente == vicePresidente || presidente == presi || presidente == vice || vicePresidente == presi || vicePresidente == vice = False
  | otherwise = compararConElResto (presidente, vicePresidente) formulas

-- 3

porcentajeDeVotos :: Presidente -> Formulas -> Votos -> Float
porcentajeDeVotos _ _ [] = 0
porcentajeDeVotos _ [] _ = 0
porcentajeDeVotos presidente formulas votos = porcentajeDeVotosConTotal presidente formulas votos (calcularTotalVotos votos)

-- HELPER
division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

calcularTotalVotos :: Votos -> Int
calcularTotalVotos [] = 0
calcularTotalVotos (voto : votos) = voto + calcularTotalVotos votos

porcentajeDeVotosConTotal :: Presidente -> Formulas -> Votos -> Int -> Float
porcentajeDeVotosConTotal presidente ((presi, vice) : formulas) (voto : votos) totalVotos
  | presidente == presi = division (voto * 100) totalVotos
  | otherwise = porcentajeDeVotosConTotal presidente formulas votos totalVotos

-- 4

proximoPresidente :: Formulas -> Votos -> Presidente
proximoPresidente formulas votos = proximoPresidenteConTotalDeVotos formulas votos (calcularTotalVotos votos)

-- HELPER
proximoPresidenteConTotalDeVotos :: Formulas -> Votos -> Int -> Presidente
proximoPresidenteConTotalDeVotos [(presi, vice)] _ _ = presi
proximoPresidenteConTotalDeVotos ((presi1, vice1) : (presi2, vice2) : formulas) (voto1 : voto2 : votos) totalVotos
  | porcentajeDeVotosConTotal presi1 ((presi1, vice1) : (presi2, vice2) : formulas) (voto1 : voto2 : votos) totalVotos > porcentajeDeVotosConTotal presi2 ((presi2, vice2) : formulas) (voto2 : votos) totalVotos = proximoPresidenteConTotalDeVotos ((presi1, vice1) : formulas) (voto1 : votos) totalVotos
  | otherwise = proximoPresidenteConTotalDeVotos ((presi2, vice2) : formulas) (voto2 : votos) totalVotos