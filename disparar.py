from Constantes import *
import numpy as np


def disparar(atacante, defensor, coordenadas='auto'):

    if coordenadas == 'auto':
        while True:
            columna, fila = np.random.randint(TAM_TABLERO), np.random.randint(TAM_TABLERO)
            if (atacante.tablero_ajeno.matriz[fila, columna] != BARCO_TOCADO and
                    atacante.tablero_ajeno.matriz[fila, columna] != IMPACTO_AGUA):
                # Sale porque tiene las nuevas coordenadas validas
                break
    else:
        fila, columna = coordenadas[0], coordenadas[1]

    # Asi se evitan comprobaciones en maquina overpower
    if not 0 <= columna < 9 and not 0 <= fila <= 9:
        return D_FALLASTE, (columna, fila)

    #print('Disparo (c,f):', (columna, fila))
    if defensor.get_coord_propia((fila, columna)) == AGUA:
        defensor.set_coord_propia((fila, columna), IMPACTO_AGUA)
        atacante.set_coord_ajena((fila, columna), IMPACTO_AGUA)
        print('Agua')
        return D_FALLASTE, (columna, fila)

    elif defensor.get_coord_propia((fila, columna)) == BARCO_VIVO:
        coordenadas_bordes = defensor.set_coord_propia((fila, columna), BARCO_TOCADO, True)
        atacante.set_coord_ajena((fila, columna), BARCO_TOCADO)
        # Si el barco se ha hundido marca las casillas vecinas
        # en el tablero atacante, en el defensor ya se han marcado
        #print('Coordenadas bordes son:', coordenadas_bordes)
        if coordenadas_bordes:
            for c, f in coordenadas_bordes:
                atacante.set_coord_ajena((f, c), IMPACTO_AGUA)
        print('Tocado')

        if defensor.he_perdido():
            return D_VICTORIA, (columna, fila)
        else:
            return D_ACERTASTE, (columna, fila)
    else:
        print('Has disparado a una coordenada rara')
        return D_FALLASTE, (columna, fila)
