import sys

import pygame

from settings import Settings
from plane import Plane
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    p_settings = Settings()
    screen = pygame.display.set_mode(
        (p_settings.screen_width, p_settings.screen_height))
    pygame.display.set_caption("Airplane")

    # Make a plane
    plane = Plane(screen)

    # Set the background color.
    bg_color = (135, 206, 250)

    # Start the main loop for the game.
    while True:
        gf.check_events(plane)
        gf.update_screen(p_settings, screen, plane)
        
run_game()
