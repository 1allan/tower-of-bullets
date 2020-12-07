import pygame

from entity import Entity
from .screen import Screen
from util.constants import CLOSEVIEW_ID, STARTVIEW_ID


class PauseView(Screen):

    def __init__(self, surface: pygame.Surface, position=None, size=None):
        super().__init__(surface, position, size)
        self.inicio = Entity(self.surface, (170, 300),
                             (200, 75), 0, 'misc/inicio.png')
        self.play = Entity(self.surface, (344, 170),
                           (102, 117), 0, 'misc/pause/play.png')

    def event_listener(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        emit = None
        if (pygame.key.get_pressed()[pygame.K_p] or 
           self.play.rect.collidepoint(mouse_pos) and mouse_click[0]):
            emit = CLOSEVIEW_ID
        elif self.inicio.rect.collidepoint(mouse_pos) and mouse_click[0]:
            emit = STARTVIEW_ID

        return emit

    def render(self):
        self.surface.blit(self.play.image, (344, 170))
        self.surface.blit(self.inicio.image, (295, 300))
        return self.event_listener()
