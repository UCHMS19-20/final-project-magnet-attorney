import pygame
import sys


width, height = 600,480

screen = pygame.display.set_mode((width,height))

class Button:
    # def __init__(self, x, y):
    def __init__(self):
        self.x = 20
        self.y = 20
        self.img = pygame.image.load("buttons/tesla.png")
        self.rect = self.img.get_rect()
    
    def has_mouse(self):
        """Return True if mouse is in button and False otherwise"""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False
        

button = Button()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.has_mouse():
                print("Hello")
    
    screen.blit(button.img, (button.x,button.y))
    pygame.display.flip()