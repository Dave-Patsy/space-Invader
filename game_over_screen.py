from pygame import *
from button import Button
from Text import Text
from settings import settings

class game_over_screen:
    def __init__(self, setting: settings, surface: display):
        self.rect = Rect(setting.screen_width/8, setting.screen_height/8, setting.screen_width * 3/4, setting.screen_height * 3/4)
        self.rect_width = self.rect.width
        self.rect_height = self.rect.height
        self.surface = surface
        self.title = Text('GAME OVER',
                          82,
                          Color('#00FF00'),
                          Vector2(self.rect_width / 2 + self.rect.left - 200,
                                  self.rect_height / 8 + self.rect.top))

        self.button1 = Button(surface, 'HIGH SCORES', Vector2(self.rect_width / 8 + self.rect.left + 150,
                                                              self.rect_height / 8 * 5 + self.rect.top),
                              Vector2(250, 64))
        self.button2 = Button(surface, 'NEW GAME', Vector2(self.rect_width / 8 + self.rect.left + 150,
                                                           self.rect_height / 8 * 4 + self.rect.top),
                              Vector2(250, 64))

    def draw(self):
        draw.rect(self.surface, Color('#0000FF'), self.rect, 5)
        self.title.draw(self.surface)
        self.button1.draw_button()
        self.button2.draw_button()

