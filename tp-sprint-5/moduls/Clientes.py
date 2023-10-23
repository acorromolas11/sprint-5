from tipos.Classic import Classic
from tipos.Gold import Gold
from tipos.Black import Black

class Clientes:
    def  __init__(self,nombre,apellido,tipo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo
        if(self.tipo.lower()=='classic'):
            self.tipo = Classic()
        elif(self.tipo.lower()=='gold'):
            self.tipo = Gold()
        elif(self.tipo.lower()=='black'):
            self.tipo = Black()