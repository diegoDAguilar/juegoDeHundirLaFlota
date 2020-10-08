import numpy as np


class Tablero:
    def __init__(self, tamanio_tablero=10):
        self.matriz = np.full((tamanio_tablero, tamanio_tablero), ' ')

    def colocar_barco(self, tamanio_barco, coord_inicial, orientacion):
        # comprueba si puede colocar el barco y devuelve True/ False
        return True


tab1 = Tablero()
print(tab1.matriz)
