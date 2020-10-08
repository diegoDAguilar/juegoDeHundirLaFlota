import numpy as np


class Tablero:
    def __init__(self, tamanio_tablero=10):
        self.matriz = np.full((tamanio_tablero, tamanio_tablero), ' ')

    def colocar_barco(self, tamanio_barco, coord_inicial, orientacion):
        # comprueba si puede colocar el barco y devuelve True/ False
        print('Barco creado')
        return True

    def colocar_todos_barcos(self):
        tamanios_barco = [1,1,1,1,2,2,2,3,3,4]
        for t in tamanios_barco:
            x,y = 0,0 # TODO aniadir random y la orientacion random
            orientacion = 'N'
            self.colocar_barco(t, (x,y),orientacion)

    def devolver_tablero(self):
        return self.matriz


tab1 = Tablero()
print(tab1.devolver_tablero())
