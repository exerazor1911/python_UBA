-- mercaderia = [NombreProductos] (Pueden haber repetidos)
-- stock = [(nombreProducto,cantidadEnStock)] = no hay repetidos
-- listaDePrecios = [(nombreProducto,precio)]

type Precio = Float

type Cantidad = Int

type NombreProducto = String

type Mercaderia = [NombreProducto]

type Stock = [(NombreProducto, Cantidad)]

type ListaDePrecios = [(NombreProducto, Precio)]

--

generarStock :: Mercaderia -> Stock
generarStock [] = []
generarStock (nombreProducto : nombresProductos) = (nombreProducto, apariciones nombreProducto nombresProductos) : generarStock (eliminarTodos nombreProducto (nombreProducto : nombresProductos))

-- HELPERS
apariciones :: NombreProducto -> [NombreProducto] -> Cantidad
apariciones _ [] = 1
apariciones nombreProducto (nomProdu : productos)
  | nombreProducto == nomProdu = 1 + apariciones nombreProducto productos
  | otherwise = apariciones nombreProducto productos

eliminarTodos :: NombreProducto -> Mercaderia -> Mercaderia
eliminarTodos _ [] = []
eliminarTodos nombreProducto (nomProdu : nomProductos)
  | nombreProducto == nomProdu = eliminarTodos nombreProducto nomProductos
  | otherwise = nomProdu : eliminarTodos nombreProducto nomProductos

--

stockDeProducto :: Stock -> NombreProducto -> Cantidad
stockDeProducto [] _ = 0
stockDeProducto ((nomProdu, cantidad) : stocks) nombreProducto
  | nombreProducto == nomProdu = cantidad
  | otherwise = stockDeProducto stocks nombreProducto

--

dineroEnStock :: Stock -> ListaDePrecios -> Precio
dineroEnStock [] _ = 0
dineroEnStock _ [] = 0
dineroEnStock ((nombreDeProducto,cantidad):stocks) listaDePrecios = damePrecioDeLista nombreDeProducto listaDePrecios * fromIntegral cantidad + dineroEnStock stocks listaDePrecios

-- HELPER
damePrecioDeLista :: NombreProducto -> ListaDePrecios -> Precio
damePrecioDeLista _ [] = 0
damePrecioDeLista producto ((nombreProducto,precio):listaPrecios) | producto == nombreProducto = precio
                                                                  | otherwise = damePrecioDeLista producto listaPrecios

--
aplicarOferta :: Stock -> ListaDePrecios -> ListaDePrecios
aplicarOferta [] _ = []
aplicarOferta _ [] = []
aplicarOferta stock ((nomProdu,precio):listaDePrecios) = (nomProdu,calcularPrecio stock nomProdu precio) : aplicarOferta stock listaDePrecios

calcularPrecio :: Stock -> NombreProducto -> Precio -> Precio
calcularPrecio stock nombreDeProducto precio | stockDeProducto stock nombreDeProducto > 10 = precio * 0.80
                                             | otherwise = precio