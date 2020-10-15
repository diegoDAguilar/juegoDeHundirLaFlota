from clases.Partida import Partida

def empezar_partida():
    print("""
,--.  ,--.                      ,--. ,--.             ,--.               ,---. ,--.           ,--.            
|  '--'  | ,--.,--. ,--,--,   ,-|  | `--' ,--.--.     |  |  ,--,--.     /  .-' |  |  ,---.  ,-'  '-.  ,--,--. 
|  .--.  | |  ||  | |      \ ' .-. | ,--. |  .--'     |  | ' ,-.  |     |  `-, |  | | .-. | '-.  .-' ' ,-.  | 
|  |  |  | '  ''  ' |  ||  | \ `-' | |  | |  |        |  | \ '-'  |     |  .-' |  | ' '-' '   |  |   \ '-'  | 
`--'  `--'  `----'  `--''--'  `---'  `--' `--'        `--'  `--`--'     `--'   `--'  `---'    `--'    `--`--'
    """)
    print("""
    
    --------------------------------------------------------------------------------------------------------------
    
          - PARTIDA FACIL      PULSE 1 - 
          - PARTIDA NORMAL     PULSE 2 -
          - PARTIDA DIFICIL    PULSE 3 -
          - SALIR              PULSE 4 -  
    """)
    opcion = None
    while opcion not in ['1', '2', '3', '4']:
        opcion = input()

    if opcion == '1':
        partida = Partida(dificultad=int(opcion))
        partida.jugar()
    elif opcion == '2':
        partida = Partida(dificultad=int(opcion))
        partida.jugar()
    elif opcion == '3':
        partida = Partida(dificultad=int(opcion))
        partida.jugar()
    # opcion 3
    else:
        print('HAS SALIDO DEL JUEGO')

