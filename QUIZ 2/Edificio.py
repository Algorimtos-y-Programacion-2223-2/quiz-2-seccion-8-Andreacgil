class Edificio:

    def __init__(self, nombre, pisos, calle, ciudad, codigo_postal, apartamentos):
        self.nombre = nombre
        self.pisos = pisos
        self.calle = calle
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.apartamentos = apartamentos 


    def mostrar(self):
        return (f"Nombre: {self.nombre}, Pisos: {self.pisos}, Calle: {self.calle}, Ciudad: {self.ciudad}, Codigo postal: {self.codigo_postal}, Apartamentos: {self.apartamentos}")
    

