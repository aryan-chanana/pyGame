import pygame
from pygame import *

pygame.init()

screen = pygame.display.set_mode((800,600))
background = pygame.image.load('D:\\Temp. Folder\\Programming\\Python\\Pygame space\\background.png')   
x = 0

running = True
while running:
    rectangle = x%background.get_rect().width
    screen.blit(background, (rectangle - background.get_rect().width,0))
    if rectangle<800:
        screen.blit(background, (rectangle,0))
    x -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()