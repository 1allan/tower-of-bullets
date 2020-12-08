import pygame

from util.functions import load_image
from util.constants import CLOSEVIEW_ID, CONFIGVIEW_ID, CHOOSEWEAPONVIEW_ID

from entity import Entity
from .screen import Screen
from towerofbullets import TowerOfBullets


class StartView(Screen):

    def __init__(self, surface: pygame.Surface, position=None, size=None):
        super().__init__(surface, position, size)
        self.width, self.height = surface.get_size() if size is None else size
        self.surface = pygame.display.set_mode((self.width, self.height))

        self.bg = load_image('misc/start/bg.png', (self.width, self.height))
        self.play = Entity(self.surface, (170, 300),
                           (200, 75), 0, 'misc/start/play.png')
        self.config = Entity(self.surface, (420, 300),
                             (200, 75), 0, 'misc/start/config.png')
        self.exit = Entity(self.surface, (680, 100),
                           (60, 60), 0, 'misc/start/exit.png')

    def event_listener(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        emit = None

        if self.play.rect.collidepoint(*mouse_pos) and mouse_click[0]:
            emit = CLOSEVIEW_ID
        elif self.config.rect.collidepoint(*mouse_pos) and mouse_click[0]:
            # emit = CHOOSEWEAPONVIEW_ID
            emit = CONFIGVIEW_ID
        elif self.exit.rect.collidepoint(*mouse_pos) and mouse_click[0]:
            pygame.quit()

        return emit

    def render(self):
        self.surface.blit(self.bg, (0, 0))
        self.surface.blit(self.play.image, (170, 300))
        self.surface.blit(self.config.image, (420, 300))
        self.surface.blit(self.exit.image, (680, 100))
        return self.event_listener()
