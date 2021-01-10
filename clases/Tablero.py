from Constantes import *
from clases.Barco import Barco
import numpy as np


class Tablero:

    def __init__(self, propio, tamanio=TAM_TABLERO):
        self.matriz = np.full((tamanio, tamanio), AGUA)
        self.lista_barcos = []
        if propio:
            self.colocar_todos_barcos()

    def get_barcos(self):
        """Devuelve la lista con los barcos"""
        return self.lista_barcos

    def get_coordenada(self, coordenada):
        """Devuelve el valor en unas coordenadas"""
        c = coordenada[0]
        f = coordenada[1]
        return self.matriz[f, c]

    def set_coordenada(self, coordenada, valor, bordes=False):

        def coordenada_vecina():
            # print('Comprobando vecinos')
            np_fc = np.array([celda_c, celda_f])
            np_fc2 = np.array([c2, f2])
            resta_vecinos = np.array(([1, 0],
                                      [0, 1],
                                      [-1, 0],
                                      [0, -1],
                                      [1, 1],
                                      [-1, -1],
                                      [-1, 1],
                                      [1, -1]))
            # print(np_fc - np_fc2)
            if list(np_fc - np_fc2) in resta_vecinos.tolist():
                # print('True')
                return True
            else:
                # print('False')
                return False

        c = coordenada[0]
        f = coordenada[1]
        coordenadas_bordes = list()
        self.matriz[f, c] = valor
        # TODO, no lo hace para cada coordenada del hundido
        # Si toca un barco, busca entre los barcos
        # del tablero aquel con esas coordenadas
        # y lo golpea
        if valor == BARCO_TOCADO:
            for b in self.get_barcos():
                if coordenada in b.get_coordenadas():
                    b.golpear_barco((c, f))
                    # Si el barco esta muerto lo rodea
                    # con agua tocado
                    if not b.estoy_vivo():
                        print('Barco hundido')
                        # Bordea cada celda del barco
                        if bordes:
                            for celda in b.get_coordenadas():
                                celda_c, celda_f = celda[0], celda[1]
                                for f2 in range(TAM_TABLERO):
                                    for c2 in range(TAM_TABLERO):
                                        # print('coordenada: ', self.matriz[f2, c2])
                                        if coordenada_vecina() and self.matriz[f2, c2] == AGUA:
                                            # Las coordenadas aqui se pintan en el tablero defensor
                                            # porque ahi es donde estan los barcos, pero despues se
                                            # tienen que enviar para que las pinte el otro tablero
                                            self.matriz[f2, c2] = IMPACTO_AGUA
                                            coordenadas_bordes.append((c2, f2))
                        return coordenadas_bordes

    def colocar_barco(self, tam_barco='auto', coordenadas='auto',
                      orientacion='auto'):

        orientaciones = ['n', 's', 'e', 'w']

        # Si los parámetros están en auto, los genera, sino coge los definidos
        if orientacion == 'auto':
            orientacion = orientaciones[np.random.randint(4)]

        if coordenadas == 'auto':
            # Coordenadas columna, fila
            coordenadas = (np.random.randint(TAM_TABLERO), np.random.randint(TAM_TABLERO))
        else:
            coordenadas = np.array([coordenadas])

        while True:
            # Variables del tablero
            # x es el segundo elemento, y es el primero
            columna = coordenadas[0]
            fila = coordenadas[1]
            x_limit = TAM_TABLERO
            y_limit = TAM_TABLERO

            # Comprobamos si la posición es posible en cada orientación,
            # después comprobamos que en las coordenadas no hay barcos
            # y colocamos el nuestro

            if (0 <= fila - tam_barco) and (orientacion == 'n'):
                if BARCO_VIVO not in self.matriz[fila - tam_barco:fila, columna]:
                    l_coordenadas = Tablero.rellenar_coordenadas(columna, fila, tam_barco, orientacion)
                    if Tablero.barco_aislado(l_coordenadas, self.matriz) == True:
                        for c, f in l_coordenadas:
                            self.matriz[f, c] = BARCO_VIVO

                        # Añadimos barco
                        # print('Creando barco')
                        # print(l_coordenadas)
                        # print('orientacion:', orientacion)

                        self.lista_barcos.append(Barco(l_coordenadas))
                        # print('Barco creado')
                        break

            elif (fila + tam_barco < x_limit) and (orientacion == 's'):
                if BARCO_VIVO not in self.matriz[fila:fila + tam_barco, columna]:
                    l_coordenadas = Tablero.rellenar_coordenadas(columna, fila, tam_barco, orientacion)
                    if Tablero.barco_aislado(l_coordenadas, self.matriz) == True:
                        for c, f in l_coordenadas:
                            self.matriz[f, c] = BARCO_VIVO

                        # Añadimos barco
                        # print('Creando barco')
                        # print(l_coordenadas)
                        # print('orientacion:', orientacion)

                        self.lista_barcos.append(Barco(l_coordenadas))
                        # print('Barco creado')
                        break

            elif (columna + tam_barco < y_limit) and (orientacion == 'e'):
                if BARCO_VIVO not in self.matriz[fila, columna:columna + tam_barco]:
                    l_coordenadas = Tablero.rellenar_coordenadas(columna, fila, tam_barco, orientacion)
                    if Tablero.barco_aislado(l_coordenadas, self.matriz) == True:
                        for c, f in l_coordenadas:
                            self.matriz[f, c] = BARCO_VIVO

                        # Añadimos barco
                        # print('Creando barco')
                        # print(l_coordenadas)
                        # print('orientacion:', orientacion)

                        self.lista_barcos.append(Barco(l_coordenadas))
                        # print('Barco creado')
                        break

            elif (0 <= columna - tam_barco) and (orientacion == 'w'):
                if BARCO_VIVO not in self.matriz[fila, columna - tam_barco:columna]:
                    l_coordenadas = Tablero.rellenar_coordenadas(columna, fila, tam_barco, orientacion)
                    if Tablero.barco_aislado(l_coordenadas, self.matriz) == True:
                        for c, f in l_coordenadas:
                            self.matriz[f, c] = BARCO_VIVO

                        # Añadimos barco
                        # print('Creando barco')
                        # print(l_coordenadas)
                        # print('orientacion:', orientacion)

                        self.lista_barcos.append(Barco(l_coordenadas))
                        # print('Barco creado')
                        break

            # Si las coordenadas no son válidas,
            # generamos unas nuevas y repetimos el proceso

            orientacion = orientaciones[np.random.randint(4)]
            coordenadas = (np.random.randint(TAM_TABLERO), np.random.randint(TAM_TABLERO))

        return True

    @staticmethod
    def rellenar_coordenadas(columna, fila, tam_barco, orientacion):
        coordenadas = []
        if orientacion == 'n':
            for i in range(tam_barco):
                coordenadas.append((columna, fila - i))
        elif orientacion == 's':
            for i in range(tam_barco):
                coordenadas.append((columna, fila + i))
        elif orientacion == 'e':
            for i in range(tam_barco):
                coordenadas.append((columna + i, fila))
        elif orientacion == 'w':
            for i in range(tam_barco):
                coordenadas.append((columna - i, fila))

        return coordenadas

    @staticmethod
    def barco_aislado(coors, tablero):

        for c, f in coors:
            # Comienza el churro: si funciona perfecto, nadie lo mira x dentro
            if c == 0:
                if f == 0:
                    if (tablero[f, c + 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c] == BARCO_VIVO) or \
                            (tablero[f + 1, c + 1] == BARCO_VIVO):
                        return False

                elif f == 9:
                    if (tablero[f - 1, c] == BARCO_VIVO) or \
                            (tablero[f - 1, c + 1] == BARCO_VIVO) or \
                            (tablero[f, c + 1] == BARCO_VIVO):
                        return False

                else:
                    if (tablero[f - 1, c] == BARCO_VIVO) or \
                            (tablero[f - 1, c + 1] == BARCO_VIVO) or \
                            (tablero[f, c + 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c] == BARCO_VIVO) or \
                            (tablero[f + 1, c + 1] == BARCO_VIVO):
                        return False

            elif c == 9:
                if f == 0:
                    if (tablero[f, c - 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c - 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c] == BARCO_VIVO):
                        return False

                elif f == 9:
                    if (tablero[f - 1, c - 1] == BARCO_VIVO) or \
                            (tablero[f - 1, c] == BARCO_VIVO) or \
                            (tablero[f, c - 1] == BARCO_VIVO):
                        return False

                else:
                    if (tablero[f - 1, c - 1] == BARCO_VIVO) or \
                            (tablero[f - 1, c] == BARCO_VIVO) or \
                            (tablero[f, c - 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c - 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c] == BARCO_VIVO):
                        return False

            elif c != 0 or c != 9:
                if f == 0:
                    if (tablero[f, c - 1] == BARCO_VIVO) or \
                            (tablero[f, c + 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c - 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c] == BARCO_VIVO) or \
                            (tablero[f + 1, c + 1] == BARCO_VIVO):
                        return False

                elif f == 9:
                    if (tablero[f - 1, c - 1] == BARCO_VIVO) or \
                            (tablero[f - 1, c] == BARCO_VIVO) or \
                            (tablero[f - 1, c + 1] == BARCO_VIVO) or \
                            (tablero[f, c - 1] == BARCO_VIVO) or \
                            (tablero[f, c + 1] == BARCO_VIVO):
                        return False
                else:
                    if (tablero[f - 1, c - 1] == BARCO_VIVO) or \
                            (tablero[f - 1, c] == BARCO_VIVO) or \
                            (tablero[f - 1, c + 1] == BARCO_VIVO) or \
                            (tablero[f, c - 1] == BARCO_VIVO) or \
                            (tablero[f, c + 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c - 1] == BARCO_VIVO) or \
                            (tablero[f + 1, c] == BARCO_VIVO) or \
                            (tablero[f + 1, c + 1] == BARCO_VIVO):
                        return False

        else:
            return True

    def colocar_todos_barcos(self):
        for t in TAMANIOS_BARCOS:
            self.colocar_barco(t)

    def devolver_tablero(self):
        return self.matriz

    def imprimir_tablero(self):
        def borde_horizontal():
            # Imprime el borde horizontal
            for c in range(TAM_TABLERO):
                print('{:->4}'.format('-'), end='')
            print()

        letra_columna = 97
        for c in range(TAM_TABLERO):
            if c == 0:
                print('    ', end='')
            print('{:^3}'.format(chr(letra_columna + c).upper()), end='')
        print()

        borde_horizontal()
        for f in range(TAM_TABLERO):
            if f > 8:
                print(f'{f + 1} |', end='')
            else:
                print(f'{f + 1}  |', end='')
            for c in range(TAM_TABLERO):
                print('{:^3}'.format(self.matriz[f, c]), end='')
            print('|')
        borde_horizontal()
