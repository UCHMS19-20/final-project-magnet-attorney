import pygame
import sys

pygame.init()

w, h = 800, 600
x,y = 20,20
sz = 40
speed = .1
moving = True

screen = pygame.display.set_mode( (w, h) )
pygame.time.set_timer(pygame.USEREVENT + 1, 500)

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT + 1:
            moving = not moving
    
    if moving:
        x += speed
    pygame.draw.rect(screen, (130, 80, 255), (x,y,sz,sz))

    
    pygame.display.flip()
