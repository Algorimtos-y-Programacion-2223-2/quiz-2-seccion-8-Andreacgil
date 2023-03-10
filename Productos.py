class Productos:
    
    def __init__(self,id,name, type, stock, price):
        self.id = id
        self.name = name
        self.type = type 
        self.stock = stock
        self.price = price

    def mostrar(self):
        return(f"Cedula:{self.id} \nNombre: {self.name}\nTipo: {self.type}\nStock: {self.stock}\nPrecio: {self.price} \n\n")

