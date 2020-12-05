import pygame

from towerofbullets import TowerOfBullets
from screens.hud import Hud
from screens.pause import PauseView
from screens.start import StartView
from screens.config import ConfigView

from util.constants import PAUSEVIEW_ID, STARTVIEW_ID, CLOSEVIEW_ID, CONFIGVIEW_ID
from dao.saveDAO import SaveDAO


views = {
    PAUSEVIEW_ID: PauseView,
    STARTVIEW_ID: StartView,
    CONFIGVIEW_ID: ConfigView
}

class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((800, 600))
        self.game = TowerOfBullets(self.display)
        self.game.run()
        self.__overlay = StartView(self.display)
        self.hud = Hud(self.display, self.game.room.player)
        self.last_pause = 0

        self.save_dao = SaveDAO('save_info.pkl')

    @property
    def overlay(self):
        return self.__overlay

    @overlay.setter
    def overlay(self, value):
        if pygame.time.get_ticks() - self.last_pause > 200:
            self.__overlay = value
            self.last_pause = pygame.time.get_ticks()

    # salvar score no pickle
    def save(self):
        saved_score = self.save_dao.add(self.game.room.player)

    def start(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Tower of Bullets")
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            if self.overlay is None:
                self.game.render()

                next_ = self.hud.render(self.game.room.player)
                if next_ is not None:
                    self.overlay = views[next_](self.display)
            else:
                next_ = self.overlay.render()
                if next_ == CLOSEVIEW_ID:
                    self.overlay = None
                elif next_ is not None:
                    self.overlay = views[next_](self.display)

            pygame.display.update()
        
    def quit(self):
        pygame.quit()

if __name__ == '__main__':
    g = Game()
    g.start()