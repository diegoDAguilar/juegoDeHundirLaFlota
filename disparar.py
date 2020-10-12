from Constantes import *
import numpy as np


def disparar(ataca, defiende, coordenadas = 'auto', ia = False, nivel = 1):
    """

    :param tablero: tablero al que dispara
    :param coordenada: coordenada elegida
    :param ia: if True la eleccion de coordenada es aleatoria
    :param nivel: TODO
    :return:
    """
    if coordenadas == 'auto':
        while True:
            y,x = np.random.randint(defiende.tablero_propio.matriz.shape[0], size=(2,1))
            if defiende.tablero_propio.matriz[x, y] != BARCO_TOCADO and\
                    defiende.tablero_propio.matriz[x, y] != IMPACTO_AGUA:
                break


    y, x = coordenadas

    if defiende.tablero_propio.matriz[x, y] == AGUA:
        defiende.tablero_propio.matriz[x, y] = IMPACTO_AGUA
        ataca.tablero_ajeno.matriz[x, y] = IMPACTO_AGUA
        print('Has impactado en el agua')

    elif defiende.tablero_propio.matriz[x, y] == BARCO_VIVO:
        defiende.tablero_propio.matriz[x, y] = BARCO_TOCADO
        ataca.tablero_ajeno.matriz[x, y] = BARCO_TOCADO
        print('¡Barco tocado!')
    else:
        print(f'Has disparado a un OVNI {defiende.tablero_propio.matriz[x, y]}')

    # TODO: no se como meter la parte de IA
    """
    if not ia:
        if tablero[x, y] == BARCO_VIVO:
            tablero[x, y] = BARCO_TOCADO
        elif tablero[x, y] == AGUA:
            tablero[x, y] = IMPACTO_AGUA
        else:
            pass
    """