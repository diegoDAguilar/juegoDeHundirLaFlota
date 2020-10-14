import pygame
import numpy as np
import keyboard
from Constantes import *
from clases.Barco import *
from clases.Jugador import Jugador
from Constantes import *
from disparar import disparar
from clases.Tablero import *

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


def inicio_juego():

    pygame.init()

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

    gameState = np.zeros((celdaX,celdaY))

    # Control de la ejecución del juego
    pauseExect = False
    color = True

    while True:

        color = not color

        newGameState = np.copy(gameState)
        screen.fill(bg)

        #Disparamos pulsando
        newGameState = registrar_disparo(newGameState, ancho_celda, alto_celda)

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
                if 9<x<14:
                    pygame.draw.polygon(screen, (0, 0, 0), poly, 0)
                elif newGameState[x,y] == 1:
                    pygame.draw.polygon(screen, (50, 50, 50), poly, 0)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 1)


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
