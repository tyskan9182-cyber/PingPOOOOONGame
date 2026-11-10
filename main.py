from pygame import *
from random import randint 
window_size_one = 900
window_size_two = 700

game = True
finish = False

clock = time.Clock()

fps = 60

window = display.set_mode((window_size_one, window_size_two))
display.set_caption('PingPONG')
background = transform.scale(image.load('table.PNG') , (window_size_one, window_size_two))

speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None, 55)
lose1 = font1.render('PLAYER ONE LOSE!!!', True, (180,0,0))
lose2 = font1.render('PLAYER TWO LOSE!!!', True, (180,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_size_two - 95:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_size_two - 95:
            self.rect.y += self.speed
rocket_player_one = Player('racket.png', 60, 300, 35, 100, 5)
rocket_player_two = Player('racket.png', 800, 300, 35, 100, 5)
balls = Player('tenis_ball.png', 100, 100, 50, 50, 4)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        balls.rect.x += speed_x
        balls.rect.y += speed_y
        window.blit(background, (0, 0))
        rocket_player_one.reset()
        rocket_player_one.update_r()
        rocket_player_two.reset()
        rocket_player_two.update_l()
        if balls.rect.y > window_size_two-50 or balls.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(rocket_player_one, balls) or sprite.collide_rect(rocket_player_two, balls):
            speed_x *= -1
            randoms = randint(1, 2)
            if randoms == 1:
                speed_y *= -1
        if balls.rect.x < 0:
            finish = True
            window.blit(lose1, (270, 330))
        if balls.rect.x > window_size_one:
            finish = True
            window.blit(lose2, (270, 330))
        balls.reset()
        display.update()
        clock.tick(fps)