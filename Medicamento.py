import pygame


class Medicamento:
    """Clase para el medicamento"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pill_image = pygame.image.load('Imagenes/cura.png')
        self.rect = self.pill_image.get_rect()
        self.pill_speed = 2
        self.rect.top = y
        self.rect.left = x

    def draw_medicamento(self, pygame_window):  # funcion para dibujar al medicamento
        pygame_window.blit(self.pill_image, self.rect)

    def mov_medicamento(self):  # funcion para el movimiento del medicamento
        self.rect.top = self.rect.top - self.pill_speed
