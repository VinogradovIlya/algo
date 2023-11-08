from pygame import *
import card
import pic


# константы
GREEN = (0, 255, 0)
WIN_WIDTH = 700
WIN_HEIGHT = 500

# основная программа
display.set_caption('Моя первая игра')
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
picture = transform.scale(image.load(
    'algo/pro1_m6y1/1920x1080.jpg'), (WIN_WIDTH, WIN_HEIGHT))
player1 = card.Card(80, 80, 100, 200, GREEN, window)
player2 = pic.Pic('algo/pro1_m6y1/square.png', 80, 80, 500, 200, window)
run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(picture, (0, 0))
    player1.draw()
    player2.reset()
    display.update()
