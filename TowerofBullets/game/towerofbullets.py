import pygame
from random import choice
from pygame.sprite import Group, groupcollide, spritecollide, spritecollideany
from time import time

from util.functions import load_image
from util.constants import ROOMS_DB, DEADVIEW_ID, WAITVIEW_ID

from .singleton import SingletonMeta
from scenery.room import Room
from screens.hud import Hud
from character.player import Player
from dao.saveDAO import SaveDAO


class TowerOfBullets(metaclass=SingletonMeta):

    def __init__(self, display, fps=60):
        self.surface = display
        self.width, self.height = self.surface.get_size()
        self.fps = fps

        self.room = None
        self.player = None
        self.sprites = Group()
        self.save_dao = SaveDAO('save_info.pkl')
        self.changed_room = False

    def run(self):
        self.sprites = Group()
        self.player = Player(self.surface, (0, 0), (40, 70), 5,
                             100, 200, Group(), gold=0, animated=True)
        self.new_room()

        self.room.spawn_player(self.player)
        self.hud = Hud(self.surface, self.player)

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

        self.player.move(direction)

        if keyboard[pygame.K_q]:
            self.player.swap_weapons()

        if mouse[0]:
            self.player.attack(mouse_pos)
            self.sprites.add(self.player.bullets)

    def new_room(self):
        if self.room is not None:
            self.room.kill()
        room_data = ROOMS_DB[choice(list(ROOMS_DB.keys()))]
        self.room = Room(self.surface, (0, 0), (self.width, self.height), 
                         room_data)
        self.player.wall_sprites = self.room.walls
        self.room.player = self.player
        self.player.rect.left, self.player.rect.top = self.room.spawn_point
        self.changed_room = True

    def __collide_with(self, target):
        def callback(spr1, spr2):
            hited = spr1.rect.colliderect(spr2.rect)
            if hited:
                if target == 'bullet':
                    spr1.be_hit(spr2.damage)
                elif target == 'heart':
                    spr1.hp += 10
                    if spr1.hp > spr1.max_hp:
                        spr1.hp = spr1.max_hp
                elif target == 'coin':
                    spr1.gold += 1
                elif target == 'portal':
                    pass
                elif target == 'energy_orb':
                    spr1.energy += 10
                    if spr1.energy > spr1.max_energy:
                        spr1.energy = spr1.max_energy
                spr2.kill()
            return hited
        return callback

    def collision(self):
        bullets = Group()
        bullets.add(self.player.bullets)
        bullets.add(self.room.enemies_bullets)

        groupcollide(bullets, self.room.walls, True, False)
        spritecollideany(self.player, self.room.enemies_bullets,
                         collided=self.__collide_with('bullet'))
        groupcollide(self.room.enemies, self.player.bullets, False, False,
                     collided=self.__collide_with('bullet'))

        spritecollideany(self.player, self.room.hearts,
                         collided=self.__collide_with('heart'))
        spritecollideany(self.player, self.room.coins,
                         collided=self.__collide_with('coin'))
        spritecollideany(self.player, self.room.energy_orbs,
                         collided=self.__collide_with('energy_orb'))

        if self.room.portal is not None:
            entered = self.player.rect.colliderect(self.room.portal.rect)
            if entered:
                self.new_room()
                self.player.rooms_survived += 1

    def update(self):
        self.handle_input()
        self.collision()
        self.sprites.update()
        self.player.weapon.update(pygame.mouse.get_pos())

    def render(self):
        self.update()

        # if self.changed_room:
        #     self.changed_room = False
        #     return WAITVIEW_ID

        self.room.draw()
        self.sprites.draw(self.surface)

        self.room.overlay.draw(self.surface)

        hud_render = self.hud.render()
        # ver se o jogador ganhou ou perdeu
        if self.player.hp <= 0:
            player = {
                "rooms": self.player.rooms_survived,
                "gold": self.player.gold
            }

            self.save_dao.add(player)
            return DEADVIEW_ID
        elif(len(self.room.enemies) == 0 and
             self.room.wave_now > len(self.room.waves)):
            print('ganhou!')
        else:
            return hud_render
