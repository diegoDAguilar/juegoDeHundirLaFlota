import numpy as np
from Constantes import *
from clases.Barco import *

class Tablero:


    def __init__(self, tamanio=TAM_TABLERO):
        self.matriz = np.full((tamanio, tamanio), AGUA)
        self.lista_barcos = []

    def get_barcos(self):
        """Devuelve la lista con los barcos"""
        return self.lista_barcos


    def colocar_barco(self, tam_barco='auto', coordenadas='auto',
                      orientacion='auto'):

        orientaciones = ['n', 's', 'e', 'o']

        # Si los parámetros están en auto, los genera, sino coge los definidos
        if orientacion == 'auto':
            orientacion = orientaciones[np.random.randint(4)]

        if coordenadas == 'auto':
            coordenadas = np.random.randint(self.matriz.shape[0],
                                                 size=(1, 2))  # Array de (X,Y)
        else:
            coordenadas = np.array([coordenadas])



        while True:
            # Variables del tablero
            # x es el segundo elemento, y es el primero
            columna = coordenadas[0][1]
            fila = coordenadas[0][0]
            x_limit = self.matriz.shape[0]
            y_limit = self.matriz.shape[1]

            # Comprobamos si la posición es posible en cada orientación,
            # después comprobamos que en las coordenadas no hay barcos
            # y colocamos el nuestro

            if (0 <= columna - tam_barco) and (orientacion == 'n'):
                if BARCO_VIVO not in self.matriz[(columna - tam_barco):columna, fila]:
                    coordenadas = Tablero.rellenar_coordenadas(columna, fila, tam_barco, orientacion)
                    for punto in coordenadas:
                        self.matriz[punto] = BARCO_VIVO

                    #Añadimos barco
                    self.lista_barcos.append(Barco(coordenadas))
                    break

            elif (columna + tam_barco < x_limit) and (orientacion == 's'):
                if BARCO_VIVO not in self.matriz[columna:(columna + tam_barco), fila]:
                    coordenadas = Tablero.rellenar_coordenadas(columna, fila, tam_barco, orientacion)
                    for punto in coordenadas:
                        self.matriz[punto] = BARCO_VIVO

                    #Añadimos barco
                    self.lista_barcos.append(Barco(coordenadas))
                    break

            elif (fila + tam_barco < y_limit) and (orientacion == 'e'):
                if BARCO_VIVO not in self.matriz[columna, fila:(fila + tam_barco)]:
                    coordenadas = Tablero.rellenar_coordenadas(columna, fila, tam_barco, orientacion)
                    for punto in coordenadas:
                        self.matriz[punto] = BARCO_VIVO

                    #Añadimos barco
                    self.lista_barcos.append(Barco(coordenadas))
                    break

            elif (0 <= fila - tam_barco) and (orientacion == 'o'):
                if BARCO_VIVO not in self.matriz[columna, (fila - tam_barco):fila]:
                    coordenadas = Tablero.rellenar_coordenadas(columna, fila, tam_barco, orientacion)
                    for punto in coordenadas:
                        self.matriz[punto] = BARCO_VIVO

                    #Añadimos barco
                    self.lista_barcos.append(Barco(coordenadas))
                    break

            # Si las coordenadas no son válidas,
            # generamos unas nuevas y repetimos el proceso

            orientacion = orientaciones[np.random.randint(4)]
            coordenadas = np.random.randint(x_limit, size=(1, 2))  # Array de (X,Y)

        print('Barco creado')
        print(orientacion)



        return True

    @staticmethod
    def rellenar_coordenadas(columna, fila, tam_barco, orientacion):
        coordenadas = []
        if orientacion == 'n':
            for i in range(tam_barco):
                coordenadas.append((columna - i, fila))
        elif orientacion == 's':
            for i in range(tam_barco):
                coordenadas.append((columna, fila + i))
        elif orientacion == 'e':
            for i in range(tam_barco):
                coordenadas.append((columna + i, fila))
        elif orientacion == 'o':
            for i in range(tam_barco):
                coordenadas.append((columna, fila - i))

        return coordenadas


    def colocar_todos_barcos(self):
        tamanios_barco = [1,1,1,1,2,2,2,3,3,4]
        """
        # Por ahora colocar 3 barcos y ya:
        #self.colocar_barco(1, np.array((1,1)), 'N')
        #self.colocar_barco(3, np.array((5,5)), 'E')
        #self.colocar_barco(2, np.array((3,3)), 'S')
        #self.colocar_barco(1)
        #self.colocar_barco(3)
        #self.colocar_barco(2)

        # BARCOS MANUALES
        self.matriz[3, 2] = 'O'
        self.matriz[3, 3] = 'O'

        self.matriz[0, 8] = 'O'
        self.matriz[1, 8] = 'O'
        self.matriz[2, 8] = 'O'

        self.matriz[7, 4] = 'O'

        print('Mis barcos colocados son: ')
        print(self.matriz)
        # TODO eliminar esto cuando los tests funcionen
        return
        """


        for t in tamanios_barco:
            #x,y = 0,0 # TODO aniadir random y la orientacion random
            #orientacion = 'N'
            self.colocar_barco(t, coordenadas='auto', orientacion='auto')

    def devolver_tablero(self):
        return self.matriz



if __name__ == '__main__':
    tab1 = Tablero()
    print(tab1.devolver_tablero())
    #BARCO_VIVO in tab1.matriz[1,3]
    tab1.colocar_barco(4, (3,5), 'n')
    print(tab1.devolver_tablero())
