import pygame
import sys
from battlefield_screen import battlefield_screen
from map_screen import map_screen
from start_screen import start_screen

# define game states
START_SCREEN = 0
MAP_SCREEN = 1
BATTLE_SCREEN = 2

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("EVEN Steven Beats ODDS")

# game loop
run = True
current_screen = START_SCREEN

while run:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if current_screen == START_SCREEN:
            current_screen = start_screen(
                screen, MAP_SCREEN, START_SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                current_screen = MAP_SCREEN
        elif current_screen == MAP_SCREEN:
            current_screen = map_screen()
        elif current_screen == BATTLE_SCREEN:
            current_screen = battlefield_screen(screen)

    # Render game elements for the current screen
    pygame.display.update()  # Update display

# exit pygame
pygame.quit()
sys.exit()
