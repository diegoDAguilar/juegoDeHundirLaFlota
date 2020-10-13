from clases.Jugador import Jugador
from Constantes import *
from disparar import disparar


class Partida:
    def __init__(self, j1='humano', j2='auto', dificultad=1):
        self.jugadores = []
        self.dificultad = dificultad

        for j in [j1, j2]:
            if j == 'humano':
                self.jugadores.append(Jugador())
            elif j == 'auto':
                self.jugadores.append(Jugador(dificultad))

    def imprimir_todo(self):
        "Imprime todos los tableros"
        # TODO
        pass


    def nuevo_turno(self):
        def leer_teclado():
            print('Es su turno, ¡dispare!')
            while True:
                try:
                    entrada_teclado = input('Coordenadas objetivo: ')
                    # TODO mejorar tratamiento excepciones
                    columna, fila = int(chr(ord(entrada_teclado[0].lower()) - 48)) - 1, int(entrada_teclado[1:]) - 1
                    if (len(entrada_teclado) not in [2, 3] or
                            not 0 <= fila < TAM_TABLERO or
                            not 0 <= columna < TAM_TABLERO):
                        print('Ha fallado una condicion')
                        raise
                except:
                    print('''El formato de las coordenadas debe ser:)
                    Columnas A-J, filas 1-10, ej: A8
                    En el except''')
                else:
                    break
                    print('Todo correcto')

            return columna, fila



        # juega j1, despues j2
        # TURNO J1
        print('Turno de J1')
        # j1 juega hasta que falle
        if self.jugadores[0].auto:
            print('Maquina disparando!')
            while disparar(self.jugadores[0], self.jugadores[1]):
                print('Maquina sigue disparando!!')
                pass
        # si no es automatico, que introduzca la coord de disparo
        else:
            print('Jugador disparando!')
            #print(self.jugadores[0].tablero_propio.devolver_tablero(),
            #      self.jugadores[1].tablero_propio.devolver_tablero())
            print(self.jugadores[0].tablero_propio.devolver_tablero())
            print(self.jugadores[0].tablero_ajeno.devolver_tablero())
            print('-----------')
            print('Tablero maquina')
            print(self.jugadores[1].tablero_propio.devolver_tablero())

            columna, fila = leer_teclado()
            while disparar(self.jugadores[0], self.jugadores[1], (columna, fila), False, 1):
                print('Jugador sigue disparando!')
                print(self.jugadores[0].tablero_propio.devolver_tablero())
                print('-----------')
                print(self.jugadores[1].tablero_propio.devolver_tablero())
                columna, fila = leer_teclado()
                pass


        # TURNO J2
        print('Turno de J2')
        if self.jugadores[1].auto:
            print('Maquina disparando!')
            while disparar(self.jugadores[1], self.jugadores[0]):
                print('Maquina sigue disparando!')
        # si no es automatico, que introduzca la coord de disparo
        else:
            print(self.jugadores[0].tablero_propio.devolver_tablero(),
                  self.jugadores[1].tablero_propio.devolver_tablero())
            columna, fila = leer_teclado()
            while disparar(self.jugadores[1], self.jugadores[0], (columna, fila), False, 1):
                print(self.jugadores[0].tablero_propio.devolver_tablero(),
                      self.jugadores[1].tablero_propio.devolver_tablero())
                columna, fila = leer_teclado()

    def jugar(self):
        print('Estas jugando')
        for j in self.jugadores:
            j.preparar_tablero()
        print('Tablero listo. Comienza la partida.')
        while True:
            self.nuevo_turno()
        # contiene los distintos turnos
