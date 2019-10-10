from pygame import *
from crab import Crab
from jelly import Jelly
from squid import Squid
from saucer import Saucer
from button import Button
from Text import Text
from settings import settings

class start_screen:
    def __init__(self, surface: display, screen_dim: Vector2, setting: settings):
        self.surface = surface
        self.setting = setting
        self.screen_dim = screen_dim
        self.title1 = Text('SPACE', 80, Color('#000000'), Vector2(screen_dim.x / 2 - 100, screen_dim.y / 10))
        self.title2 = Text('INVADERS', 64, Color('#000000'), Vector2(screen_dim.x / 2 - 120, (screen_dim.y / 10) * 2))
        self.high_score_button = Button(surface, 'HIGH SCORES', Vector2(screen_dim.x/2 - 250, screen_dim.y / 10 * 7), Vector2(500, 70))
        self.play_game_button = Button(surface, 'PLAY SPACE INVADERS', Vector2(screen_dim.x/2 - 250, screen_dim.y / 10 * 8), Vector2(500, 70))

        self.sprite_models = list()
        self.gen_sprites()
        self.score_list = list()
        self.gen_score_list()

    def gen_sprites(self):
        self.sprite_models.append(Crab(self.setting, Vector2(self.screen_dim.x / 2 - 128, self.screen_dim.y / 10 * 3)))
        self.sprite_models.append(Jelly(self.setting, Vector2(self.screen_dim.x / 2 - 128, self.screen_dim.y / 10 * 4)))
        self.sprite_models.append(Squid(self.setting, Vector2(self.screen_dim.x / 2 - 128, self.screen_dim.y / 10 * 5)))
        self.sprite_models.append(Saucer(self.setting, Vector2(self.screen_dim.x / 2 - 128, self.screen_dim.y / 10 * 6)))

    def gen_score_list(self):
        row = 3
        for i in self.sprite_models:
            self.score_list.append(Text('= ' + str(i.score) + ' PTS',
                                        48,
                                        Color('#000000'),
                                        Vector2(self.screen_dim.x / 2 - 32, self.screen_dim.y / 10 * row + 12)))
            row += 1

    def draw(self, surface, frame):
        for i in self.sprite_models:
            i.draw(surface, frame)
        self.title1.draw(self.surface)
        self.title2.draw(self.surface)
        for j in self.score_list:
            j.draw(self.surface)
        self.play_game_button.draw_button()
        self.high_score_button.draw_button()