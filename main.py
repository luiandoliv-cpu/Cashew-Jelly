import pygame
import os

screen = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Cashew Jelly")
fps = 60
timer = pygame.time.Clock()
timer.tick(fps)

BASE_DIR = os.path.dirname(__file__)
font_path = os.path.join(BASE_DIR, "fonts", "Minecraft.ttf")
icon_path = os.path.join(BASE_DIR, "assets", "cashewjellylogo.png")
icon = pygame.image.load(icon_path)
telinha = pygame.image.load("manoteste1.png")
exitrect = pygame.Rect(548, 589, 176, 88)
pygame.display.set_icon(icon)

pygame.init()

font_title = pygame.font.Font(font_path, 80)
font_button = pygame.font.Font(font_path, 40)

game_state = "menu"

running = True

running = True
while running:
    timer.tick(fps)

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if exitrect.collidepoint(event.pos):
                    running = False

    screen.blit(telinha, (0, 0))
    pygame.display.flip()
    pygame.display.update()