from claseCaja import *
#construimos unobjeto de la clasecaja
cajita = Caja(5,6,1.5)
#usamos el metodo mostrar
print (cajita.mostrar())
#mostramos su Volumen
print("Volumen: ", cajita.calcularVlumen())
#mostramos su area
print ("Area total: ", cajita.calcularAreaTotal())
#creamos clon
miClono = cajita.clon()
#mostramos info del clon
print(miClono.mostrar())
#creamos una caja mas grande a paertir del clon con ayuda de cajita
caja25MasGrande = cajita.crearCajaGrande()
#mostramos info de la caja mas grande
print(caja25MasGrande.mostrar())
#verificamos si la primer caja cabe en la segunda
res = miClono.cabe1DentroDe2(miClono,caja25MasGrande)
print("Mas garnde? ", res)

