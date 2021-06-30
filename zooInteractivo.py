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
    
zoo = []
while True:

    print("Bienvenido al sistema de ZOOlogicos")
    menu = input("1.Agregar Zoologico \n2.Ingresar a Zoologico \n3.Quitar Zoologicos \n4.Salir \n Ingrese una opcion: ")
    if menu == "1":
        nombre_zoologico = input("Ingrese el nombre del Zoologico:")
        # zoo.append(nombre_zoologico)
        zoologico= Zoo(f"{nombre_zoologico}")
        zoo.append(zoologico)
        print(f"se ha agregado el zoologico {zoologico.name}")
        time.sleep(2)
        continue
    elif menu == "2":
        print("los zoologicos agregados son:")
        for zoologico in zoo:
            print(zoo.index(zoologico),"-",">",zoologico.name)
        while True:
            i = int(input("ingrese la opcion de su zoologico:"))
            print("zoologico seleccionado",zoo[i].name)
            time.sleep(2)
            seleccion=int(input("1. Agregar Animal \n2. Mostrar Animales \n3. Alimentar Animales \n4. Salir del Zoologico \nIngrese una opcion:"))
            if seleccion == 1:
                while True :
                    numero = int(input("Que animal desea aregar? : \n1. Leon \n2. Pinguino \n3. Elefante \n4. Oso \n5. Volver atras "))
                    if numero == 1:
                        pass
                    elif numero == 2:
                        pass
                    elif numero == 3:
                        pass
                    elif numero == 4:
                        pass
                    elif numero == 5:
                        print("los zoologicos agregados son:")
                        for zoologico in zoo:
                            print(zoo.index(zoologico),"-",">",zoologico.name)
                        break
                    else:
                        print("La opcion ingresada no es valida")
                        continue
                        
            elif seleccion == 2:
                pass
            elif seleccion == 3:
                pass
            elif seleccion == 4:
                break
            else:
                print("tecla no reconocida")
                time.sleep(0.5)
                print("intente nuevamente")
                time.sleep(0.5)
                continue
    elif menu == "3":
        continue
    elif menu == "4":
        print("Hasta pronto")
        time.sleep(1)
        break
    else:
        print("tecla no reconocida")
        time.sleep(1) #en segundos
        pass


