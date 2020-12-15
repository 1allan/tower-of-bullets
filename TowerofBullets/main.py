import pygame

from game.towerofbullets import TowerOfBullets
from screens.hud import Hud
from screens.pause import PauseView
from screens.start import StartView
from screens.config import ConfigView
from screens.dead import DeadView
from screens.wait import WaitView
from screens.choose_weapon import ChooseWeaponView

from util.constants import PAUSEVIEW_ID, STARTVIEW_ID, CLOSEVIEW_ID, CONFIGVIEW_ID, DEADVIEW_ID, WAITVIEW_ID, CHOOSEWEAPONVIEW_ID


views = {
    PAUSEVIEW_ID: PauseView,
    STARTVIEW_ID: StartView,
    CONFIGVIEW_ID: ConfigView,
    DEADVIEW_ID: DeadView,
    WAITVIEW_ID: WaitView,
    CHOOSEWEAPONVIEW_ID: ChooseWeaponView
}

class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((800, 600))
        self.game = TowerOfBullets(self.display)
        self.game.run()
        self.__overlay = StartView(self.display)
        self.last_pause = 0
        self.clock = pygame.time.Clock()

    @property
    def overlay(self):
        return self.__overlay

    @overlay.setter
    def overlay(self, value):
        if pygame.time.get_ticks() - self.last_pause > 200:
            self.__overlay = value
            self.last_pause = pygame.time.get_ticks()

    def start(self):
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption("Tower of Bullets")
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            if self.overlay is None:
                next_ = self.game.render()
                if next_ is not None:
                    self.overlay = views[next_](self.display)
            else:
                next_ = self.overlay.render()
                if next_ == CLOSEVIEW_ID:
                    self.overlay = None

                elif next_ == STARTVIEW_ID:
                    self.overlay = views[next_](self.display)
                    self.game.run() # roda TowerofBullets de novo

                elif next_ == CHOOSEWEAPONVIEW_ID:
                    self.overlay = views[next_](self.display, player=self.game.player)

                elif next_ is not None:
                    self.overlay = views[next_](self.display)
            self.clock.tick(60)
            pygame.display.update()
        
    def quit(self):
        pygame.quit()

if __name__ == '__main__':
    g = Game()
    g.start()