from paddle import Paddle
from tiniball import Tiniball
import pygame
pygame.init()

#constants
BLACK = (0,0,0)
WHITE = (255,255,255)
SIZE = (500,600)

#making screen
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("pong")

#makingpaddles
paddle1 = Paddle(WHITE,10,100)
paddle1.rect.x = 20
paddle1.rect.y = 200

paddle2 = Paddle(WHITE,10,100)
paddle2.rect.x = SIZE[0]-20
paddle2.rect.y = 200

tiniball = Tiniball(WHITE,10,10)
tiniball.rect.x = SIZE[0]/2
tiniball.rect.y = SIZE[1]/2

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(tiniball)

#gameloops
carryOn = True
clock = pygame.time.Clock()
middle = SIZE[0]/2

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()
    tiniball.update()
    if keys[pygame.K_w]:
        paddle1.moveUp(5)
    if keys[pygame.K_x]:
        paddle1.moveDown(5)
    if keys[pygame.K_i]:
        paddle2.moveUp(5)
    if keys[pygame.K_m]:
        paddle2.moveDown(5)
    
    pygame.draw.line(screen,WHITE,[middle,0],[middle,SIZE[1]],5)
    all_sprites_list.draw(screen)

    if tiniball.rect.x > SIZE[0]:
        tiniball.speed[0] = -tiniball.speed[0]
    if tiniball.rect.x < 0:
        tiniball.speed[0] = -tiniball.speed[0]
    if tiniball.rect.y > SIZE[1]:
        tiniball.speed[1] = -tiniball.speed[1]
    if tiniball.rect.y < 0:
        tiniball.speed[1] = -tiniball.speed[1]

    if pygame.sprite.collide_mask(tiniball, paddle1) or pygame.sprite.collide_mask(tiniball, paddle2):
        tiniball.bounce()
    

    pygame.display.flip()
    clock.tick(60)

