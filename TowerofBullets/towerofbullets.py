import pygame
from time import time

from util.functions import load_image
from util.constants import ROOMS_DB, DEADVIEW_ID
from scenery.room import Room
from screens.hud import Hud
from dao.saveDAO import SaveDAO


class TowerOfBullets:

    def __init__(self, display, fps=60):
        self.surface = display
        self.width, self.height = self.surface.get_size()
        self.fps = fps

        self.room = None
        self.sprites = pygame.sprite.Group()
        self.save_dao = SaveDAO('save_info.pkl')

    def run(self):
        self.room = Room(self.surface, self.sprites, (0, 0), (self.width,
                                               self.height), ROOMS_DB['SALA1'])
        self.hud = Hud(self.surface, self.room.player)

    def handle_input(self):
        keyboard = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        direction = [0, 0]
        if keyboard[pygame.K_a]:
            direction[0] = -1
        elif keyboard[pygame.K_d]:
            direction[0] = 1

        if keyboard[pygame.K_w]:
            direction[1] = -1
        elif keyboard[pygame.K_s]:
            direction[1] = 1

        self.room.player.move(direction)

        if mouse[0]:
            self.room.player.attack(mouse_pos)
            self.sprites.add(self.room.player.bullets)

    def __collide_with(self, target):
        def callback(spr1, spr2):
            hited = spr1.rect.colliderect(spr2.rect)
            if hited:
                if target == 'bullet':
                    spr1.be_hit(spr2.damage)
                elif target == 'heart':
                    spr1.hp += 10
                    if spr1.hp > 20:
                        spr1.hp = 20
                elif target == 'coin':
                    spr1.gold += 1
                elif target == 'portal':
                    pass
                spr2.kill()
            return hited
        return callback

    def collision(self):
        bullets = pygame.sprite.Group()
        bullets.add(self.room.player.bullets)
        bullets.add(self.room.enemy_bullets)

        pygame.sprite.groupcollide(bullets, self.room.walls, True, False)
        pygame.sprite.spritecollideany(self.room.player, 
                                       self.room.enemy_bullets, 
                                       collided=self.__collide_with('bullet'))
        pygame.sprite.groupcollide(self.room.enemies, self.room.player.bullets,
                                   False, False, 
                                   collided=self.__collide_with('bullet'))
        
        pygame.sprite.spritecollideany(self.room.player, self.room.hearts, 
                                       collided=self.__collide_with('heart'))
        pygame.sprite.spritecollideany(self.room.player, self.room.coins, 
                                       collided=self.__collide_with('coin'))
        pygame.sprite.spritecollideany(self.room.player, self.room.portal,
                                       collided=self.__collide_with('portal'))

    def update(self):
        self.handle_input()
        self.collision()
        self.sprites.update()

    def render(self):
        self.update()

        self.room.draw()
        self.sprites.draw(self.surface)
        
        self.room.overlay.draw(self.surface)

        hud_render = self.hud.render()
        # ver se o jogador ganhou ou perdeu
        if self.room.player.hp <= 0:
            player = {
                "score": self.room.player.score,
                "gold": self.room.player.gold
            }

            self.save_dao.add(player)
            return DEADVIEW_ID
        elif( len(self.room.enemies) == 0 and 
            self.room.wave_now > self.room.waves[self.room.wave_now]["AMOUNT"]):
            print('ganhou!')
        else:
            return hud_render
