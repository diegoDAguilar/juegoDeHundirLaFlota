from clases.Tablero import Tablero
from Constantes import *


class Jugador:
    def __init__(self):
        """
        El jugador tiene el tablero donde coloca sus
        barcos y el tablero donde va marcando sus disparos
        """
        self.tablero_propio = Tablero(propio=True)
        self.tablero_ajeno = Tablero(propio=False)

    def preparar_tablero_propio(self):
        # TODO juntar con lo de colocar barcos
        # TODO podra ser rnd o que el jugador elija
        self.tablero_propio.colocar_todos_barcos()
        print('Barcos colocados')
        pass

    def get_coord_propia(self, coordenada):
        return self.tablero_propio.get_coordenada(coordenada)

    def set_coord_propia(self, coordenada, tipo_impacto, bordes=False):
        self.tablero_propio.set_coordenada(coordenada, tipo_impacto, bordes)

    def set_coord_ajena(self, coordenada, tipo_impacto, bordes=False):
        self.tablero_ajeno.set_coordenada(coordenada, tipo_impacto, bordes)

    def he_perdido(self):
        """
        Guarda una lista NEGADA con si los barcos estan muertos o no
        False, False son 2 barcos vivos
        True, True son 2 barcos muertos
        """
        mis_barcos = [not b.estoy_vivo() for b in self.tablero_propio.get_barcos()]
        barcos_restantes = 0
        for b in mis_barcos:
            if not b:
                barcos_restantes += 1
        print('Barcos restantes:', barcos_restantes)
        return all(mis_barcos)

    def imprimir_tableros(self):
        tablero_propio = self.tablero_propio.get_tablero()
        tablero_ajeno = self.tablero_ajeno.get_tablero()

        def borde_horizontal():
            # Imprime el borde horizontal
            for c in range(TAM_TABLERO):
                print('{:->4}'.format('-'), end='')

        def coord_horizontal():
            letra_columna = 97
            for c in range(TAM_TABLERO):
                if c == 0:
                    print('    ', end='')
                print('{:^3}'.format(chr(letra_columna + c).upper()), end='')

        # fin_linea para el segundo tablero
        def imprimir_matrices(t_propio, t_ajeno):
            for f in range(TAM_TABLERO):
                for i in range(2):
                    if i == 1:
                        print('    ', end='')
                    if f > 8:
                        print(f'{f + 1} |', end='')
                    else:
                        print(f'{f + 1}  |', end='')
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
        print()
