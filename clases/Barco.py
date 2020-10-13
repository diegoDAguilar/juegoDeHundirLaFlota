# 'X' disparo en agua
# 'O' barco
# ' ' agua

import numpy as np

class Barco:

    def __init__(self, coordenadas):


        #Diccionario de coordenadas
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

    def golpear_barco(self, impacto):
        self.coordenadas[impacto] = False
        print('Barco golpeado')

##TEST

if __name__ == '__main__':
    barco1 = Barco(5,5,4,'n')
    print(barco1.estoy_vivo())

## FIN TEST