import pygame

from .screen import Screen
from entity import Entity


class Pause(Screen):

    def __init__(self, surface: pygame.Surface, position=None, size=None):
        super().__init__(surface, position, size)
        self.inicio = Entity(self.surface, (170, 300),
                             (200, 75), 0, 'misc/inicio.png')
        self.loja = Entity(self.surface, (420, 300),
                           (200, 75), 0, 'misc/loja.png')
        self.play = Entity(self.surface, (344, 170),
                           (102, 117), 0, 'misc/pause/play.png')

    def draw(self):
        click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        if click:
            if mouse_pos[0] > self.inicio.rect.left and mouse_pos[0] < self.inicio.rect.left + self.inicio.width and mouse_pos[1] > self.inicio.rect.top and mouse_pos[1] < self.inicio.rect.top + self.inicio.height:
                return 'inicio'
        
        self.surface.blit(self.inicio.image, (170, 300))
        self.surface.blit(self.loja.image, (420, 300))
        self.surface.blit(self.play.image, (344, 170))

if __name__ == '__main__':
    pause = Pause((800, 600))
    pause.run()
