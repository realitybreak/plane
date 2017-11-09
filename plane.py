import pygame

class Plane():

    def __init__(self, screen):
        """Initialize the plane and set its starting position."""
        self.screen = screen

        # Load the plane image and get its rect
        self.image = pygame.image.load('images/plane.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the left center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the plane's position based on the movement flag."""
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
