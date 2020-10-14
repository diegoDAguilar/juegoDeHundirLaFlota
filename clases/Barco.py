# 'X' disparo en agua
# 'O' barco
# ' ' agua

import numpy as np

class Barco:

    def __init__(self, coordenadas):


        #Diccionario de coordenadas
        self.coordenadas = dict(zip([x for x in coordenadas], [True for x in coordenadas]))
        #print(self.coordenadas)

    def estoy_vivo(self):
        for c in self.coordenadas.values():
            if c:
                #print('Estoy vivo')
                return True

        else:
            print('Barco hundido')
            return False

    def golpear_barco(self, impacto):
        c = impacto[0]
        f = impacto[1]
        self.coordenadas[c, f] = False
        #print('Barco golpeado')

    def get_coordenadas(self):
        return self.coordenadas.keys()
##TEST

if __name__ == '__main__':
    barco1 = Barco(5,5,4,'n')
    print(barco1.estoy_vivo())

## FIN TEST