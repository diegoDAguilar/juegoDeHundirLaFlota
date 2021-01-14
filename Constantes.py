BARCO_VIVO = 'O'
BARCO_TOCADO = 'X'
AGUA = ' '
IMPACTO_AGUA = '-'
# CODIGO PARA RODEAR EL BARCO
BARCO_HUNDIDO = 'H'

TAM_TABLERO = 10
TAMANIOS_BARCOS = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

# CODIGOS FUNCION DISPARAR
D_FALLASTE = 0
D_ACERTASTE = 1
D_VICTORIA = 2

# CODIGOS FIN PARTIDA
PARTIDA_CONTINUA = 0
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

DIFICULTADES = ['1', '2']
SALIR_JUEGO = ['3']

# Mensajes

MSG_OPCION_ERRONEA = 'Opción no válida'
MSG_SALIR_DEL_JUEGO = 'HAS SALIDO DEL JUEGO'
MSG_MENU_DIFICULTADES = """
    
    --------------------------------------------------------------------------------------------------------------
    
                              - JUGAR: DIFICULTAD NORMAL        PULSE 1 -
                              - JUGAR: DIFICULTAD IA TRAMPAS    PULSE 2 -
                              - SALIR                           PULSE 3 -  
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