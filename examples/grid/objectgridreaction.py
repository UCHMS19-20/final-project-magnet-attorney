import pygame
import sys

width, height = 600, 600
cell_count = 3
cell_size = width/cell_count

grid = []

class Cell:

    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.sz = sz
        self.filled = False
        self.rectangle = pygame.Rect(self.x * sz, self.y * sz, sz, sz)
    
    def show(self):
        pygame.draw.rect(screen, pygame.Color("pink"), self.rectangle, 2)
        if self.filled:
            pygame.draw.rect(screen, pygame.Color("pink"), self.rectangle)

pygame.init()

screen = pygame.display.set_mode((width, height))

for y in range(cell_count):
    for x in range(cell_count):
        grid.append(Cell(x, y, cell_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # pygame.draw.rect(screen, pygame.Color("red"), (0,0,50,50))
    for cell in grid:
        if cell.rectangle.collidepoint(pygame.mouse.get_pos()):
            cell.filled = True
        cell.show()
        
        
    pygame.display.flip()