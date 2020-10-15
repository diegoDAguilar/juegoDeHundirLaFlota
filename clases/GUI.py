import pygame
import pygame_gui
import numpy as np
import keyboard
from Constantes import *
from clases.Barco import *
from clases.Jugador import Jugador
from Constantes import *
from clases.Partida import Partida
from disparar import disparar
from clases.Tablero import *
from funciones import empezar_partida

def registrar_disparo(estado, ancho_celda, alto_celda):
    ## Disparar
    # Registramos eventos de teclado y ratón.
    ev = pygame.event.get()

    for event in ev:

        mouseClick = pygame.mouse.get_pressed()
        posX, posY = pygame.mouse.get_pos()
        celX, celY = int(np.floor(posX / ancho_celda)), int(np.floor(posY / alto_celda))
        if (mouseClick == (1, 0, 0)):
            estado[celX, celY] = 1

    return estado


def inicio_juego(dificultad_elegida):
    print(f'Se ha seleccionado la dificultad {dificultad_elegida}.')
    pygame.init()

    # empieza la partida
    partida = Partida()
    for j in partida.jugadores:
        j.preparar_tablero()
    #partida.jugar()
    #print(partida.jugadores[0].tablero_propio.matriz)

    manager = pygame_gui.UIManager((800, 600))

    width, height = 960, 400
    screen = pygame.display.set_mode((width, height))
    bg = 0, 128, 255 #25,25,25
    screen.fill(bg)


    # Número de celdas
    celdaX, celdaY = (TAM_TABLERO*2)+4, TAM_TABLERO


    # Dimension celdas
    ancho_celda = width/celdaX #40
    alto_celda = height/celdaY #40

    # Estado de las celdas

    gameState = np.zeros((celdaX, celdaY))

    # Control de la ejecución del juego
    pauseExect = False

    clock = pygame.time.Clock()
    contador = 0
    tablero_j1 = partida.jugadores[0].tablero_propio.matriz
    visor_j1 = partida.jugadores[0].tablero_ajeno.matriz
    while True:
        time_delta = clock.tick(1)/1000

        newGameState = np.copy(gameState)
        screen.fill(bg)

        #Disparamos pulsando
        newGameState = registrar_disparo(newGameState, ancho_celda, alto_celda)

        # Obtenemos el valor actual del tablero de J1

        tablero_j1 = partida.jugadores[0].tablero_propio.matriz
        visor_j1 = partida.jugadores[0].tablero_ajeno.matriz

        for x in range(0, celdaX):
            for y in range(0,celdaY):
                # Creamos el polígono de cada celda a dibujar.
                poly = [((x) * ancho_celda, (y) * alto_celda),
                        ((x + 1) * ancho_celda, (y) * alto_celda),
                        ((x + 1) * ancho_celda, (y + 1) * alto_celda),
                        ((x) * ancho_celda, (y + 1) * alto_celda)]

                #Convertimos a int cada valor de la lista
                poly = [tuple(map(int, coor)) for coor in poly]


                ## Dibujamos la celda para cada par de x e y.
                if 9 < x < 14:
                    pygame.draw.polygon(screen, (0, 0, 0), poly, 0)
                # Pinta el primer tablero
                elif x < 10:
                    if tablero_j1[y,x] == AGUA:
                        pygame.draw.polygon(screen, (0, 0, 255), poly, 0)
                    elif tablero_j1[y,x] == BARCO_VIVO:
                        pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                    elif tablero_j1[y, x] == BARCO_TOCADO:
                        pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
                    elif tablero_j1[y, x] == IMPACTO_AGUA:
                        pygame.draw.polygon(screen, (255, 0, 255), poly, 0)
                # Pinta el visor
                else:
                    if visor_j1[y,x-TAM_TABLERO-6] == AGUA:
                        pygame.draw.polygon(screen, (0, 0, 255), poly, 0)
                    elif visor_j1[y,x-TAM_TABLERO-6] == BARCO_VIVO:
                        pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                    elif visor_j1[y,x-TAM_TABLERO-6] == BARCO_TOCADO:
                        pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
                    elif visor_j1[y,x-TAM_TABLERO-6] == IMPACTO_AGUA:
                        pygame.draw.polygon(screen, (255, 0, 255), poly, 0)

        manager.update(time_delta)
        print(contador)
        contador += 1
        partida.nuevo_turno()

        # Actualizamos el estado del juego
        gameState = np.copy(newGameState)
        pygame.display.flip()

        # Control de ejecución del juego
        if keyboard.is_pressed("p"):
            break



##TEST

if __name__ == "__main__":
    print('Iniciamos juego')
    inicio_juego()
