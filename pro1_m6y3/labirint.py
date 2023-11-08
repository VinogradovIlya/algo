from pygame import *

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
wall_1 = GameSprite('wall.jpg', 80, 180, 200, 320)
wall_2 = GameSprite('wall.jpg', 80, 180, 200, 140)
wall_3 = GameSprite('wall.jpg', 300, 80, 160, 100)
barriers = sprite.Group()
barriers.add(wall_1)
barriers.add(wall_2)
barriers.add(wall_3)

class Player(GameSprite):
    """ Класс для создания персонажа """
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        
player = Player('hero.png', 80, 80, 5, 400, 0, 0)
final = GameSprite('final.png', 80, 80, 600, 400)
win = transform.scale(image.load('win.jpg'), (700, 500))
lose = transform.scale(image.load('lose.jpeg'), (700, 500))
enemy = GameSprite('enemy.png', 80, 80, 300, 200)



finish = False
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

    if finish != True:  
        window.fill(back)
        player.reset()
        enemy.reset()
        player.update()
        final.reset()
        barriers.draw(window)

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (0, 0))
        if sprite.collide_rect(player, enemy):
            finish = True
            window.blit(lose, (0, 0))

    time.delay(50)
    display.update()
    

