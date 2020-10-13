# 'X' disparo en agua
# 'O' barco
# ' ' agua

import numpy as np

class Barco:

    def __init__(self, x, y, tam_barco, orientacion):

        self.columna = x
        self.fila = y
        self.tam_barco = tam_barco
        self.orientacion = orientacion

        # Coordenadas vienen por slicing [x,a-y],
        # necesitamos individualizar cada punto del barco
        coordenadas = []
        if self.orientacion == 'n':
            for i in range(self.tam_barco):
                coordenadas.append((self.columna - i, self.fila))
        elif self.orientacion == 's':
            for i in range(self.tam_barco):
                coordenadas.append((self.columna, self.fila + i))
        elif self.orientacion == 'e':
            for i in range(self.tam_barco):
                coordenadas.append((self.columna + i, self.fila))
        elif self.orientacion == 'o':
            for i in range(self.tam_barco):
                coordenadas.append((self.columna, self.fila - i))


        #Lista de coordenadas
        self.coordenadas = dict(zip([x for x in coordenadas], [True for x in coordenadas]))
        print(self.coordenadas)

    def estoy_vivo(self):
        for coordenada in self.coordenadas.values():
            if coordenada == True:
                print('Estoy vivo')
                return True

        else:
            print('Estoy hundido')
            return False

##TEST

if __name__ == '__main__':
    barco1 = Barco(5,5,4,'n')
    print(barco1.estoy_vivo())

## FIN TEST