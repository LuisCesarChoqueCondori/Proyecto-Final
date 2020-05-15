import pygame
from random import randint
from Contagio import Contagio


class Virus:
    """Clase para el virus"""

    def __init__(self, x, y, window_width, window_height):
        pygame.sprite.Sprite.__init__(self)
        self.virus_image = pygame.image.load('Imagenes/covid_19b.png')
        self.rect = self.virus_image.get_rect()
        self.width = window_width
        self.height = window_height
        self.posicion_image = 0
        self.virus_speed = 2
        self.rect.top = y
        self.rect.left = x
        self.list_virus = []
        self.rango_contagio = 5
        self.time_cambio = 1
        self.mov_right = True

    def draw_virus(self, pygame_window):  # funcion para dibujar al virus
        pygame_window.blit(self.virus_image, self.rect)

    def comportamiento(self, tiempo):  # funcion para disparar el virus
        self._contagio()
        if self.time_cambio == tiempo:
            self.posicion_image += 1
            self.time_cambio += 1
            if self.posicion_image > (len(self.list_virus) - 1):
                self.posicion_image = 0

    def _contagio(self):
        if randint(0, 1000) < self.rango_contagio:
            self._propagacion()

    def _propagacion(self):  # funcion para guardar el virus
        x, y = self.rect.center
        virus = Contagio(x, y)
        self.list_virus.append(virus)

    def mov_virus(self):  # funcion para el movimiento del virus
        if self.mov_right:
            if self.rect.left < self.width - 60:
                self.rect.left += 2
            else:
                self.mov_right = False
        elif self.mov_right == False:
            if self.rect.left > 0:
                self.rect.left -= 2
            else:
                self.mov_right = True
