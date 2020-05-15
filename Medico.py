import pygame
from Medicamento import Medicamento


class Medico:
    """Clase para el medico"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.medical_image = pygame.image.load('Imagenes/medico.png')
        self.rect = self.medical_image.get_rect()
        self.x = x
        self.y = y
        self.rect.centerx = self.x / 2
        self.rect.centery = self.y - 30
        self.life = True
        self.list_curas = []
        self.medical_speed = 20

    def draw_medico(self, pygame_window):  # funcion para dibujar al medico
        pygame_window.blit(self.medical_image, self.rect)

    def mov_medico(self):  # funcion para movimiento del medico
        if self.life:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > self.x - 30:
                self.rect.right = self.x - 60

    def disparar_cura(self, x, y):  # funcion para disparar la cura
        cura = Medicamento(x, y)
        self.list_curas.append(cura)
