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
        self.tamanio = np.full((tamanio, tamanio), AGUA)
        self.pantalla = np.full((tamanio, tamanio), AGUA) #Esta es la pantalla donde visualizamos los disparos realizados

    def coloca_barco(self, tam_barco = 'auto', orientacion = 'auto', coordenadas = 'auto'):
        self.tam_barco = tam_barco
        self.orientacion = orientacion
        self.coordenadas = coordenadas

        orientaciones = ['n', 's', 'e', 'o']

        #Instanciamos el modo aleatorio
        if self.tam_barco == 'auto':
            self.tam_barco = np.random.randint(1, 5)  # Valor máximo de eslora: 4
        elif self.orientacion == 'auto':
            self.orientacion = orientaciones[np.random.randint(4)]
        elif self.coordenadas == 'auto':
            self.coordenadas = np.random.randint(self.tamanio.shape[0], size=(1, 2))  # Array de (X,Y)

        while True:
            self.orientacion = orientaciones[np.random.randint(4)]
            self.coordenadas = np.random.randint(self.tamanio.shape[0], size=(1, 2)) #Array de (X,Y)

            print(self.coordenadas, self.orientacion)
            print('[0]', self.coordenadas[0][0])
            print('[1]', self.coordenadas[0][1])

            #Comprobamos si la posición es posible en cada orientación y colocamos barco
            if 0<=(self.coordenadas[0][1]-self.tam_barco)<self.tamanio.shape[1] and self.orientacion == 'n':
                if BARCO_VIVO not in self.tamanio[self.coordenadas[0][0], (self.coordenadas[0][1] - self.tam_barco):self.coordenadas[0][1]]:
                    self.tamanio[self.coordenadas[0][0], self.coordenadas[0][1] - self.tam_barco:self.coordenadas[0][1]] = BARCO_VIVO
                    barco1 = Barco()
                    break
            elif 0<=(self.coordenadas[0][1]+self.tam_barco)<self.tamanio.shape[1] and self.orientacion == 's':
                if BARCO_VIVO not in self.tamanio[self.coordenadas[0][0], self.coordenadas[0][1]:(self.coordenadas[0][1] + self.tam_barco)]:
                    self.tamanio[self.coordenadas[0][0], self.coordenadas[0][1]:(self.coordenadas[0][1] + self.tam_barco)] = BARCO_VIVO
                    break
            elif 0<=(self.coordenadas[0][0]+self.tam_barco)<self.tamanio.shape[0] and self.orientacion == 'e':
                if BARCO_VIVO not in self.tamanio[self.coordenadas[0][0]:(self.coordenadas[0][0] + self.tam_barco), self.coordenadas[0][1]]:
                    self.tamanio[self.coordenadas[0][0]:(self.coordenadas[0][0] + self.tam_barco), self.coordenadas[0][1]] = BARCO_VIVO
                    break
            elif 0<=(self.coordenadas[0][0]-self.tam_barco)<self.tamanio.shape[0] and self.orientacion == 'o':
                if BARCO_VIVO not in self.tamanio[(self.coordenadas[0][0] - self.tam_barco):self.coordenadas[0][0], self.coordenadas[0][1]]:
                    self.tamanio[(self.coordenadas[0][0] - self.tam_barco):self.coordenadas[0][0], self.coordenadas[0][1]] = BARCO_VIVO
                    break

## FUNCIONES
def disparar(ataca, defiende, coordenadas = 'auto', dificultad = 1):
    if coordenadas == 'auto':
        while True:
            coordenadas = np.random.randint(defiende.tamanio.shape[0], size=(2,1))
            if defiende.tamanio[coordenadas[0], coordenadas[1]] != BARCO_TOCADO and defiende.tamanio[coordenadas[0], coordenadas[1]] != IMPACTO_AGUA:
                break

    if defiende.tamanio[coordenadas[0], coordenadas[1]] == AGUA:
        defiende.tamanio[coordenadas[0], coordenadas[1]] = IMPACTO_AGUA
        ataca.pantalla[coordenadas[0], coordenadas[1]] = IMPACTO_AGUA
        print('Has impactado en el agua')

    elif defiende.tamanio[coordenadas[0], coordenadas[1]] == BARCO_VIVO:
        defiende.tamanio[coordenadas[0], coordenadas[1]] = BARCO_TOCADO
        ataca.pantalla[coordenadas[0], coordenadas[1]] = BARCO_TOCADO
        print('¡Barco tocado!')


##TEST

#Creamos dos jugadores
j1 = Tablero(10)
j2 = Tablero(10)
print(j1.tamanio)

#Colocamos todos los barcos en cada tablero
for i in barcos:
    j2.coloca_barco(tam_barco=i)
for i in barcos:
    j1.coloca_barco(tam_barco=i)

#Imprimimos los dos tableros
print('Jugador 1\n', j1.tamanio)
print('Jugador 2\n', j2.tamanio)

#El jugador 1 dispara 5 veces al jugador 2
for i in range(5):
    disparar(j1, j2)

#Imprimimos tablero del jugador 2 y la pantalla del jugador 1
print(j2.tamanio)
print(j1.pantalla)


