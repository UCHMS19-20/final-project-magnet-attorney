import pygame
import sys

width, height = 600, 600
cell_count = 3
cell_size = width/cell_count


pygame.init()

screen = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # pygame.draw.rect(screen, pygame.Color("red"), (0,0,50,50))
    for y in range(cell_count):
        for x in range(cell_count):
            pygame.draw.rect(screen, pygame.Color("pink"), (x * cell_size,y * cell_size,cell_size,cell_size), 2)

    pygame.display.flip()