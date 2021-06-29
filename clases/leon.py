from .animal import Animal

class Leon(Animal):
    def __init__(self, nombre, edad, nivel_salud=10, nivel_felicidad=10):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.reproduccion = 'viviparo'
    
    def display_info(self):
        print('-'*15,"Tipo: ",self.__class__.__name__,'-'*15)
        super().display_info()

    def alimentar(self):
            print(f''' se esta alimentando a {self.nombre} con Carne, ñam ñam''')
            #
            if self.nivel_salud+30 >100:
                self.nivel_salud = 100
            else:
                self.nivel_salud += 30
            if self.nivel_felicidad+30>100:
                self.nivel_felicidad = 100
            else:
                self.nivel_felicidad += 30
            print(f'''los nuevos parametros de {self.nombre} son''')
            self.display_info()