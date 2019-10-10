from settings import settings
from crab import Crab
from jelly import Jelly
from squid import Squid
from saucer import Saucer
import pygame
import random
from pygame.math import Vector2
from gun import Gun


#from space_ship import Ship


def check_shoot():
    x = random.randint(0, 500)

    if x == 0:
        return True
    return False


class Fleet:
    def __init__(self, setting: settings, shoot_sound):
        self.shoot_sound = shoot_sound
        self.fleet = list()
        self.move_speed = setting.alien_speed
        self.creep_speed = setting.creep_speed
        self.gun = Gun(setting)
        self.setting = setting
        self.saucer = Saucer(setting, Vector2(-64, 64 * 2))

        for i in range(10):
            self.fleet.append(Squid(setting, pygame.Vector2( 70 * i, 70)))
        for i in range(10):
            self.fleet.append(Squid(setting, pygame.Vector2( 70 * i, 70 * 2)))
        for i in range(10):
            self.fleet.append(Jelly(setting, pygame.Vector2( 70 * i, 70 * 3)))
        for i in range(10):
            self.fleet.append(Jelly(setting, pygame.Vector2( 70 * i, 70 * 4)))
        for i in range(10):
            self.fleet.append(Crab(setting, pygame.Vector2( 70 * i, 70 * 5)))
        for i in range(10):
            self.fleet.append(Crab(setting, pygame.Vector2( 70 * i, 70 * 6)))

    def draw(self, surface, frame):
        for alien in self.fleet:
            alien.draw(surface, frame)
        self.gun.draw(surface)
        if self.saucer.spawned and not self.saucer.despawned:
            self.saucer.draw(surface, frame)

    def move(self):
        for alien in self.fleet:
            alien.move(self.move_speed)
            if check_shoot():
                self.shoot_sound.play()
                self.gun.shoot(self.setting, Vector2(alien.position.x + alien.sprite_sheet.cell_width /2, alien.position.y + alien.sprite_sheet.cell_height), 'down')
        for bullet in self.gun.bullet_list:
            bullet.move()
        self.gun.out_of_bound()

        if self.saucer.spawned and not self.saucer.despawned:
            self.saucer.move()
        else:
            self.saucer.start_move()

    def creep(self):
        for alien in self.fleet:
            alien.creep(self.creep_speed)

    def out_of_bound(self, setting: settings):
        hit = False
        for alien in self.fleet:
            if alien.rect.left < 0:
                hit = True
            if alien.rect.right > setting.screen_width:
                hit = True
        if hit:
            self.move_speed = self.move_speed * -1
            self.creep()

    def speedup(self):
        self.move_speed *= self.setting.speedup_scale
