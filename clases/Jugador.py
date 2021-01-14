from clases.Tablero import Tablero
from Constantes import *
import logging
import numpy as np


class Jugador:
    def __init__(self, name):
        """
        El jugador tiene el tablero donde coloca sus
        barcos y el tablero donde va marcando sus disparos
        """
        self.name = name
        self.memoria = list()
        self.tablero_propio = Tablero(propio=True)
        self.tablero_ajeno = Tablero(propio=False)
        logging.basicConfig(level=logging.INFO)
        #logging.info('Objeto Jugador creado')

    def get_coord_propia(self, coordenada):
        return self.tablero_propio.get_coordenada(coordenada)

    def set_coord_propia(self, coordenada, tipo_impacto):
        return self.tablero_propio.set_coordenada(coordenada, tipo_impacto)

    def set_coord_ajena(self, coordenada, tipo_impacto):
        return self.tablero_ajeno.set_coordenada(coordenada, tipo_impacto)

    def turno(self, defensor, modo='manual'):

        def get_vecina(anterior_impacto):
            f, c = anterior_impacto
            coord_vecinas = [
                (f - 1, c),
                (f, c - 1),
                (f, c + 1),
                (f + 1, c),
            ]
            np.random.shuffle(coord_vecinas)
            for fv, cv in coord_vecinas:
                # If it is inside of the board
                if (0 <= fv < TAM_TABLERO) and (0 <= cv < TAM_TABLERO) and (self.tablero_ajeno.get_coordenada((fv, cv)) == AGUA):
                    return fv, cv

        def get_coord_disparo(anterior_impacto=None):
            # Modo automatico
            if modo != 'manual':
                coordenadas_nuevas = None
                # Intenta conseguir las coordenadas a partir del anterior disparo hasta 4 veces
                contador = 4
                while True:
                    #print('Bucle get_coord_disparo')
                    if anterior_impacto and contador:
                        coordenadas_nuevas = get_vecina(anterior_impacto)
                        contador -= 1
                    if not coordenadas_nuevas:
                        coordenadas_nuevas = np.random.randint(TAM_TABLERO), np.random.randint(TAM_TABLERO)

                    if self.tablero_ajeno.get_coordenada(coordenadas_nuevas) == AGUA:
                        # Sale porque tiene las nuevas coordenadas validas
                        break
                    else:
                        coordenadas_nuevas = None
                return coordenadas_nuevas
            # Modo introducir las coordenadas
            else:
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
                        Columnas A-J, filas 1-10, ej: A8''')
                    else:
                        # Comienza el juego saliendo de leer teclado
                        break

                return fila, columna

        if modo == 'manual':
            self.imprimir_tableros()
        coordenadas = get_coord_disparo()
        codigo_disparo = self.disparar(defensor, coordenadas)
        while codigo_disparo == D_ACERTASTE:
            if modo == 'manual':
                self.imprimir_tableros()
            if defensor.he_perdido():
                print(f'Enhorabuena {self.name}, has ganado, fin de la partida.')
                return FIN_VICTORIA
            # Saca las nuevas coordenadas usando la memoria de las anteriores
            coordenadas = get_coord_disparo(coordenadas)
            codigo_disparo = self.disparar(defensor, coordenadas)
        return PARTIDA_CONTINUA

    def disparar(self, defensor, coordenadas):
        if defensor.get_coord_propia(coordenadas) == AGUA:
            defensor.set_coord_propia(coordenadas, IMPACTO_AGUA)
            self.set_coord_ajena(coordenadas, IMPACTO_AGUA)
            logging.info('Agua')
            return D_FALLASTE
        elif defensor.get_coord_propia(coordenadas) == BARCO_VIVO:
            resultado_impacto, lista_bordes = defensor.set_coord_propia(coordenadas, BARCO_TOCADO)
            self.set_coord_ajena(coordenadas, BARCO_TOCADO)
            logging.info('Tocado')

            if resultado_impacto == BARCO_HUNDIDO:
                for e in lista_bordes:
                    defensor.set_coord_propia(e, IMPACTO_AGUA)
                    self.set_coord_ajena(e, IMPACTO_AGUA)
                else:
                    logging.info('Barco rodeado')
            return D_ACERTASTE

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
