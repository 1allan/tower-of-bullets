import pygame

from utils import load_image

from character.player import Player
from scenery.room import Room


class TowerOfBullets:
    
    def __init__(self, screen_size, fps=60):
        self.width, self.height = screen_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fps
        self.room = None
        self.player = None
        self.paused = False
    
    def run(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Tower of Bullets")
        
        # setar elementos principais
        self.room = Room(self.screen, (0, 0), (self.width, self.height),
                         'scenery/01.png', 0, 0, False)
        
        self.player = Player(self.screen, (self.width/2, self.height/2),
                             (70, 70), 5, 'placeholder.png', 200, 200)
        
        # while do jogo principal
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            # personagem colisão parede
            self.collide_walls()

            # ver se não está pausado, para renderizar o principal do jogo
            if not self.paused:
                self.render()

            # handle key events
            self.handle_input()
    
    # colisão com paredes
    def collide_walls(self):
        for index, pad in enumerate(self.room.pads):
            # parede esquerda
            if self.player.rect.colliderect(pad) and index == 0:
                self.player.move((1, 0))

            # parede inferior
            elif self.player.rect.colliderect(pad) and index == 1:
                self.player.move((0, 1))

            # parede direita
            elif self.player.rect.colliderect(pad) and index == 2:
                self.player.move((-1, 0))

            # parede superior
            elif self.player.rect.colliderect(pad) and index == 3:
                self.player.move((0, -1))

    def render(self):
        self.room.draw()
        self.player.draw()
        pygame.display.update()

    def handle_input(self):
        keyboard = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        direction = [0, 0]
        if keyboard[pygame.K_a]:
            direction[0] = -1
        elif keyboard [pygame.K_d]:
            direction[0] = 1

        if keyboard[pygame.K_w]:
            direction[1] = -1
        elif keyboard[pygame.K_s]:
            direction[1] = 1
        
        self.player.move(direction)

        if mouse[0]:
            self.player.shoot()

    def quit(self):
        pygame.quit()


if __name__ == '__main__':
    game = TowerOfBullets((800, 600))
    game.run()