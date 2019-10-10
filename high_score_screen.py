from pygame import *
from button import Button
from Text import Text
from settings import settings
from score import score
from os import path

class high_score_screen:
    def __init__(self, surface: display, setting: settings):
        self.surface = surface
        self.setting = setting
        self.return_button = Button(surface,
                                    'RETURN TO MENU',
                                    Vector2((self.setting.screen_width / 2 - 150),
                                            (self.setting.screen_height / 10) * 7 + 20),
                                    Vector2(300, 50))
        self.high_scores_text = list()
        self.high_scores = list()
        self.rect = Rect(setting.screen_width, setting.screen_height, setting.screen_width, setting.screen_height)
        self.gen_scores()
        self.title = Text('HIGH SCORES',
                          82,
                          Color('#000000'),
                          Vector2((self.setting.screen_width / 2 - 225),
                                  (self.setting.screen_height / 10) * 0 + 20))

    def gen_scores(self):
        row = 1
        if path.exists(self.setting.score_filename):
            try:
                with open(self.setting.score_filename, 'r') as f:
                    content = f.read()
                    words = content.split()
                    for word in words:
                        self.high_scores.append(int(word))
                        self.high_scores_text.append(Text(word,
                                                          64,
                                                          Color('#000000'),
                                                          Vector2((self.setting.screen_width / 2 - 40),
                                                                  (self.setting.screen_height / 10) * row + 40)))
                        row += 1
                        if row == 6:
                            break
                f.close()
            except IOError as e:
                for i in range(5):
                    self.high_scores_text.append(Text('- - -',
                                                      64,
                                                      Color('#000000'),
                                                      Vector2((self.setting.screen_width / 2 - 40),
                                                              (self.setting.screen_height / 10) * row + 40)))
                    row += 1
        else:
            for i in range(5):
                self.high_scores_text.append(Text('- - -',
                                                  64,
                                                  Color('#000000'),
                                                  Vector2((self.setting.screen_width / 2 - 40),
                                                          (self.setting.screen_height / 10) * row + 40)))
                row += 1


    def save_score(self, ship_score):
        self.high_scores.append(ship_score)
        self.high_scores.sort()

        print(self.high_scores)

        file = open(self.setting.score_filename, 'w+')
        count = 0
        for i in self.high_scores:
            if count < 5:
                file.write(str(i))
            else:
                break
        file.close()

    def draw(self):
        draw.rect(self.surface, Color('#00FF00'), self.rect, 5)
        self.title.draw(self.surface)
        for i in self.high_scores_text:
            i.draw(self.surface)
        self.return_button.draw_button()