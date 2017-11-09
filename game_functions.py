import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, plane):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    plane.blitme()

    # Make the Most recently drawn screen visible.
    pygame.display.flip()
