from Constantes import *
from clases.Partida import Partida
import numpy as np


def empezar_partida():
    print("""
,--.  ,--.                      ,--. ,--.             ,--.               ,---. ,--.           ,--.            
|  '--'  | ,--.,--. ,--,--,   ,-|  | `--' ,--.--.     |  |  ,--,--.     /  .-' |  |  ,---.  ,-'  '-.  ,--,--. 
|  .--.  | |  ||  | |      \ ' .-. | ,--. |  .--'     |  | ' ,-.  |     |  `-, |  | | .-. | '-.  .-' ' ,-.  | 
|  |  |  | '  ''  ' |  ||  | \ `-' | |  | |  |        |  | \ '-'  |     |  .-' |  | ' '-' '   |  |   \ '-'  | 
`--'  `--'  `----'  `--''--'  `---'  `--' `--'        `--'  `--`--'     `--'   `--'  `---'    `--'    `--`--'
    """)
    print("""
    
    ---------------------------------
    
          - PARTIDA FÁCIL      PULSE 1 - 
          - PARTIDA DIFÍCIL    PULSE 2 -
          - SALIR              PULSE 3 -  
    """)
    opcion = None
    while opcion not in ['1', '2', '3']:
        opcion = input()

    if opcion == '1':
        partida = Partida(dificultad=int(opcion))
        partida.jugar()
    elif opcion == '2':
        partida = Partida(dificultad=int(opcion))
        partida.jugar()
    # opcion 3
    else:
        print('HAS SALIDO DEL JUEGO')

