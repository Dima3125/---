from random import randint
from pygame import *
from time import time as timer

font.init()
font2 = font.SysFont('Arial', 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (75, 80))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
           self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
           self.rect.y += self.speed


win_width = 700
win_height = 500
lost = 0
score = 0
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("P1.png"), (win_width, win_height))
player = Player('M.png', 5, win_height - 70, 20)
player2 = Player('M.png', 620, win_height - 70, 20)

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,  (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2,  (200, 200))

        racket1.recet()
        racket2.reset()
        ball.reset()

        
        
        player.reset()
        player2.reset()
        player.update_l()
        player2.update_r()



    display.update()
    time.delay(20)







        
    
