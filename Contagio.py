import pygame


class Contagio:
    """Clase para el contagio"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.covid_image = pygame.image.load('Imagenes/virus.png')
        self.rect = self.covid_image.get_rect()
        self.covid_speed = 1
        self.rect.top = y
        self.rect.left = x

    def draw_covid(self, pygame_window):  # funcion para dibujar el covid
        pygame_window.blit(self.covid_image, self.rect)

    def mov_covid(self):  # funcion para movimiento del covid
        self.rect.top = self.rect.top + self.covid_speed
