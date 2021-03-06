from clases.Jugador import Jugador
from Constantes import *
from disparar import disparar
from clases.memoria_maquina import maquina_apunta_dispara


class Partida:
    def __init__(self, dificultad=1):
        self.jugadores = []
        self.dificultad = dificultad
        self.jugadores.append(Jugador())
        self.jugadores.append(Jugador())

    def imprimir_tableros_jugador(self):
        tablero_propio = self.jugadores[0].tablero_propio.devolver_tablero()
        tablero_ajeno = self.jugadores[0].tablero_ajeno.devolver_tablero()

        def borde_horizontal():
            # Imprime el borde horizontal
            for c in range(TAM_TABLERO):
                print('{:->4}'.format('-'), end='')
        def coord_horizontal():
            letra_columna = 97
            for c in range(TAM_TABLERO):
                if c == 0:
                    print('    ',end='')
                print('{:^3}'.format(chr(letra_columna+c).upper()), end='')

        # fin_linea para el segundo tablero
        def imprimir_matrices(t_propio, t_ajeno):
            for f in range(TAM_TABLERO):
                for i in range(2):
                    if i == 1:
                        print('    ', end='')
                    if f > 8:
                        print(f'{f + 1} |', end='')
                    else:
                        print(f'{f+1}  |', end='')
                    for c in range(TAM_TABLERO):
                        if i == 0:
                            print('{:^3}'.format(t_propio[f, c]), end='')
                        else:
                            print('{:^3}'.format(t_ajeno[f, c]), end='')
                    print('|', end='')
                print()

        borde_horizontal()
        borde_horizontal()
        print()

        coord_horizontal()
        print('     ', end='')
        coord_horizontal()
        print()

        imprimir_matrices(tablero_propio, tablero_ajeno)
        borde_horizontal()
        borde_horizontal()













    def nuevo_turno(self):
        def leer_teclado():
            while True:
                try:
                    entrada_teclado = input('Coordenadas objetivo: ')
                    # TODO mejorar tratamiento excepciones
                    columna, fila = (ord(entrada_teclado[0].lower())) - 97, int(entrada_teclado[1:]) - 1
                    if (len(entrada_teclado) not in [2, 3] or
                            not 0 <= fila < TAM_TABLERO or
                            not 0 <= columna < TAM_TABLERO):
                        #print('Ha fallado una condicion')
                        raise
                except:
                    print('''El formato de las coordenadas debe ser:)
                    Columnas A-J, filas 1-10, ej: A8
                    En el except''')
                else:
                    # Comienza el juego saliendo de leer teclado
                    break

            return columna, fila



        # juega j1, despues j2
        # TURNO J1
        #print('Turno de J1')
        # j1 juega hasta que falle

        # si no es automatico, que introduzca la coord de disparo
        #self.jugadores[0].tablero_propio.imprimir_tablero()
        #print()
        #self.jugadores[0].tablero_ajeno.imprimir_tablero()
        self.imprimir_tableros_jugador()

        columna, fila = leer_teclado()
        codigo, impacto = disparar(self.jugadores[0], self.jugadores[1], (columna, fila))
        #print('MOCK:')
        #columnaMOCK, filaMOCK = leer_teclado()
        #codigoMOCK, impacto = disparar(self.jugadores[1], self.jugadores[0], (columnaMOCK, filaMOCK))
        while codigo == 1:
            #self.jugadores[0].tablero_propio.imprimir_tablero()
            #print()
            #self.jugadores[0].tablero_ajeno.imprimir_tablero()
            self.imprimir_tableros_jugador()
            columna, fila = leer_teclado()
            codigo, impacto = disparar(self.jugadores[0], self.jugadores[1], (columna, fila))

        if codigo == 2:
            print('Enhorabuena J1, has ganado!, FIN de la partida')
            return 1


        # TURNO J2
        #print('Turno de J2')

        #print('Maquina disparando!')
        codigo, impacto = disparar(self.jugadores[1], self.jugadores[0])
        if self.dificultad == 1:
            while codigo == 1:
                codigo, _ = disparar(self.jugadores[1], self.jugadores[0])
        if self.dificultad >1 and codigo == 1:
            codigo = maquina_apunta_dispara(self.jugadores[1], self.jugadores[0], impacto)
        if codigo == 2:
            print('Enhorabuena J2, has ganado!, FIN de la partida')
            return 2

        # Dificultad 3, la maquina tiene 2 turnos
        if self.dificultad == 3:
            codigo, impacto = disparar(self.jugadores[1], self.jugadores[0])
            if self.dificultad == 1:
                while codigo == 1:
                    codigo, _ = disparar(self.jugadores[1], self.jugadores[0])
            if self.dificultad > 1 and codigo == 1:
                codigo = maquina_apunta_dispara(self.jugadores[1], self.jugadores[0], impacto)
            if codigo == 2:
                print('Enhorabuena J2, has ganado!, FIN de la partida')
                return 2

        return 0

    def jugar(self):
        for j in self.jugadores:
            j.preparar_tablero()
        print('Tableros preparados. Comienza la partida en dificultad ', self.dificultad)
        resultado = 0
        while not resultado:
            # contiene los distintos turnos
            resultado = self.nuevo_turno()
        else:
            if resultado == 1:
                print("""
                                                              
           ,--.          ,--.                   ,--.          
,--.  ,--. `--'  ,---. ,-'  '-.  ,---.  ,--.--. `--'  ,--,--. 
 \  `'  /  ,--. | .--' '-.  .-' | .-. | |  .--' ,--. ' ,-.  | 
  \    /   |  | \ `--.   |  |   ' '-' ' |  |    |  | \ '-'  | 
   `--'    `--'  `---'   `--'    `---'  `--'    `--'  `--`--' 
                                                             
                """)
            else:
                print("""
                                                                                 
,------.                                             ,--.            
|  .-.  \   ,---.  ,--.--. ,--.--. ,--.--.  ,---.  ,-'  '-.  ,--,--. 
|  |  \  : | .-. : |  .--' |  .--' |  .--' | .-. | '-.  .-' ' ,-.  | 
|  '--'  / \   --. |  |    |  |    |  |    ' '-' '   |  |   \ '-'  | 
`-------'   `----' `--'    `--'    `--'     `---'    `--'    `--`--' 
                                                                     
                """)


