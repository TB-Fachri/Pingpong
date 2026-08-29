from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,speed=0):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 9:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_h - 80:
            self.rect.y += self.speed
    def updatee(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 9:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_h - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
      

win_h = 500
win_w = 700
window = display.set_mode((win_w,win_h))
background = transform.scale(image.load("bg.png"),(win_w,win_h))

clock = time.Clock()
FPS = 60
run = True

racket1 = Player("ball.png",100, 222,10,50,10)
racket2 = Player("ball.png",600, 222,10,50,10)
ball = Ball("racket.png",200,222,30,30,5)

font.init()
font1 = font.SysFont("Arial",80)
win1 = font1.render("Player 1 Win" ,True,(0,255,0))
win2 = font1.render("Player 2 Win" ,True,(0,255,0))

speed_x = 3


finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:

      

        window.blit(background,(0,0))
        racket1.reset()
        racket1.update()

        racket2.reset()
        racket2.updatee()

        ball.reset()
        ball.update()
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            self.speed *= -1

        display.update()
        clock.tick(FPS)