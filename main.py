import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Cashew Jelly")
icon = pygame.image.load("cashewjellylogo.png")
pygame.display.set_icon(icon)
fps = 60
timer = pygame.time.Clock()
screen.fill('Light Blue')
timer.tick(fps)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()