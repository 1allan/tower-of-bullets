import pygame

from .screen import Screen
from util.functions import *
from util.constants import PAUSEVIEW_ID


COLOR_RED = pygame.Color(237, 28, 36)
COLOR_BLUE = pygame.Color(0, 162, 232)
COLOR_YELLOW = pygame.Color(250, 203, 62)


class Hud(Screen):
    
    def __init__(self, surface: pygame.Surface, player, position=None, 
                 size=None):
                 
        super().__init__(surface, position, size)

        # self.surface = surface
        self.player = player

        self.gold_start = self.player.gold
        
        self.pause_button_rect = pygame.Rect((720, 15), (40, 40))

    def event_listener(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        emit = None
        if (self.pause_button_rect.collidepoint(mouse_pos) and 
           mouse_click[0] or
           pygame.key.get_pressed()[pygame.K_p]):
            emit =  PAUSEVIEW_ID
            
        return emit

    def render(self):
        # Life bar
        current_hp = 150 * self.player.hp / self.player.max_hp
        pygame.draw.rect(self.surface, (0, 0, 0), (17, 8, 154, 19))
        pygame.draw.rect(self.surface, COLOR_RED, (20, 10, current_hp, 15))

        # Energy bar
        current_energy = 150 * self.player.energy / self.player.max_energy
        pygame.draw.rect(self.surface, (0, 0, 0), (17, 33, 154, 19))
        pygame.draw.rect(self.surface, COLOR_BLUE, (20, 35, current_energy, 
                         15))

        # Coins display
        font = pygame.font.SysFont('Arial', 15)
        gold = font.render(str(self.player.gold), True, COLOR_YELLOW)
        self.surface.blit(load_image('misc/coin.png', (15, 15)), (20, 55))
        self.surface.blit(gold, (40, 55))

        self.surface.blit(load_image('ui/pause.png', (40, 40)), (720, 15))
        
        return self.event_listener()
