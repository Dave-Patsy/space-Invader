from pygame import *
import pygame

class Text:

    def __init__(self, msg, font_size, text_color: Color, position: Vector2):
        self.font = None
        self.font_size = font_size
        self.text_color = text_color
        self.position = position
        self.text = None
        self.msg = msg

        self.prep_msg(self.msg, self.font_size)
        pygame.font.init()

    def prep_msg(self, msg, font_size):
        """Turn msg into a rendered image and center text on the button."""
        self.font = pygame.font.SysFont(None,
                                        self.font_size,
                                        True)

        self.text = self.font.render(self.msg,
                                     True,
                                     self.text_color)

    def draw(self, surface: display):
        surface.blit(self.text, self.position)