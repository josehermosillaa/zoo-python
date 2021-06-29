import time
from clases.animal import Animal
from clases.elefante import Elefante
from clases.leon import Leon
from clases.pinguino import Pinguino
from clases.oso import Oso
class Zoo:
    def __init__(self, zoo_name):
        self.animales = []
        self.name = zoo_name
    def add_leon(self, nombre,edad):
        self.animales.append( Leon(nombre,edad) )
        
        
    def add_pinguino(self, nombre,edad):
        self.animales.append(Pinguino(nombre,edad) )
    
    def add_elefante(self,nombre,edad): 
        self.animales.append(Elefante(nombre,edad) )
    
    def add_oso(self, nombre, edad):
        self.animales.append(Oso(nombre,edad) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animales:
            animal.display_info()

    def lista_animales(self):
        # print(f"la lista es:{self.animales}")#siempre se debe hacer con un for
        for i in range(len(self.animales)):
            print(self.animales[i].nombre)
            print(self.animales[i].edad)
            # print(self.animales[i].nivel_felicidad)
    
    def alimentar_a_todos(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animales:
            animal.alimentar()
        return self
    

while True:
    print("Bienvenido al sistema de ZOOlogicos")
    menu = input("1.Agregar Zoologico \n2.Agregar Animal \n 3.Mostrar Zoologicos \n4.Alimentar Animales \n5.Salir \n Ingrese una opcion: ")
    if menu == "1":
        pass
    elif menu == "2":
        pass
    elif menu == "3":
        pass
    elif menu == "4":
        pass
    elif menu == "5":
        break
    else:
        print("tecla no reconocida")
        time.sleep(1) #en segundos
        pass
