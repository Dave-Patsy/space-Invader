import pygame, sys, time
from pygame.locals import *


class settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 780
        self.bg_color = Color('#ffff00')

        # Filenames
        self.crab_filename = "image/Crab Alien.png"
        self.jelly_filename = "image/Jelly Alien.png"
        self.saucer_filename = "image/suacer.png"
        self.ship_filename = "image/Space Ship.png"
        self.squid_filename = "image/Squid.png"
        self.score_filename = "data/score.txt"

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = Color('#000000')
        self.bullets_allowed = 100

        # Score value
        self.crab_score = 20
        self.jelly_score = 40
        self.squid_score = 80
        self.saucer_score_min = 100
        self.saucer_score_max = 1000

        # sprite speed
        self.ship_speed = 30
        self.alien_speed = 5
        self.bullet_speed = 25
        self.creep_speed = 10

        #
        self.ship_life = 3

        # spawn direction
        self.fleet_direction = 1

        # Scalers
        self.speedup_scale = 1.04
        self.score_scale = 1.5

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    def increase_score(self):
        self.crab_score *= self.score_scale
        self.jelly_score *= self.score_scale
        self.squid_score *= self.score_scale


