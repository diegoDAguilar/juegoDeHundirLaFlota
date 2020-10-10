from clases.Jugador import Jugador
from Constantes import *


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
        # juega j1, despues j2
        print('Es su turno, ¡dispare!')
        while True:
            try:
                entrada_teclado = input('Coordenadas objetivo: ')

                # TODO mejorar tratamiento excepciones
                fila, columna = int(entrada_teclado[0]) - 1, int(chr(ord(entrada_teclado[1].lower()) - 48)) - 1
                if (len(entrada_teclado) != 2 or
                        not 0 <= fila < TAM_TABLERO or
                        not 0 <= columna < TAM_TABLERO):
                    print('Ha fallado una condicion')
                    raise
            except:
                print('El formato de las coordenadas debe ser: 1A')
                print('En el except')
            else:
                print('Todo correcto')
            finally:
                # TODO por ahora sale del bucle dp del primer turno de J1
                break


    def jugar(self):
        print('Estas jugando')
        for j in self.jugadores:
            j.preparar_tablero()
        print('Tablero listo. Comienza la partida.')
        #while True:
        self.nuevo_turno()
        # contiene los distintos turnos
