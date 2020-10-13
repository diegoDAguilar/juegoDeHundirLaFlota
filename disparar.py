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
            columna, fila = np.random.randint(TAM_TABLERO), np.random.randint(TAM_TABLERO)
            if defiende.tablero_propio.matriz[fila, columna] != BARCO_TOCADO and\
                    defiende.tablero_propio.matriz[fila, columna] != IMPACTO_AGUA:
                break
    else:
         fila,columna = coordenadas

   # if defiende.tablero_propio.matriz[fila, columna] == AGUA:
    #    defiende.tablero_propio.matriz[fila, columna] = IMPACTO_AGUA
     #   ataca.tablero_ajeno.matriz[fila, columna] = IMPACTO_AGUA
      #  print('Has impactado en el agua')
       # return D_FALLASTE
    if defiende.tablero_propio.get_coordenada((fila, columna)) == AGUA:
        defiende.tablero_propio.set_coordenada((fila, columna), IMPACTO_AGUA)
        ataca.tablero_ajeno.set_coordenada((fila, columna), IMPACTO_AGUA)
        print('Has impactado en el agua')
        return D_FALLASTE

    #elif defiende.tablero_propio.matriz[fila, columna] == BARCO_VIVO:
     #   defiende.tablero_propio.matriz[fila, columna] = BARCO_TOCADO
      #  ataca.tablero_ajeno.matriz[fila, columna] = BARCO_TOCADO
       # print('¡Barco tocado!')
    elif defiende.tablero_propio.get_coordenada((fila, columna)) == BARCO_VIVO:
        defiende.tablero_propio.set_coordenada((fila, columna), BARCO_TOCADO)
        ataca.tablero_ajeno.set_coordenada((fila, columna), BARCO_TOCADO)
        print('¡Barco tocado!')

        if defiende.he_perdido():
            return D_VICTORIA
        else:
            return D_ACERTASTE
    else:
        print(f'Has disparado a un OVNI {defiende.tablero_propio.matriz[fila, columna]}')

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