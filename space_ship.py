from settings import settings
import pygame
import time
from sprite_sheet import spriteSheet
from pygame.math import Vector2
from pygame.locals import *
from gun import Gun
from fleet import Fleet
from score import score


class Ship:

    def __init__(self, setting: settings):
        self.velocity = pygame.Vector2(0, 0)
        self.sprite_sheet = spriteSheet(setting.ship_filename, 5, 4)
        self.position = Vector2(setting.screen_width/2 - self.sprite_sheet.cell_width/2, setting.screen_height - self.sprite_sheet.cell_height)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.sprite_sheet.cell_width, self.sprite_sheet.cell_height)

        self.ship_speed = setting.ship_speed
        self.life = setting.ship_life
        self.setting = setting
        self.gun = Gun(setting)
        self.moving_right = False
        self.moving_left = False
        self.score = score(0, Vector2())
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans', 24, True)

    def draw(self, surface, frame):
        # pygame.draw.rect(surface, Color('#ff0000'), self.rect)
        for bullet in self.gun.bullet_list:
            bullet.draw(surface)
        self.sprite_sheet.draw(surface, ((frame % 4) * 5), self.position.x, self.position.y)
        self.score.draw(surface, self.setting)

    def draw_score(self, surface):
        title = self.font.render("SCORE", False, Color('#000000'))
        surface.blit(title, (self.setting.screen_width - 64, 0))

    def move(self):
        if self.moving_right and self.rect.right < self.setting.screen_width:
            self.position.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.position.x -= self.ship_speed
        self.rect.x = self.position.x
        for bullet in self.gun.bullet_list:
            bullet.move()
        self.gun.out_of_bound()

    def draw_life(self, surface, frame):
        for i in range(self.life):
            self.sprite_sheet.draw(surface, ((frame % 4) * 5), 64 * i, 0)

    def shoot(self):
        self.gun.shoot(self.setting, Vector2(self.rect.centerx,self.rect.top), 'up')

    def draw_death(self, surface, frame):

        row = ((frame % 3) * 5)
        for i in range(1, 5):
            print(row + i)
            self.sprite_sheet.draw(surface, row + i, self.sprite_sheet.cell_width, self.sprite_sheet.cell_height)
            time.sleep(0.1)

    def check_alive(self):
        if self.life == 0:
            return True
        return False