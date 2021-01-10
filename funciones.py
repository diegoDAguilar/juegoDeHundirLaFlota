from clases.Partida import Partida
from Constantes import *


def menu_dificultades():
    """
    Muestra el menu con las dificultades.
    El usuario selecciona la dificultad o sale del juego.
    :return: partida.jugar()
    """
    print(MSG_LOGO)
    print(MSG_MENU_DIFICULTADES)
    opcion_seleccionada = input()

    while opcion_seleccionada not in DIFICULTADES and opcion_seleccionada not in SALIR_JUEGO:
        print(f'opcion_seleccionada {opcion_seleccionada} of type {type(opcion_seleccionada)}')
        print(MSG_OPCION_ERRONEA)
        opcion_seleccionada = input()
        if opcion_seleccionada in SALIR_JUEGO:
            print(MSG_SALIR_DEL_JUEGO)
            break
    else:
        if opcion_seleccionada in SALIR_JUEGO:
            print(MSG_SALIR_DEL_JUEGO)
        else:
            partida = Partida(dificultad=int(opcion_seleccionada))
            partida.empezar_y_jugar()
