from pygame import *
import os

os.chdir(r'C:\Users\Liaw\Desktop\Pong Game')
back = ( 200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys - key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys - key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

racket1 = Player('racket.png', 30, 200, 50, 150, 4) 
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

clock = time.Clock()
FPS = 60
game = True

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)