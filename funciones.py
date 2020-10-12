from Constantes import *
from clases.Partida import Partida


def disparar(ataca, defiende, coordenada = 'auto', ia = False, nivel = 1):
    """

    :param tablero: tablero al que dispara
    :param coordenada: coordenada elegida
    :param ia: if True la eleccion de coordenada es aleatoria
    :param nivel: TODO
    :return:
    """
    if coordenadas == 'auto':
        while True:
            x, y = np.random.randint(defiende.tablero.matriz.shape[0], size=(2,1))
            if defiende.tablero.matriz[x, y] != BARCO_TOCADO and\
                    defiende.tablero.matriz[x, y] != IMPACTO_AGUA:
                break


    x, y = coordenada

    if defiende.tablero.matriz[x, y] == AGUA:
        defiende.tablero.matriz[x, y] = IMPACTO_AGUA
        ataca.visor.matriz[x, y] = IMPACTO_AGUA
        print('Has impactado en el agua')

    elif defiende.tablero.matriz[x, y] == BARCO_VIVO:
        defiende.tablero.matriz[x, y] = BARCO_TOCADO
        ataca.tablero.matriz[x, y] = BARCO_TOCADO
        print('¡Barco tocado!')

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

def empezar_partida():
    print("""
    BIENVENIDO A HUNDIR LA FLOTA
    ---------------------------------
    
          - JUGAR      PULSE 1 - 
          - CONFIGURAR PULSE 2 -
          - SALIR      PULSE 3 -  
    """)

    opcion = None
    while opcion not in ['1', '2', '3']:
        opcion = input()

    if opcion == '1':
        partida = Partida()
        partida.jugar()
    elif opcion == '2':
        while True:
            try:
                dificultad = int(input('Elija un nv de dificultad: 1 - 3\n'))
                if dificultad not in [1, 2, 3]:
                    raise
            # TODO aniadir tipo de excepcion
            except:
                print('Nivel de dificultad seleccionado no valido.')
            else:
                # dificultad bn seleccionada
                break
        partida = Partida()
        partida.jugar()
    # opcion 3
    else:
        print('HAS SALIDO DEL JUEGO')

