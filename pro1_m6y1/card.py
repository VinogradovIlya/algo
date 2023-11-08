import pygame


class Card(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, window):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, self.fill_color, self.rect)
