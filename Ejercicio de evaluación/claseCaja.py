class Caja ():
    def __init__(self,ancho, largo,alto):
        self.ancho = ancho
        self.largo = largo
        self.alto = alto
    def mostrar(self):
        return"Alto: ",self.alto," Ancho: ", self.ancho," Largo", self.largo
    def calcularVlumen(self):
        r = (self.alto * self.ancho * self.largo)   
        return r
    def areaFrontal(self):
        return self.alto * self.ancho 
    def areaLateral(self):
        return self.largo * self.alto 
    def areaSuperior(self):
        return self.largo * self.ancho 
    def calcularAreaTotal(self):
        r = (2 * self.areaFrontal() + 2 * self.areaSuperior() + 2 *self.areaLateral())
        return r 
    def clon(self):
        c = Caja(self.ancho, self.largo, self.alto)
        return c
    def crearCajaGrande(self):
       nuevoAlto = self.alto * 1.25
       nuevoAncho = self.ancho * 1.25
       nuevoLargo = self.largo * 1.25

       cajaNueva = Caja(nuevoAncho, nuevoLargo, nuevoAlto)
       return cajaNueva
       
    def cabe1DentroDe2(self, c,cajaNueva):
        if c.ancho < cajaNueva.ancho and c.alto < cajaNueva.alto and c.largo < cajaNueva.largo: 
            return "Si cabe"
        else:
            return "No cabe"
        
          

    