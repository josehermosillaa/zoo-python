
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
    
    # def __str__(self) -> str:
    #     str_con_el_resultado = 'Objeto de animales: '
    #     for animal in self.animales:
    #         str_con_el_resultado += "\n  * {}".format(animal)
    #     print(str_con_el_resultado)
    #     return str_con_el_resultado
    

zoo1 = Zoo("John's Zoo")
zoo1.add_leon("Nala",5)
zoo1.add_leon("Simba",6)
zoo1.add_pinguino("Rey Julien",4)
zoo1.add_pinguino("Rico",4)
zoo1.add_oso("Baloo",10)
zoo1.add_elefante("Dumbo",10)
zoo1.print_all_info()
zoo1.alimentar_a_todos()
# zoo1.lista_animales()
