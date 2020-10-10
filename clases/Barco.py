# 'X' disparo en agua
# 'O' barco
# ' ' agua

import numpy as np

class Barco:

    def __init__(self, coordenadas):

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

coors = ([(1,3),
          (2,3),
          (3,3)])

barco1 = Barco(coors)
print(barco1.estoy_vivo())

##FIN TEST