import pygame
from pygame.draw import *

pygame.init()

black = 0, 0, 0
white = 255, 255, 255
light_grey = 220, 220, 220
grey = 192, 192, 192
dark_grey = 60, 60, 60
red = 255, 0, 0
purple = 160, 35, 255
pink = 255, 96, 208
light_green = 96, 255, 128
green = 0, 255, 0
light_blue = 80, 208, 255
blue = 0, 0, 255
yellow = 225, 225, 0
orange = 255, 160, 20
brown = 160, 130, 100

FPS = 30
screen = pygame.display.set_mode((600, 600))

x1 = 100
y1 = 100
x2 = 500
y2 = 200
N = 15

rect(screen, blue, (x1, y1, x2 - x1, y2 - y1), 4)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, orange, (x, y1), (x, y2), 5)
    x += h

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()