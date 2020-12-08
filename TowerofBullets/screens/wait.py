import pygame

from entity import Entity
from .screen import Screen
from util.constants import CLOSEVIEW_ID, WEAPONS_DB


class WaitView(Screen):

    def __init__(self, surface: pygame.Surface, position=None, size=None):
        super().__init__(surface, position, size)
        self.duration = 3000
        self.created_at = pygame.time.get_ticks()
        self.remaining_time = 0

    def event_listener(self):
        time_passed = pygame.time.get_ticks() - self.created_at
        if time_passed > self.duration:
            return CLOSEVIEW_ID
        else:
            self.remaining_time = ((self.duration - time_passed)//1000) + 1

    def render(self):
        surface_size = self.surface.get_size()
        
        # Background
        pygame.draw.rect(self.surface, (25, 25, 25),(self.x, self.y, self.width, self.height))

        # Timer
        font = pygame.font.SysFont('Arial', 64)
        timer = font.render(str(self.remaining_time), True, (255, 255, 255))

        self.surface.blit(timer, (surface_size[0]/2, surface_size[1]/2 - 200))
        return self.event_listener()
