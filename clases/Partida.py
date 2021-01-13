from clases.Jugador import Jugador
from Constantes import *
from disparar import disparar_old
from clases.memoria_maquina import maquina_apunta_dispara
import logging


class Partida:

    def __init__(self, dificultad):
        self.jugadores = [
            Jugador('J1'),
            Jugador('J2'),
        ]
        self.dificultad = dificultad
        logging.basicConfig(level=logging.INFO)
        logging.info('Objeto Partida creado')

    def empezar_y_jugar(self):
        while True:
            self.jugadores[0].imprimir_tableros()
            respuesta = input('Si quiere un tablero diferente escriba \'nuevo\'')
            if respuesta.lower() != 'nuevo':
                break
            else:
                self.jugadores[0] = Jugador('J1')
        print('Tableros preparados. Comienza la partida en dificultad ', self.dificultad)
        condicion_victoria = PARTIDA_CONTINUA
        while condicion_victoria == PARTIDA_CONTINUA:
            # contiene los distintos turnos
            condicion_victoria = self.manejar_turno()
        else:
            if condicion_victoria == FIN_VICTORIA:
                print(MSG_VICTORIA)
            else:
                print(MSG_DERROTA)

    def manejar_turno(self):
        # Turno de J1
        cod_j1 = self.jugadores[0].turno(defensor=self.jugadores[1])
        if cod_j1 == FIN_VICTORIA:
            return FIN_VICTORIA

        # Turno de J2
        cod_j2 = self.jugadores[1].turno(defensor=self.jugadores[0], modo='auto')
        if cod_j2 == FIN_VICTORIA:
            return FIN_DERROTA

        # Dificultad 3, la maquina tiene 2 turnos
        if self.dificultad == 3:
            cod_j2 = self.jugadores[1].turno(defensor=self.jugadores[0], modo='auto')
            if cod_j2 == FIN_VICTORIA:
                return FIN_DERROTA

        return PARTIDA_CONTINUA
