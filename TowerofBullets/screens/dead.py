import pygame

from entity import Entity
from .screen import Screen
from util.constants import CONFIGVIEW_ID, STARTVIEW_ID
from dao.saveDAO import SaveDAO

COLOR_WHITE = pygame.Color(255, 255, 255)
class DeadView(Screen):

    def __init__(self, surface: pygame.Surface, position=None, size=None):
        super().__init__(surface, position, size)
        self.bg = Entity(self.surface, (0, 0), self.surface.get_size(), 0, 'ui/config/bg.png')

        self.game_over = Entity(self.surface, (240, 60), (320, 202), 0, 'ui/game_over/gameOver.png')
        self.inicio = Entity(self.surface, (100, 400),
                             (200, 75), 0, 'ui/inicio.png')
        self.config = Entity(self.surface, (500, 400),
                             (200, 75), 0, 'ui/start/config.png')
        
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 30)

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

    def get_score(self):
        scores = self.save_dao.get_all()
        orderedScores = sorted(scores, key=lambda k: k['timestamp'], reverse=True)

        font_score = self.font.render(
            f'Rooms survived: {str(orderedScores[0]["rooms"])} | Gold: {str(orderedScores[0]["gold"])}', True, COLOR_WHITE)
        self.surface.blit(font_score, (230, 300))

    def render(self):
        self.surface.blit(self.bg.image, (0, 0))
        self.surface.blit(self.game_over.image, (240, 60))

        self.surface.blit(self.inicio.image, (100, 400))
        self.surface.blit(self.config.image, (500, 400))

        self.get_score()

        return self.event_listener()
