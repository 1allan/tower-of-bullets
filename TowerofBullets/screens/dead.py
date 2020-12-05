import pygame

from entity import Entity
from .screen import Screen
from util.constants import CONFIGVIEW_ID, STARTVIEW_ID
from dao.saveDAO import SaveDAO

class DeadView(Screen):

    def __init__(self, surface: pygame.Surface, position=None, size=None):
        super().__init__(surface, position, size)
        self.bg = Entity(self.surface, (0, 0), (800, 600))
        self.game_over = Entity(self.surface, (240, 60), (320, 202), 0, 'misc/game_over/gameOver.png')

        self.inicio = Entity(self.surface, (170, 300),
                             (200, 75), 0, 'misc/inicio.png')
        self.config = Entity(self.surface, (420, 300),
                             (200, 75), 0, 'misc/start/config.png')
        
        self.save_dao = SaveDAO('save_info.pkl')


    def event_listener(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        emit = None
        if self.config.rect.collidepoint(mouse_pos) and mouse_click[0]:
            emit = CONFIGVIEW_ID
        elif self.inicio.rect.collidepoint(mouse_pos) and mouse_click[0]:
            emit = STARTVIEW_ID

        return emit

    def render(self):
        self.surface.blit(self.bg, (0, 0))
        self.surface.blit(self.game_over, (240, 60))

        self.surface.blit(self.inicio, (100, 400))
        self.surface.blit(self.config, (300, 400))

        return self.event_listener()
