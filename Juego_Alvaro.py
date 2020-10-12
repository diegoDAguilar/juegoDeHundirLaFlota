# 'X' disparo en agua
# 'O' barco
# ' ' agua

import numpy as np


## CONSTANTES
BARCO_VIVO = 'O'
BARCO_TOCADO = 'X'
AGUA = ' '
IMPACTO_AGUA = '-'
barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]  # Lista de barcos que se crearán (MAIN)

## CLASES
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


class Tablero:

    def __init__(self, tamanio):

        #Construimos el tablero y lo llenamos de agua
        self.matriz = np.full((tamanio, tamanio), AGUA)

    def coloca_barco(self, tam_barco = 'auto', orientacion = 'auto',
                     coordenadas = 'auto'):

        self.tam_barco = tam_barco
        self.orientacion = orientacion
        self.coordenadas = coordenadas

        orientaciones = ['n', 's', 'e', 'o']

        #Instanciamos el modo aleatorio

        if self.orientacion == 'auto':
            self.orientacion = orientaciones[np.random.randint(4)]
            self.coordenadas = np.random.randint(self.matriz.shape[0],
                                                 size=(1, 2))  # Array de (X,Y)

        while True:

            #Variables del tablero

            x = self.coordenadas[0][0]
            y = self.coordenadas[0][1]
            x_limit = self.matriz.shape[0]
            y_limit = self.matriz.shape[1]

            # Comprobamos si la posición es posible en cada orientación,
            # después comprobamos que en las coordenadas no hay barcos
            # y colocamos el nuestro

            if (0 <= y-self.tam_barco) and (self.orientacion == 'n'):
                if BARCO_VIVO not in self.matriz[x, (y - self.tam_barco):y]:
                    self.matriz[x, y - self.tam_barco:y] = BARCO_VIVO
                    break

            elif (y + self.tam_barco < y_limit) and (self.orientacion == 's'):
                if BARCO_VIVO not in self.matriz[x, y:(y + self.tam_barco)]:
                    self.matriz[x, y:(y + self.tam_barco)] = BARCO_VIVO
                    break

            elif (x+self.tam_barco < x_limit) and (self.orientacion == 'e'):
                if BARCO_VIVO not in self.matriz[x:(x + self.tam_barco), y]:
                    self.matriz[x:(x + self.tam_barco), y] = BARCO_VIVO
                    break

            elif (0 <= x-self.tam_barco) and (self.orientacion == 'o'):
                if BARCO_VIVO not in self.matriz[(x - self.tam_barco):x, y]:
                    self.matriz[(x - self.tam_barco):x, y] = BARCO_VIVO
                    break

            # Si las coordenadas no son válidas,
            # generamos unas nuevas y repetimos el proceso

            self.orientacion = orientaciones[np.random.randint(4)]
            self.coordenadas = np.random.randint(x_limit, size=(1, 2)) #Array de (X,Y)

## FUNCIONES
def disparar(ataca, defiende, coordenadas = 'auto', dificultad = 1):

    if coordenadas == 'auto':
        while True:
            coordenadas = np.random.randint(defiende.tamanio.shape[0], size=(2,1))
            if defiende.tablero[coordenadas[0], coordenadas[1]] != BARCO_TOCADO and\
                    defiende.tablero[coordenadas[0],coordenadas[1]] != IMPACTO_AGUA:
                break

    # Coordenadas del tablero
    x,y  = coordenadas

    if defiende.tablero.matriz[x, y] == AGUA:
        defiende.tablero.matriz[x, y] = IMPACTO_AGUA
        ataca.visor.matriz[x, y] = IMPACTO_AGUA
        print('Has impactado en el agua')

    elif defiende.tablero.matriz[x, y] == BARCO_VIVO:
        defiende.tablero.matriz[x, y] = BARCO_TOCADO
        ataca.tablero.matriz[x, y] = BARCO_TOCADO
        print('¡Barco tocado!')


##TEST

#Creamos dos jugadores
j1 = Tablero(10)
j2 = Tablero(10)
print(j1.matriz)

#Colocamos todos los barcos en cada tablero
for i in barcos:
    j2.coloca_barco(tam_barco=i)
for i in barcos:
    j1.coloca_barco(tam_barco=i)

#Imprimimos los dos tableros
print('Jugador 1\n', j1.matriz)
print('Jugador 2\n', j2.matriz)

#El jugador 1 dispara 5 veces al jugador 2
for i in range(5):
    disparar(j1, j2)

#Imprimimos tablero del jugador 2 y la pantalla del jugador 1
print(j2.matriz)
print(j1.pantalla)


