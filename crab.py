from settings import settings
import pygame
from pygame.locals import *
import time
from sprite_sheet import spriteSheet
from pygame.math import Vector2

class Crab:

    def __init__(self, setting: settings, position: Vector2):
        self.velocity = pygame.Vector2(0, 0)
        self.position = position
        self.score = setting.crab_score
        self.sprite_sheet = spriteSheet(setting.crab_filename, 5, 3)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.sprite_sheet.cell_width, self.sprite_sheet.cell_height)

    def draw(self, surface, frame):
        #pygame.draw.rect(surface, Color('#ff0000'), self.rect)
        self.sprite_sheet.draw(surface, ((frame % 3) * 5), self.position.x, self.position.y)

    def draw_death(self, surface, frame):

        row = ((frame % 3) * 5)
        for i in range(1, 5):
            print(row + i)
            self.sprite_sheet.draw(surface, row + i, self.sprite_sheet.cell_width, self.sprite_sheet.cell_height)
            time.sleep(0.1)

    def move(self, alien_speed):
        self.position.x += alien_speed
        self.rect.x = self.position.x

    def creep(self, creep_speed):
        self.position.y += creep_speed
        self.rect.y = self.position.y
