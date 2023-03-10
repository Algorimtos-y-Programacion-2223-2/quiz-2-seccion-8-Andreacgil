from Edificio import Edificio 

class App:
    def __init__(self):
        self.edificios = []



    def constructor(self):
        nuevo_nombre = len(self.edificios) + 1 
        nombre = input ("Nombre del edificio:  ")
        pisos = input ("Numero de pisos: ")
        calle =  input ("Calle donde se ubica: ")
        ciudad = input ("Ciudad: ")
        codigo_postal = input ("Código postal: ")
        apartamentos = input ("Lista de apartamentos: ")

        self.edificios.append(nuevo_nombre, nombre, pisos, calle, ciudad, codigo_postal, apartamentos)

    def mostrar_direccion(self):
        for edificios in self.edificios:
            print (edificios.mostrar())


    def start(self):
        self.edificios
        while True:
            print ("Ingrese\n1. si desea agregar un edificio \n2. Si desea ver la direccion\n3. Salir")
            x = input(">")

            if x == "1":
                self.constructor()
            elif x == "2":
                self.mostrar_direccion()
            elif x== "3":
                print("salir")
                break
            else:
                print ("Ingreso invalido")

        



    
            
    


