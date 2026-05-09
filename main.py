import pygame
import os

BASE_DIR = os.path.dirname(__file__)
font_path = os.path.join(BASE_DIR, "fonts", "Minecraft.ttf")

pygame.init()

font_title = pygame.font.Font(font_path, 80)
font_button = pygame.font.Font(font_path, 40)

game_state = "menu"   # ← começa no menu

screen = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Cashew Jelly")
icon = pygame.image.load("cashewjellylogo.png")
pygame.display.set_icon(icon)
fps = 60
timer = pygame.time.Clock()
screen.fill('Light Blue')
timer.tick(fps)


running = True

def draw_menu():
    screen.fill((135, 206, 250))  # azul claro

    # Título
    title_text = font_title.render("Cashew Jelly", True, (255,255,255))
    screen.blit(title_text, (420, 150))

    # Botão START
    start_button = pygame.Rect(540, 350, 200, 80)
    pygame.draw.rect(screen, (60, 180, 75), start_button)

    start_text = font_button.render("START", True, (255,255,255))
    screen.blit(start_text, (580, 370))

    return start_button
def draw_game():
    screen.fill((50, 170, 90))
    
    text = font_button.render("JOGO INICIADO!", True, (255,255,255))
    screen.blit(text, (500, 350))

running = True
while running:
    timer.tick(fps)

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ESTADOS DO JOGO
    if game_state == "menu":
        start_button = draw_menu()

        # clicar no botão start
        if start_button.collidepoint(mouse_pos) and mouse_click:
            game_state = "game"

    elif game_state == "game":
        draw_game()

    pygame.display.update()