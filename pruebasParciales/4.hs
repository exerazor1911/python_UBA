type NombreEquipo = String

type NombreGoleador = String

type GoleadorEquipo = (NombreEquipo, NombreGoleador)

type Goles = [Int]

--

golesDeNoGoleadores :: [GoleadorEquipo] -> Goles -> Int -> Int
golesDeNoGoleadores _ [] totalGoles = totalGoles
golesDeNoGoleadores goleadores (gol : goles) totalGoles = golesDeNoGoleadores goleadores goles (totalGoles - gol)

--

equiposValidos :: [GoleadorEquipo] -> Bool
equiposValidos [] = True
equiposValidos ((equipo, goleador) : equiposGoleadores)
  | perteneceEquipo equipo equiposGoleadores || perteneceGoleador goleador equiposGoleadores || perteneceGoleadorANombreEquipo goleador equiposGoleadores = False
  | otherwise = equiposValidos equiposGoleadores

-- HELPER
perteneceEquipo :: NombreEquipo -> [GoleadorEquipo] -> Bool
perteneceEquipo _ [] = False
perteneceEquipo nombreEquipo ((equipo, _) : equipos)
  | nombreEquipo == equipo = True
  | otherwise = perteneceEquipo nombreEquipo equipos

perteneceGoleador :: NombreGoleador -> [GoleadorEquipo] -> Bool
perteneceGoleador _ [] = False
perteneceGoleador nombreGoleador ((_, goleador) : equipos)
  | nombreGoleador == goleador = True
  | otherwise = perteneceGoleador nombreGoleador equipos

perteneceGoleadorANombreEquipo :: NombreGoleador -> [GoleadorEquipo] -> Bool
perteneceGoleadorANombreEquipo _ [] = False
perteneceGoleadorANombreEquipo nombreGoleador ((equipo, _) : equipos)
  | nombreGoleador == equipo = True
  | otherwise = perteneceGoleadorANombreEquipo nombreGoleador equipos

--

porcentajeDeGoles :: NombreGoleador -> [GoleadorEquipo] -> Goles -> Float
porcentajeDeGoles nombreGoleador equipos goles = division ((cantidadDeGolesDelGoleador nombreGoleador equipos goles) * 100) (cantidadDeGolesTotales goles)

-- HELPER
division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

cantidadDeGolesDelGoleador :: NombreGoleador -> [GoleadorEquipo] -> Goles -> Int
cantidadDeGolesDelGoleador nombreGoleador ((equipo, goleador) : equipos) (gol : goles)
  | goleador == nombreGoleador = gol
  | otherwise = cantidadDeGolesDelGoleador nombreGoleador equipos goles

cantidadDeGolesTotales :: Goles -> Int
cantidadDeGolesTotales [] = 0
cantidadDeGolesTotales (gol : goles) = gol + cantidadDeGolesTotales goles

--

botinDeOro :: [GoleadorEquipo] -> Goles -> NombreGoleador
botinDeOro equipos goles = botinDeOroAux equipos goles 0 ""

botinDeOroAux :: [GoleadorEquipo] -> Goles -> Int -> NombreGoleador -> NombreGoleador
botinDeOroAux [] [] _ nombreMayorGoleador = nombreMayorGoleador
botinDeOroAux ((equipo, goleador) : equipos) (gol : goles) mayorCantidadGoles nombreMayorGoleador
  | gol > mayorCantidadGoles = botinDeOroAux equipos goles gol goleador
  | otherwise = botinDeOroAux equipos goles mayorCantidadGoles nombreMayorGoleador