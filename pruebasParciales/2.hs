type Alumno = (Nombre, Notas)

type Nombre = [Char]

type Notas = [Float]

aproboMasDeNMaterias :: [Alumno] -> Nombre -> Int -> Bool
aproboMasDeNMaterias [] _ _ = False
aproboMasDeNMaterias ((nom, notas) : alumnos) nombre cantidadMaterias
  | nombre == nom = contarMateriasAprobadas notas >= cantidadMaterias
  | otherwise = aproboMasDeNMaterias alumnos nombre cantidadMaterias

-- HELPER
contarMateriasAprobadas :: [Float] -> Int
contarMateriasAprobadas [] = 0
contarMateriasAprobadas (nota : notas)
  | nota >= 4 = 1 + contarMateriasAprobadas notas
  | otherwise = contarMateriasAprobadas notas

--

buenosAlumnos :: [Alumno] -> [Nombre]
buenosAlumnos [] = []
buenosAlumnos ((nom, notas) : alumnos)
  | esBuenAlumno notas (contarCantidadDeNotas notas) = nom : buenosAlumnos alumnos
  | otherwise = buenosAlumnos alumnos

-- HELPER

contarCantidadDeNotas :: Notas -> Int
contarCantidadDeNotas [] = 0
contarCantidadDeNotas (nota : notas) = 1 + contarCantidadDeNotas notas

esBuenAlumno :: Notas -> Int -> Bool
esBuenAlumno [] _ = True
esBuenAlumno _ 0 = True
esBuenAlumno notas cantidadDeNotas = not (tieneAplazos notas) && sumarNotas notas / fromIntegral cantidadDeNotas >= 8

tieneAplazos :: Notas -> Bool
tieneAplazos [] = False
tieneAplazos (nota : notas)
  | nota < 4 = True
  | otherwise = tieneAplazos notas

sumarNotas :: Notas -> Float
sumarNotas [] = 0
sumarNotas (nota : notas) = nota + sumarNotas notas

--

mejorPromedio :: [Alumno] -> Nombre
mejorPromedio alumnos = calcularPromedioDesdeBase alumnos 0 ""

-- HELPER
calcularPromedioDesdeBase :: [Alumno] -> Float -> Nombre -> Nombre
calcularPromedioDesdeBase [] _ nombreMayorPromedio = nombreMayorPromedio
calcularPromedioDesdeBase ((nombre, notas) : alumnos) promedioMasAlto nombreMayorPromedio
  | (sumarNotas notas / fromIntegral (contarCantidadDeNotas notas)) > promedioMasAlto = calcularPromedioDesdeBase alumnos (sumarNotas notas / fromIntegral (contarCantidadDeNotas notas)) nombre
  | otherwise = calcularPromedioDesdeBase alumnos promedioMasAlto nombreMayorPromedio

--

seGraduoConHonores :: [Alumno] -> Int -> Nombre -> Bool
seGraduoConHonores registro cantMateriasCarrera alumno = aproboMasDeNMaterias registro alumno (cantMateriasCarrera - 1) && perteneceABuenosAlumnos alumno registro && promedioAMenosDe1Punto alumno registro

-- HELPER
perteneceABuenosAlumnos :: Nombre -> [Alumno] -> Bool
perteneceABuenosAlumnos _ [] = False
perteneceABuenosAlumnos nom ((nombre, notas) : alumnos)
  | nom == nombre = esBuenAlumno notas (contarCantidadDeNotas notas)
  | otherwise = perteneceABuenosAlumnos nom alumnos

promedioAMenosDe1Punto :: Nombre -> [Alumno] -> Bool
promedioAMenosDe1Punto nombre alumnos = calcularPromedio nombre alumnos >= (calcularMejorPromedioDesdeBase alumnos 0 - 1)

calcularMejorPromedioDesdeBase :: [Alumno] -> Float -> Float
calcularMejorPromedioDesdeBase [] promedioMasAlto = promedioMasAlto
calcularMejorPromedioDesdeBase ((nombre, notas) : alumnos) promedioMasAlto
  | (sumarNotas notas / fromIntegral (contarCantidadDeNotas notas)) > promedioMasAlto = calcularMejorPromedioDesdeBase alumnos (sumarNotas notas / fromIntegral (contarCantidadDeNotas notas))
  | otherwise = calcularMejorPromedioDesdeBase alumnos promedioMasAlto

calcularPromedio :: Nombre -> [Alumno] -> Float
calcularPromedio _ [] = 0
calcularPromedio nombre ((nom, notas) : alumnos)
  | nombre == nom = sumarNotas notas / fromIntegral (contarCantidadDeNotas notas)
  | otherwise = calcularPromedio nombre alumnos