from Productos import Productos

class App:
    
    def __init__(self):
        self.productos = []
        self.products = [
{ "id": 1, "name": "Nevera", type: "Hogar", "stock": 753, "price": 800 },
{ "id": 2, "name": "Cama", type: "Hogar", "stock": 327, "price": 600 },
{ "id": 3, "name": "Suéter", type: "Ropa", "stock": 260, "price": 25 },
{ "id": 4, "name": "Zapatos", type: "Ropa", "stock": 593, "price": 5 },
{ "id": 5, "name": "Laptop Gamer", type: "Gaming", "stock": 11, "price": 2500 },
{ "id": 6, "name": "Nintendo Switch OLED", type: "Gaming", "stock": 25, "price": 400 },
]


    def descargar_datos(self):
        for productos in self.products:
            self.productos.append(Productos(productos["id"], productos["name"], productos[type], productos["stock"], productos["price"]))

    def imprimir_productos(self):
        print (self.productos)
        for productos in self.productos:
            print(productos.mostrar())


    def start(self):
        self.productos
        self.descargar_datos()
        while True:
            print ("Ingrese\n1. Si desea ver los productos \n2. Salir")
            x = input(">")

            if x == "1":
                print("------ CATÁLOGO DE PRODUCTOS------")
                self.imprimir_productos()
            elif x == "2":
                print("ADIOS")
            else:
                print ("Ingreso invalido")
