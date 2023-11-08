from pygame import *
import os
from pathlib import Path


# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по путimport os

# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по пути

width = 700
height = 500
back = (0, 132, 220)

display.set_caption('Лабиринт')
window = display.set_mode((width, height))
window.fill(back)


class GameSprite(sprite.Sprite):
    """ Класс для создания стен """

    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


wall_1 = GameSprite(DIR / 'wall.jpg', 80, 180, 200, 320)
wall_2 = GameSprite(DIR / 'wall.jpg', 80, 180, 150, 200)
wall_3 = GameSprite(DIR / 'wall.jpg', 80, 180, 100, 150)


class Player(GameSprite):
    """ Класс для создания персонажа """

    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


player = Player(DIR / 'hero.png', 80, 80, 5, 400, 0, 0)

run = True
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                player.y_speed -= 5
            if e.key == K_DOWN:
                player.y_speed += 5
            if e.key == K_RIGHT:
                player.x_speed += 5
            if e.key == K_LEFT:
                player.x_speed -= 5
        elif e.type == KEYUP:
            if e.key == K_UP:
                player.y_speed = 0
            if e.key == K_DOWN:
                player.y_speed = 0
            if e.key == K_RIGHT:
                player.x_speed = 0
            if e.key == K_LEFT:
                player.x_speed = 0
    window.fill(back)

    player.reset()
    player.update()
    wall_1.reset()
    wall_2.reset()
    wall_3.reset()

    time.delay(50)
    display.update()
