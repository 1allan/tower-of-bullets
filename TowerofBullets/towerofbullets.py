import pygame

from character.player import Player


class TowerOfBullets:
    
    def __init__(self, screen_size, fps=60):
        self.width, self.height = screen_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fps
        self.rooms = []
        self.player = None
        self.paused = False
    
    def start(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Super Test - Tower of Bullets")
        
        self.player = Player(self.screen, (self.width/2, self.height/2), (70, 70), 1, 'placeholder.png', 200, 200, 200)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if not self.paused:
                self.render()
            
            self.handle_key_events()
            pygame.display.update()

    def render(self):
        self.screen.fill(0)
        self.player.draw()

    def handle_key_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(( 0, -1))
        if keys[pygame.K_a]:
            self.player.move((-1,  0))
        if keys[pygame.K_s]:
            self.player.move(( 0,  1))
        if keys[pygame.K_d]:
            self.player.move(( 1,  0))


if __name__ == '__main__':
    game = TowerOfBullets((800, 600))
    game.start()