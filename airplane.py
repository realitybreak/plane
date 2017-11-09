import sys

import pygame

from settings import Settings
from plane import Plane

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Airplane")

    # Make a plane
    plane = Plane(screen)

    # Set the background color.
    bg_color = (135, 206, 250)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        plane.blitme()

        # Make the Most recently drawn screen visible.
        pygame.display.flip()

run_game()