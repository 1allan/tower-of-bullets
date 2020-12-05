import pygame

from random import randint, choice

from character.enemy import Enemy
from character.player import Player
from scenery.scenario import Scenario
from items.item import Item


class Room(Scenario):

    def __init__(self, surface: pygame.Surface,
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, args):

        super().__init__(surface, position, size, sprite_group, args)

        # self.enemies = pygame.sprite.Group()
        self.timeout = False
        self.coins = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.last_wave = 0
        self.player = Player(self.surface, self.sprite_group, (size[0]/2, size[1]/2),
                             (70, 70), 3, 20, 200, self.wall_sprites, gold=0)

    def spawn_portal(self):
        image_file = 'misc/portal.png'

        chosen = choice(list(self.floor_sprites))
        position = (chosen.rect.left, chosen.rect.top)

        self.portal.add(Item(self.surface, position, (32, 64), image_file, 0))

        self.sprite_group.add(self.portal)

    def detect_collision(self):
        # detect collision with each enemy
        for enemy in self.enemies:
            # bullet enemy with player
            collisionPlayer = pygame.sprite.spritecollideany(
                self.player, enemy.weapon.bullets)
            if collisionPlayer:
                self.player.be_hit(enemy.weapon.damage)
                collisionPlayer.kill()

            # bullet player with enemies
            collisionEnemy = pygame.sprite.spritecollideany(
                enemy, self.player.weapon.bullets)
            if collisionEnemy:
                enemy.be_hit(self.player.weapon.damage)
                if enemy.hp <= 0:
                    self.player.score += 10
                collisionEnemy.kill()

            # bullet with walls
            collisionWallsEnemy = pygame.sprite.groupcollide(
                enemy.weapon.bullets, self.wall_sprites, True, False)

        # detect collision coins
        collisionGold = pygame.sprite.spritecollideany(
            self.player, self.coins)
        if collisionGold:
            self.player.gold += 1
            collisionGold.kill()

        # detect collision hearts
        collisionHeart = pygame.sprite.spritecollideany(
            self.player, self.hearts)
        if collisionHeart:
            self.player.hp += 10
            if self.player.hp > 20:
                self.player.hp = 20
            collisionHeart.kill()

        # detect collision bullet player walls
        collisionWallsPlayer = pygame.sprite.groupcollide(
            self.player.weapon.bullets, self.wall_sprites, True, False)

        # detect collision portal
        collisionPortal = pygame.sprite.spritecollideany(
            self.player, self.portal)
        if collisionPortal:
            pass
            # new room logic

    def spawn_coins(self, quantity: int):
        image_file = "items/coin.png"

        for _ in range(quantity):
            chosen = choice(list(self.floor_sprites))
            position = (chosen.rect.left, chosen.rect.top)

            self.coins.add(Item(self.surface, position, (20, 20), image_file,
                                0))
            self.sprite_group.add(self.coins)

    def spawn_hearts(self, quantity: int):
        image_file = "items/ui_heart_full.png"

        for _ in range(quantity):
            chosen = choice(list(self.floor_sprites))
            position = (chosen.rect.left, chosen.rect.top)

            self.hearts.add(Item(self.surface, position, (30, 30), image_file,
                                 0))
            self.sprite_group.add(self.hearts)

    def update(self):
        self.player.draw()

        if (len(self.enemies) == 0 and self.wave_now <= self.waves[self.wave_now]["AMOUNT"] and not self.timeout):
            self.timeout = True
            self.last_wave = pygame.time.get_ticks()
            self.spawn_coins(2)
            self.spawn_hearts(1)

        elif len(self.enemies) == 0 and self.wave_now > self.waves[self.wave_now]["AMOUNT"]:
            # handle carinha passou de nível
            print('carinha passou de nível')
            self.spawn_portal()

        # timeout between waves
        if self.timeout and (pygame.time.get_ticks() - self.last_wave > 3000):
            self.timeout = False
            self.last_wave = pygame.time.get_ticks()
            self.start_wave()

        for enemy in self.enemies:
            enemy.shoot((self.player.x, self.player.y))
            enemy.chase((self.player.x, self.player.y))
            enemy.draw()
