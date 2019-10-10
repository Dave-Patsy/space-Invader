from settings import settings
import pygame
import time
from sprite_sheet import spriteSheet
from pygame.locals import *
import random
from pygame import *


class Saucer:

    def __init__(self, setting: settings, pos: Vector2):
        self.velocity = pygame.Vector2(0, 0)
        self.setting = setting
        self.sprite_sheet = spriteSheet(setting.saucer_filename, 6, 2)
        self.position = pos
        self.rect = pygame.Rect(pos.x, pos.y, self.sprite_sheet.cell_width, self.sprite_sheet.cell_height)
        self.speed = setting.alien_speed
        self.spawned = False
        self.despawned = False
        self.score = '???'

    def draw(self, surface, frame):
        #pygame.draw.rect(surface, Color('#ffffff'), self.rect)
        self.sprite_sheet.draw(surface, (frame % 2) * 6, self.position.x, self.position.y)

    def move(self):
        self.position.x += self.speed
        self.rect.x = self.position.x

    def draw_death(self, surface, frame):

        row = ((frame % 3) * 5)
        for i in range(1, 5):
            print(row + i)
            self.sprite_sheet.draw(surface, row + i, self.sprite_sheet.cell_width, self.sprite_sheet.cell_height)
            time.sleep(0.1)

    def start_move(self):
        if random.randint(0, 100) == 0:
            self.spawned = True

    def is_out_of_bound(self):
        if self.rect.left > self.setting.screen_width:
            self.despawned = True
