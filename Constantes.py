BARCO_VIVO = 'O'
BARCO_TOCADO = 'X'
AGUA = ' '
IMPACTO_AGUA = '-'
TAM_TABLERO = 10
TAMANIOS_BARCOS = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

# CODIGOS FUNCION DISPARAR
D_FALLASTE = 0
D_ACERTASTE = 1
D_VICTORIA = 2

# CODIGOS FIN PARTIDA
FIN_VICTORIA = 1
FIN_DERROTA = 2

# CODIGOS CAMBIO DE COORDENADAS
ORIENTACION_OFFSET = {
    'n': (-1, 0),
    's': (1, 0),
    'e': (0, 1),
    'w': (0, -1),
}

# Dificultades

DIFICULTADES = ['1', '2', '3']
SALIR_JUEGO = ['4']

# Mensajes

MSG_OPCION_ERRONEA = 'Opción no válida'
MSG_SALIR_DEL_JUEGO = 'HAS SALIDO DEL JUEGO'
MSG_MENU_DIFICULTADES = """
    
    --------------------------------------------------------------------------------------------------------------
    
          - PARTIDA FACIL      PULSE 1 - 
          - PARTIDA NORMAL     PULSE 2 -
          - PARTIDA DIFICIL    PULSE 3 -
          - SALIR              PULSE 4 -  
    """
MSG_LOGO = """
,--.  ,--.                      ,--. ,--.             ,--.               ,---. ,--.           ,--.            
|  '--'  | ,--.,--. ,--,--,   ,-|  | `--' ,--.--.     |  |  ,--,--.     /  .-' |  |  ,---.  ,-'  '-.  ,--,--. 
|  .--.  | |  ||  | |      \ ' .-. | ,--. |  .--'     |  | ' ,-.  |     |  `-, |  | | .-. | '-.  .-' ' ,-.  | 
|  |  |  | '  ''  ' |  ||  | \ `-' | |  | |  |        |  | \ '-'  |     |  .-' |  | ' '-' '   |  |   \ '-'  | 
`--'  `--'  `----'  `--''--'  `---'  `--' `--'        `--'  `--`--'     `--'   `--'  `---'    `--'    `--`--'
    """
MSG_DERROTA = """
                                                                                 
,------.                                             ,--.            
|  .-.  \   ,---.  ,--.--. ,--.--. ,--.--.  ,---.  ,-'  '-.  ,--,--. 
|  |  \  : | .-. : |  .--' |  .--' |  .--' | .-. | '-.  .-' ' ,-.  | 
|  '--'  / \   --. |  |    |  |    |  |    ' '-' '   |  |   \ '-'  | 
`-------'   `----' `--'    `--'    `--'     `---'    `--'    `--`--' 
                                                                     
                """
MSG_VICTORIA = """
                                                              
           ,--.          ,--.                   ,--.          
,--.  ,--. `--'  ,---. ,-'  '-.  ,---.  ,--.--. `--'  ,--,--. 
 \  `'  /  ,--. | .--' '-.  .-' | .-. | |  .--' ,--. ' ,-.  | 
  \    /   |  | \ `--.   |  |   ' '-' ' |  |    |  | \ '-'  | 
   `--'    `--'  `---'   `--'    `---'  `--'    `--'  `--`--' 
                                                             
                """