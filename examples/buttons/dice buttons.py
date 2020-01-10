import pygame
import sys
import random

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
    
    def roll_die(self):
        return random.randint(0,6)

buttons = []
for x in range(4):
    buttons.append(Button(x * 110 + 20, 20))

dice_values = [0,0,0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(0, len(buttons)-1):
                if buttons[i].has_mouse():
                    dice_values[i] = buttons[i].roll_die()

    for b in buttons:
        screen.blit(b.img, b.rect)

    print(dice_values)

    pygame.display.flip()