import pygame

from .screen import Screen
from util.functions import *


COLOR_LIFEBAR = pygame.Color(0, 200, 0)
COLOR_LIFEBAR_CRITIC = pygame.Color(255, 0, 0)
COLOR_COIN_BAR = pygame.Color(255, 255, 0)
COLOR_SCORE_BAR = pygame.Color(255, 0, 0)


class Hud(Screen):
    
    def __init__(self, surface: pygame.Surface, player, position=None, size=None):
        super().__init__(surface, position, size)

        # self.surface = surface
        self.player = player
        self.hp = self.player.hp
        self.gold = self.player.gold
        self.score = self.player.score

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 30)

        self.pause_button = None
        self.pause_button_rect = pygame.Rect((750, 15), (30, 30))

    def handle_pause(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.pause_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            return 'PAUSE'
        elif pygame.key.get_pressed()[pygame.K_p]:
            return 'PAUSE'

    def update(self):
        pass

    def render(self, player):
        # lifebar
        width = 200
        hp_now = player.hp
        porcent = (hp_now / self.hp)
        width = int(width * porcent)
        color = COLOR_LIFEBAR if (porcent * 100) > 50 else COLOR_LIFEBAR_CRITIC
        if hp_now >= 0:
            pygame.draw.rect(self.surface, color, pygame.Rect(
                (15, 15), (width, 30), border_radius=5))

        # gold
        imageGold = load_image('items/coin.png', (15, 15))
        fontGold = self.font.render(
            str(player.gold), True, COLOR_COIN_BAR)
        self.surface.blit(imageGold, (220, 25))
        self.surface.blit(fontGold, (240, 15))

        # score
        font_score = self.font.render(
            f'Score: {str(player.score)}', True, COLOR_SCORE_BAR)
        self.surface.blit(font_score, (350, 15))

        # pause button

        self.pause_button = load_image('misc/pause.png', (30, 30))
        self.surface.blit(self.pause_button, (750, 15))

        self.update()
        return self.handle_pause()
