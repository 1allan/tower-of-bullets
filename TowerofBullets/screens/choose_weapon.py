import pygame

from entity import Entity
from .screen import Screen
from util.constants import CLOSEVIEW_ID, WEAPONS_DB
from util.functions import *

class ChooseWeaponView(Screen):
  def __init__(self, surface: pygame.Surface, position=None, size=None, player=None):
        super().__init__(surface, position, size)
        self.player = player
        self.bg = Entity(self.surface, (0, 0), self.surface.get_size(), 0, 'ui/config/bg.png')

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 30)

  def event_listener(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    return None

  def render(self):
    self.surface.blit(self.bg.image, (0, 0))

    return self.event_listener()