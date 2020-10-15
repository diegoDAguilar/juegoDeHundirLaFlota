from clases.Jugador import Jugador
from Constantes import *
from disparar import disparar
from clases.maquina_overpower import maquina_apunta_dispara


class Partida:
    def __init__(self, dificultad=1):
        self.jugadores = []
        self.dificultad = dificultad
        self.jugadores.append(Jugador())
        self.jugadores.append(Jugador())



    def nuevo_turno(self):
        def leer_teclado():
            #print('Es su turno, ¡dispare!')
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
        self.jugadores[0].tablero_propio.imprimir_tablero()
        print()
        self.jugadores[0].tablero_ajeno.imprimir_tablero()

        columna, fila = leer_teclado()
        codigo, impacto = disparar(self.jugadores[0], self.jugadores[1], (columna, fila))
        #print('MOCK:')
        #columnaMOCK, filaMOCK = leer_teclado()
        #codigoMOCK, impacto = disparar(self.jugadores[1], self.jugadores[0], (columnaMOCK, filaMOCK))
        while codigo == 1:
            #print('Jugador sigue disparando!')
            self.jugadores[0].tablero_propio.imprimir_tablero()
            # print(self.jugadores[0].tablero_propio.devolver_tablero())
            print('---')
            self.jugadores[0].tablero_ajeno.imprimir_tablero()
            print('-----------')
            columna, fila = leer_teclado()
            codigo, impacto = disparar(self.jugadores[0], self.jugadores[1], (columna, fila))

            pass
        if codigo == 2:
            print('Enhorabuena J1, has ganado!, FIN de la partida')
            return 0


        # TURNO J2
        #print('Turno de J2')

        #print('Maquina disparando!')
        codigo, impacto = disparar(self.jugadores[1], self.jugadores[0])
        if self.dificultad == 1:
            #print('dif1 ', self.dificultad)
            while codigo == 1:
                codigo, _ = disparar(self.jugadores[1], self.jugadores[0])
        if self.dificultad == 2:
            #print('dif2 ', self.dificultad)
            codigo, impacto = maquina_apunta_dispara(self.jugadores[1], self.jugadores[0], impacto)
        if codigo == 2:
            print('Enhorabuena J2, has ganado!, FIN de la partida')
            return 0

        return 1

    def jugar(self):
        print('Estas jugando')
        for j in self.jugadores:
            j.preparar_tablero()
        print('Tablero listo. Comienza la partida en dificultad ', self.dificultad)
        while self.nuevo_turno():
            # contiene los distintos turnos
            pass
