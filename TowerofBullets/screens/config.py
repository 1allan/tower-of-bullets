import pygame

from util.functions import *
from util.constants import STARTVIEW_ID

from .screen import Screen
from entity import Entity
from dao.saveDAO import SaveDAO

COLOR_BLACK = pygame.Color(0, 0, 0)

class ConfigView(Screen):
    def __init__(self, surface: pygame.Surface, position=None, size=None):
        super().__init__(surface, position, size)
        self.width, self.height = surface.get_size() if size is None else size
        self.surface = pygame.display.set_mode((self.width, self.height))

        self.bg = load_image('ui/config/bg.png', (self.width, self.height))
        self.config = Entity(surface, (131, 50),
                             (500, 50), 0, 'ui/config/config.png')
        self.back = Entity(surface, (28, 50), (64, 64),
                           0, 'ui/config/voltar.png')
        self.controles = Entity(surface, (50, 100), (305, 437), 0, 'ui/config/controles.png')
        self.recordes = Entity(surface, (50, 100), (305, 437), 0, 'ui/config/recordes.png')
        
        self.saveDAO = SaveDAO('save_info.pkl')
        self.font = pygame.font.SysFont('Arial', 20)

    def event_listener(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        emit = None

        if self.back.rect.collidepoint(*mouse_pos) and mouse_click[0]:
            return STARTVIEW_ID
    
    def get_score(self):
        scores = self.saveDAO.get_all()
        orderedScores = sorted(scores, key=lambda k: k['rooms'], reverse=True)

        x_inicial = 420
        y_inicial = 200
        for i in range(0, len(orderedScores)):
            if i < 10:
                y_inicial += 20
                font_score = self.font.render(
                f'Rooms survived = {orderedScores[i]["rooms"]} | Gold = {orderedScores[i]["gold"]}', True, COLOR_BLACK)

                self.surface.blit(font_score, (x_inicial, y_inicial))

    def render(self):
        self.surface.blit(self.bg, (0, 0))
        self.surface.blit(self.config.image, (131, 50))
        self.surface.blit(self.back.image, (28, 50))
        self.surface.blit(self.controles.image, (80, 130))
        self.surface.blit(self.recordes.image, (405, 130))

        self.get_score()

        return self.event_listener()


if __name__ == "__main__":
    config = ConfigView((800, 600))
    config.run()
