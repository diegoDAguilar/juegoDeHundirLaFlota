from clases.Tablero import Tablero


class Jugador:
    def __init__(self, auto = 0):
        """
        El jugador tiene el tablero donde coloca sus
        barcos y el tablero donde va marcando sus disparos

        @ auto = >0 crea un jugador automatico con un nv de dificultad
        """
        self.auto = auto
        self.tablero_propio = Tablero()
        self.tablero_ajeno = Tablero()

    def preparar_tablero(self):
        # TODO juntar con lo de colocar barcos
        # TODO podra ser rnd o que el jugador elija
        #self.tablero_propio.colocar_todos_barcos()
        print('Barcos colocados')
        pass

