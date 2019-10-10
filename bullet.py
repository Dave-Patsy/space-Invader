from pygame.locals import *
from pygame.math import *
from settings import settings
import pygame

class Bullet:

    def __init__(self, setting: settings, position: Vector2, direction):
        self.bullet_bullets_allowed = setting.bullets_allowed
        self.bullet_color = setting.bullet_color
        if direction == 'down':
            self.bullet_speed = setting.bullet_speed * -1
        if direction == 'up':
            self.bullet_speed = setting.bullet_speed
        self.bullet_height = setting.bullet_height
        self.bullet_width = setting.bullet_width
        self.position = position
        self.rect = Rect(position.x, position.y, self.bullet_width, self.bullet_height)

    def move(self):
        self.position.y -= self.bullet_speed
        self.rect.y = self.position.y

    def draw(self, surface):
        pygame.draw.rect(surface, self.bullet_color, self.rect)