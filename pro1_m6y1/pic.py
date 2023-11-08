import pygame


class Pic(pygame.sprite.Sprite):
    def __init__(self, picture, w, h, x, y, window):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.window = window

    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))
