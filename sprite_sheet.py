import pygame


class spriteSheet:

    def __init__(self, filename, col, row):

        self.sheet = pygame.image.load(filename)

        self.row = row
        self.col = col
        self.cell_count = row * col
        print(self.cell_count)
        self.rect = self.sheet.get_rect()

        w = self.cell_width = self.rect.width / col
        h = self.cell_height = self.rect.height / row
        hw, hh = self.cell_center = (w / 2, h / 2)

        self.cells = list([((index % col) * w, (index / col) * h, w, h) for index in range(self.cell_count)])

    def draw(self, surface, cell_index, x, y):
        surface.blit(self.sheet, (x, y), self.cells[cell_index])
