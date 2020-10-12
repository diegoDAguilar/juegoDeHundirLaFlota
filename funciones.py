from Constantes import *
from clases.Partida import Partida
import numpy as np





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

