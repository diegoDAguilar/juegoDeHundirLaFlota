from Constantes import *
from clases.Barco import Barco
import numpy as np
import logging


class Tablero:

    def __init__(self, propio, tamanio=TAM_TABLERO):
        self.matriz = np.full((tamanio, tamanio), AGUA)
        self.lista_barcos = []
        if propio:
            self.colocar_todos_barcos()
        logging.basicConfig(level=logging.INFO)
        logging.info('Objeto Tablero creado')

    def get_barcos(self):
        """Devuelve la lista con los barcos"""
        return self.lista_barcos

    def get_coordenada(self, coordenada):
        """Devuelve el valor en unas coordenadas (fila, columna)"""
        return self.matriz[coordenada]

    def set_coordenada(self, coordenada, valor):

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

        coordenadas_bordes = list()
        self.matriz[coordenada] = valor
        # Si toca un barco, busca entre los barcos
        # del tablero aquel con esas coordenadas
        # y lo golpea
        if valor == BARCO_TOCADO:
            for b in self.get_barcos():
                if coordenada in b.get_coordenadas():
                    b.golpear_barco(coordenada)
                    # Si el barco esta muerto lo rodea
                    # con agua tocado
                    if not b.estoy_vivo():
                        print('Barco hundido')
                        # Bordea cada celda del barco
                        for celda_barco in b.get_coordenadas():
                            celda_f, celda_c = celda_barco
                            for f2 in range(TAM_TABLERO):
                                for c2 in range(TAM_TABLERO):
                                    # print('coordenada: ', self.matriz[f2, c2])
                                    if coordenada_vecina() and self.matriz[f2, c2] == AGUA:
                                        # Las coordenadas aqui se pintan en el tablero defensor
                                        # porque ahi es donde estan los barcos, pero despues se
                                        # tienen que enviar para que las pinte el otro tablero
                                        #self.matriz[f2, c2] = IMPACTO_AGUA
                                        coordenadas_bordes.append((f2, c2))
                        return BARCO_HUNDIDO, coordenadas_bordes
        return valor, list()

        # Devueve el valor del disparo o BARCO_HUNDIDO
        return valor

    def colocar_barco(self, tam_barco, coordenadas='auto',
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

            # Se comprueba que entra el barco
            if Tablero.entra_barco(coordenadas, tam_barco, orientacion):
                l_coordenadas = Tablero.calcular_coordenadas_barco(coordenadas, tam_barco, orientacion)
                # Se comprueba que esta aislado
                if self.barco_aislado(l_coordenadas):
                    # Se coloca
                    for f, c in l_coordenadas:
                        self.matriz[f, c] = BARCO_VIVO
                    else:
                        # Se crea el barco
                        self.lista_barcos.append(Barco(l_coordenadas))
                        logging.info(f'Barco colocado en {l_coordenadas}')
                        # print('Barco colocado')
                        return

            # Si las coordenadas no son válidas,
            # generamos unas nuevas y repetimos el proceso
            orientacion = orientaciones[np.random.randint(4)]
            coordenadas = (np.random.randint(TAM_TABLERO), np.random.randint(TAM_TABLERO))

    @staticmethod
    def entra_barco(coordenada_origen, tam_barco, orientacion):
        coord = coordenada_origen
        for idx in range(tam_barco):
            f, c = np.array(coord) + idx * np.array(ORIENTACION_OFFSET[orientacion])
            if (TAM_TABLERO > f >= 0) and (TAM_TABLERO > c >= 0):
                # print('Entra:', f, c)
                pass
            else:
                return False
        else:
            # logging.info(f'Barco completo comienza en {str(coordenada_origen)}, ori: {orientacion}, tam {tam_barco}')
            return True

    @staticmethod
    def calcular_coordenadas_barco(coordenadas, tam_barco, orientacion):
        lista_coordenadas = list()
        coord_actual = np.array(coordenadas)

        assert coordenadas[0] >= 0
        assert coordenadas[1] >= 0

        for _ in range(tam_barco):
            lista_coordenadas.append(coord_actual)
            coord_actual = coord_actual + np.array(ORIENTACION_OFFSET[orientacion])
            # [array([[2, 8]])]
        return lista_coordenadas

    def barco_aislado(self, coord):
        for f, c in coord:
            coord_vecinas = [
                (f, c),
                (f - 1, c - 1),
                (f - 1, c),
                (f - 1, c + 1),
                (f, c - 1),
                (f, c + 1),
                (f + 1, c - 1),
                (f + 1, c),
                (f + 1, c + 1),
            ]
            for fv, cv in coord_vecinas:
                # If it is inside of the board
                if (0 <= fv < TAM_TABLERO) and (0 <= cv < TAM_TABLERO) and (self.matriz[fv, cv] == BARCO_VIVO):
                    return False

        else:
            return True

    def colocar_todos_barcos(self):
        for t in TAMANIOS_BARCOS:
            self.colocar_barco(t)

    def get_tablero(self):
        return self.matriz
