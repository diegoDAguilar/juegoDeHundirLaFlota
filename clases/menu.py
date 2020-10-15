import pygame
import pygame_menu
import os
from win32api import GetSystemMetrics
from clases.GUI import *

#Inicializamos juego
window_width = 960
window_height = 400

pos_x = GetSystemMetrics(0) / 2 - window_width / 2
pos_y = GetSystemMetrics(1) - window_height
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()
surface = pygame.display.set_mode((window_width, window_height))

dificultad = 2
#Creamos menú
def seleccionar_dificultad(value, dif):
    global dificultad
    dificultad = dif
    print('Seleccionar dificultad:', dificultad)
    pass

def empezar_partida():
    print('Empezamos partida')
    pass

menu = pygame_menu.Menu(400, 960, 'Hundir la flota',
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add_selector('Dificultad: ', [('Fácil', 1), ('Medio', 2), ('Dificil', 3)], onchange=seleccionar_dificultad)
menu.add_button('Jugar', inicio_juego, dificultad)
menu.add_button('Salir', pygame_menu.events.EXIT)

menu.mainloop(surface)