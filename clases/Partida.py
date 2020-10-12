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
        # juega j1, despues j2
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
                print('El formato de las coordenadas debe ser:')
                print('Columnas A-J, filas 1-10, ej: A8')
                print('En el except')
            else:
                print('Todo correcto')
                disparar(self.jugadores[0], self.jugadores[1], (columna, fila), False, 1)
            #finally:
                # TODO por ahora sale del bucle dp del primer turno de J1
                #break


    def jugar(self):
        print('Estas jugando')
        for j in self.jugadores:
            j.preparar_tablero()
        print('Tablero listo. Comienza la partida.')
        #while True:
        self.nuevo_turno()
        # contiene los distintos turnos
