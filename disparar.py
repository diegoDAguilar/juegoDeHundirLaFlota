from Constantes import *
import numpy as np


def disparar(ataca, defiende, coordenadas='auto'):

    if coordenadas == 'auto':
        while True:
            columna, fila = np.random.randint(TAM_TABLERO), np.random.randint(TAM_TABLERO)
            if (ataca.tablero_ajeno.matriz[fila, columna] != BARCO_TOCADO and
                    ataca.tablero_ajeno.matriz[fila, columna] != IMPACTO_AGUA):
                # Sale porque tiene las nuevas coordenadas validas
                #print('disparo rnd')
                break
    else:
        columna, fila = coordenadas[0], coordenadas[1]

    # Asi se evitan comprobaciones en maquina overpower
    if not 0<=columna<9 and not 0<=fila<=9:
        return D_FALLASTE, (columna, fila)

    #print('Disparo (c,f):', (columna, fila))
    if defiende.tablero_propio.get_coordenada((columna, fila)) == AGUA:
        defiende.tablero_propio.set_coordenada((columna, fila), IMPACTO_AGUA)
        ataca.tablero_ajeno.set_coordenada((columna, fila), IMPACTO_AGUA)
        print('Agua')
        return D_FALLASTE, (columna, fila)

    elif defiende.tablero_propio.get_coordenada((columna, fila)) == BARCO_VIVO:
        coordenadas_bordes = defiende.tablero_propio.set_coordenada((columna, fila), BARCO_TOCADO, True)
        ataca.tablero_ajeno.set_coordenada((columna, fila), BARCO_TOCADO)
        # Si el barco se ha hundido marca las casillas vecinas
        # en el tablero atacante, en el defensor ya se han marcado
        #print('Coordenadas bordes son:', coordenadas_bordes)
        if coordenadas_bordes:
            for c, f in coordenadas_bordes:
                ataca.tablero_ajeno.set_coordenada((c, f), IMPACTO_AGUA)
        print('Tocado')

        if defiende.he_perdido():
            return D_VICTORIA, (columna, fila)
        else:
            return D_ACERTASTE, (columna, fila)
    else:
        print('Has disparado a una coordenada rara')
        return D_FALLASTE, (columna, fila)
