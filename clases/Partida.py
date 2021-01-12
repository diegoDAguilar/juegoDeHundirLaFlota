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
            if condicion_victoria == FIN_VICTORIA:
                print(MSG_VICTORIA)
            else:
                print(MSG_DERROTA)

    def manejar_turno(self):
        def leer_coord_disparo():
            while True:
                try:
                    entrada_teclado = input('Próximo disparo: \n')
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

            return fila, columna

        self.jugadores[0].imprimir_tableros()

        fila, columna = leer_coord_disparo()
        codigo_disparo, impacto = disparar(self.jugadores[0], self.jugadores[1], (fila, columna))
        while codigo_disparo == D_ACERTASTE:
            self.jugadores[0].imprimir_tableros()
            fila, columna = leer_coord_disparo()
            codigo_disparo, impacto = disparar(self.jugadores[0], self.jugadores[1], (fila, columna))

        if codigo_disparo == D_VICTORIA:
            print('Enhorabuena J1, has ganado, fin de la partida.')
            return FIN_VICTORIA

        # TURNO J2
        codigo_disparo, impacto = disparar(self.jugadores[1], self.jugadores[0])
        if self.dificultad == 1:
            while codigo_disparo == D_ACERTASTE:
                codigo_disparo, _ = disparar(self.jugadores[1], self.jugadores[0])
        if self.dificultad > 1 and codigo_disparo == D_ACERTASTE:
            codigo_disparo = maquina_apunta_dispara(self.jugadores[1], self.jugadores[0], impacto)
        if codigo_disparo == D_VICTORIA:
            print('Victoria de J2, fin de la partida.')
            return FIN_DERROTA

        # Dificultad 3, la maquina tiene 2 turnos
        if self.dificultad == 3:
            codigo_disparo, impacto = disparar(self.jugadores[1], self.jugadores[0])
            while codigo_disparo == D_ACERTASTE:
                codigo_disparo, _ = disparar(self.jugadores[1], self.jugadores[0])
            if self.dificultad > 1 and codigo_disparo == D_ACERTASTE:
                codigo_disparo = maquina_apunta_dispara(self.jugadores[1], self.jugadores[0], impacto)
            if codigo_disparo == D_VICTORIA:
                print('Victoria de J2, pero era muy difícil y nadie esperaba que lo lograses, fin de la partida.')
                return FIN_DERROTA

        return 0
