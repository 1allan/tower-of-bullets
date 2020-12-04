import pygame

from .screen import Screen
from entity import Entity


class PauseView(Screen):

    def __init__(self, surface: pygame.Surface, position=None, size=None):
        super().__init__(surface, position, size)
        self.inicio = Entity(self.surface, (170, 300),
                             (200, 75), 0, 'misc/inicio.png')
        self.loja = Entity(self.surface, (420, 300),
                           (200, 75), 0, 'misc/loja.png')
        self.play = Entity(self.surface, (344, 170),
                           (102, 117), 0, 'misc/pause/play.png')

    def render(self):
        self.surface.blit(self.inicio.image, (170, 300))
        self.surface.blit(self.loja.image, (420, 300))
        self.surface.blit(self.play.image, (344, 170))
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if pygame.key.get_pressed()[pygame.K_p]:
            return 'CLOSE'
        elif self.play.rect.collidepoint(mouse_pos) and mouse_click[0]:
            return 'CLOSE'
 
 
if __name__ == '__main__':
    pause = PauseView((800, 600))
    pause.run()
