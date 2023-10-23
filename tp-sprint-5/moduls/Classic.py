from exceptions.MaxCajaAhorro import MaxCajaAhorro

class Classic:
    def __init__(self, nombre, apellido, caja_ahorro_dolares = False) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.__tarjeta_debito = 0000000000000000
        self.__cajas_de_ahorro = [["Caja de ahorro en pesos 1", 1, 0]]
        self.__retiros_en_efectivo = {"Cajero 1": [0, 10000], "Cajero 2": [0, 10000]}
        self.__comisiones = {"Salientes": 0.1, "Entrantes": 0.05}
        if caja_ahorro_dolares:
            self.__cajas_de_ahorro.append([f"Caja de ahorro {len(self.__cajas_de_ahorro) + 1} en dolares", len(self.__cajas_de_ahorro) + 1, 0])

    def getCaja(self):
        return self.__cajas_de_ahorro
    
    def agregarCaja(self):
        try:
            if len(self.__cajas_de_ahorro) <= 2:
                self.__cajas_de_ahorro.append([f"Caja de ahorro {len(self.__cajas_de_ahorro) + 1} en pesos", len(self.__cajas_de_ahorro) + 1, 0])
            else:
                raise MaxCajaAhorro("No se puede agregar mas cajas de ahorro")
        except MaxCajaAhorro as e:
            print("Error: ", str(e))
