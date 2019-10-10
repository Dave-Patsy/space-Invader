import pygame, sys, random, time, math, string
from pygame.locals import *
from settings import settings
from pygame.math import Vector2

class score:
    def __init__(self, init_score, position: Vector2):
        self.score = init_score
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans', 24, True)

    def add(self, val):
        self.score += val

    def draw(self, scene, setting: settings):
        val = self.font.render(str(self.score), False, Color('#000000'))
        scene.blit(val, (setting.screen_width - 64, 24))
