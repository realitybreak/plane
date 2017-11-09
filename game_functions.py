import sys

import pygame

def check_events(plane):
    """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                plane.moving_up = True
            elif event.key == pygame.K_DOWN:
                plane.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                plane.moving_up = False
            elif event.key == pygame.K_DOWN:
                plane.moving_down = False
                

def update_screen(p_settings, screen, plane):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(p_settings.bg_color)
    plane.blitme()

    # Make the Most recently drawn screen visible.
    pygame.display.flip()
