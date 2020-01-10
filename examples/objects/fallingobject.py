import pygame
import sys
import random

class Particle:

    def __init__(self, x):
        self.x = x
        self.y = 0
        self.vel = 1
        self.is_here = True

    def fall(self):
        self.y += self.vel
    
    def show(self):
        pygame.draw.rect(screen, (200,100,255), (self.x,self.y,20,20))
    
    def check_bottom(self):
        if self.y > height/2:
            self.is_here = False

width, height = 400,800
screen = pygame.display.set_mode((width,height))

particles = [Particle(width/2)]
probability = .001

while True:
    print(probability)
    if probability < .01:
        probability += .00000001
    # determine if a new particle will be added
    if random.random() < probability:
        particles.append(Particle(random.randint(0,width)))


    if len(particles) < 1:
        particles.append(Particle(random.randint(0,width)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((0,0,0))

    for p in particles:
        p.fall()
        p.show()
        p.check_bottom()
    
    for i in range(len(particles)-1, -1, -1):
        if not particles[i].is_here:
            del particles[i]

    pygame.display.flip()