import random
def randint(min = 0, max = 100):
    if min == 0:
        num = round(max*(random.random()))
        
        return num
    else:
        num = round((max-min)*(random.random())+min)
        
        return num
# Una vez que haya probado sus diferentes animales y se sienta más cómodo con la herencia, cree una clase de zoológico para ayudar a manejar a todos sus animales.
class Animal:
    def __init__(self, nombre, edad,nivel_salud=10,nive_felicidad=10):
        self.nombre = nombre
        self.edad = edad
        self.nivel_salud = randint()
        self.nivel_felicidad = randint()

    def display_info(self):
        print(f'''
        Nombre: {self.nombre}
        Edad  : {self.edad}
        Salud : {self.nivel_salud}%
        Felicidad: {self.nivel_felicidad}%
        ''')
        
        return self
    
    def alimentar(self):
        raise NotImplementedError("No esta implementada la funcion")
        # print(f''' se esta alimentando a {self.name}, ñam ñam''')
        # if self.nivel_salud+10 >100:
        #     self.nivel_salud = 100
        # else:
        #     self.nivel_salud += 10
        # if self.nivel_felicidad+10>100:
        #     self.nivel_felicidad = 100
        # else:
        #     self.nivel_felicidad += 10
        # print(f'''los nuevos parametros de {self.name} son''')
        # self.display_info()
