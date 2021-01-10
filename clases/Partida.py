from clases.Jugador import Jugador
from Constantes import *
from disparar import disparar
from clases.memoria_maquina import maquina_apunta_dispara


class Partida:

    def __init__(self, dificultad):
        self.jugadores = [
            Jugador(),
            Jugador(),
        ]
        self.dificultad = dificultad

    def manejar_turno(self):
        def leer_teclado():
            while True:
                try:
                    entrada_teclado = input('Coordenadas objetivo: ')
                    # TODO mejorar tratamiento excepciones
                    columna, fila = (ord(entrada_teclado[0].lower())) - 97, int(entrada_teclado[1:]) - 1
                    if (len(entrada_teclado) not in [2, 3] or
                            not 0 <= fila < TAM_TABLERO or
                            not 0 <= columna < TAM_TABLERO):
                        # print('Ha fallado una condicion')
                        raise
                except:
                    print('''El formato de las coordenadas debe ser:)
                    Columnas A-J, filas 1-10, ej: A8
                    En el except''')
                else:
                    # Comienza el juego saliendo de leer teclado
                    break

            return columna, fila

        self.jugadores[0].imprimir_tableros()

        columna, fila = leer_teclado()
        codigo, impacto = disparar(self.jugadores[0], self.jugadores[1], (columna, fila))
        while codigo == 1:
            self.jugadores[0].imprimir_tableros()
            columna, fila = leer_teclado()
            codigo, impacto = disparar(self.jugadores[0], self.jugadores[1], (columna, fila))

        if codigo == 2:
            print('Enhorabuena J1, has ganado!, FIN de la partida')
            return 1

        # TURNO J2
        codigo, impacto = disparar(self.jugadores[1], self.jugadores[0])
        if self.dificultad == 1:
            while codigo == 1:
                codigo, _ = disparar(self.jugadores[1], self.jugadores[0])
        if self.dificultad > 1 and codigo == 1:
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

    def empezar_y_jugar(self):
        while True:
            self.jugadores[0].imprimir_tableros()
            respuesta = input('Si quiere un tablero diferente escriba \'nuevo\'')
            if respuesta.lower() != 'nuevo':
                break
            else:
                self.jugadores[0] = Jugador()
        print('Tableros preparados. Comienza la partida en dificultad ', self.dificultad)
        condicion_victoria = 0
        while not condicion_victoria:
            # contiene los distintos turnos
            condicion_victoria = self.manejar_turno()
        else:
            if condicion_victoria == 1:
                print(MSG_VICTORIA)
            else:
                print(MSG_DERROTA)
