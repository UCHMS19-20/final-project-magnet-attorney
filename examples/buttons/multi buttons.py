import pygame
import sys


width, height = 600,480

screen = pygame.display.set_mode((width,height))

class Button:
    def __init__(self, x, y):
        # self.x = x
        # self.y = y
        self.img = pygame.image.load("buttons/tesla.png")
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = x, y
        self.message = f"{x},{y}"
    
    def has_mouse(self):
        """Return True if mouse is in button and False otherwise"""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False
    
        

button1 = Button(20,20)
button2 = Button(200,20)
button3 = Button(220,20)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.has_mouse():
                print(button1.message)
            elif button2.has_mouse():
                print(button2.message)

    
    screen.blit(button1.img, button1.rect)
    screen.blit(button2.img, button2.rect)

    pygame.display.flip()