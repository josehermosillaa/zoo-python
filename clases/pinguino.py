from .animal import Animal

class Pinguino(Animal):
    def __init__(self, nombre, edad, nivel_salud=10, nivel_felicidad=10):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.reproduccion = 'Oviparo'

    def display_info(self):
        print('-'*15,"Tipo: ",self.__class__.__name__,'-'*15)
        super().display_info()
        
    def alimentar(self):
            print(f''' se esta alimentando a {self.nombre} con Pez, ñam ñam''')
            #
            if self.nivel_salud+15 >100:
                self.nivel_salud = 100
            else:
                self.nivel_salud += 15
            if self.nivel_felicidad+15>100:
                self.nivel_felicidad = 100
            else:
                self.nivel_felicidad += 15
            print(f'''los nuevos parametros de {self.nombre} son''')
            self.display_info()    