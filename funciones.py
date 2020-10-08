from Constantes import *


def disparar(tablero, coordenada, ia = False, nivel = 1):
    """

    :param tablero: tablero al que dispara
    :param coordenada: coordenada elegida
    :param ia: if True la eleccion de coordenada es aleatoria
    :param nivel: TODO
    :return:
    """
    x, y = coordenada
    if not ia:
        if tablero[x, y] == BARCO_VIVO:
            tablero[x, y] = BARCO_TOCADO
        elif tablero[x, y] == AGUA:
            tablero[x, y] = IMPACTO_AGUA
        else:
            pass
