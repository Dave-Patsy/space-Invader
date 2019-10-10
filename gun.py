from pygame.math import *
from settings import settings
from bullet import Bullet
from pygame.locals import *


class Gun:

    def __init__(self, setting: settings):
        self.bullet_list = list()
        self.setting = setting

    def shoot(self, setting: settings, position: Vector2, direction):
        if len(self.bullet_list) <= setting.bullets_allowed:
            self.bullet_list.append(Bullet(setting, position, direction))

    def move(self):
        for bullet in self.bullet_list:
            bullet.move()

    def draw(self, surface):
        for bullet in self.bullet_list:
            bullet.draw(surface)

    def out_of_bound(self):
        for bullet in self.bullet_list:
            if bullet.rect.bottom < 0:
                self.bullet_list.remove(bullet)
            if bullet.rect.top > self.setting.screen_height:
                self.bullet_list.remove(bullet)
            if bullet.rect.left > self.setting.screen_width:
                self.bullet_list.remove(bullet)
            if bullet.rect.right < 0:
                self.bullet_list.remove(bullet)

    def remove(self, bullet):
        self.bullet_list.remove(bullet)

    def reset(self):
        for bullet in self.bullet_list:
            self.bullet_list.remove(bullet)
