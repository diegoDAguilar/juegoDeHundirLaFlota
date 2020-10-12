import numpy as np
from Constantes import *

class Tablero:
    def __init__(self, tamanio=10):
        self.matriz = np.full((tamanio, tamanio), AGUA)

    def colocar_barco(self, tam_barco='auto', coordenadas='auto',
                      orientacion='auto'):

        self.tam_barco = tam_barco
        self.orientacion = orientacion
        self.coordenadas = coordenadas
        orientaciones = ['n', 's', 'e', 'o']

        # Si los parámetros están en auto, los genera, sino coge los definidos
        if self.orientacion == 'auto':
            self.orientacion = orientaciones[np.random.randint(4)]

        if self.coordenadas == 'auto':
            self.coordenadas = np.random.randint(self.matriz.shape[0],
                                                 size=(1, 2))  # Array de (X,Y)
        else:
            self.coordenadas = np.array([coordenadas])


        while True:
            # Variables del tablero
            # x es el segundo elemento, y es el primero
            x = self.coordenadas[0][1]
            y = self.coordenadas[0][0]
            x_limit = self.matriz.shape[0]
            y_limit = self.matriz.shape[1]

            # Comprobamos si la posición es posible en cada orientación,
            # después comprobamos que en las coordenadas no hay barcos
            # y colocamos el nuestro

            if (0 <= y - self.tam_barco) and (self.orientacion == 'n'):
                if BARCO_VIVO not in self.matriz[x, (y - self.tam_barco):y]:
                    self.matriz[(x - self.tam_barco):x, y] = BARCO_VIVO
                    print(x, y - self.tam_barco, y)
                    break

            elif (y + self.tam_barco < y_limit) and (self.orientacion == 's'):
                if BARCO_VIVO not in self.matriz[x, y:(y + self.tam_barco)]:
                    self.matriz[x:(x + self.tam_barco), y] = BARCO_VIVO
                    break

            elif (x + self.tam_barco < x_limit) and (self.orientacion == 'e'):
                if BARCO_VIVO not in self.matriz[x:(x + self.tam_barco), y]:
                    self.matriz[x, y:(y+self.tam_barco)] = BARCO_VIVO
                    break

            elif (0 <= x - self.tam_barco) and (self.orientacion == 'o'):
                if BARCO_VIVO not in self.matriz[(x - self.tam_barco):x, y]:
                    self.matriz[x, (y-self.tam_barco):y] = BARCO_VIVO
                    break

            # Si las coordenadas no son válidas,
            # generamos unas nuevas y repetimos el proceso

            self.orientacion = orientaciones[np.random.randint(4)]
            self.coordenadas = np.random.randint(x_limit, size=(1, 2))  # Array de (X,Y)

        print('Barco creado')
        print(self.orientacion)
        return True


    def colocar_todos_barcos(self):
        tamanios_barco = [1,1,1,1,2,2,2,3,3,4]
        for t in tamanios_barco:
            x,y = 0,0 # TODO aniadir random y la orientacion random
            orientacion = 'N'
            self.colocar_barco(t, (x,y), orientacion)

    def devolver_tablero(self):
        return self.matriz


tab1 = Tablero()
print(tab1.devolver_tablero())
#BARCO_VIVO in tab1.matriz[1,3]
tab1.colocar_barco(4, (5,5), 'n')
print(tab1.devolver_tablero())