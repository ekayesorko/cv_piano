
from pygame import init


import pygame
import pygame.mixer

pygame.mixer.init(frequency=22050)
m = pygame.mixer.Sound('sounds/A5.wav')
m2 = pygame.mixer.Sound('sounds/A5.wav')
m.play(2)
for i in range(2000000):
    if i%1000 == 1: continue
    print(pygame.mixer.get_busy())
    if(i == 100000):
        m2.play()
    