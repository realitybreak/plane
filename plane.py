import pygame

class Plane():

    def __init__(self, p_settings, screen):
        """Initialize the plane and set its starting position."""
        self.screen = screen
        self.p_settings = p_settings

        # Load the plane image and get its rect
        self.image = pygame.image.load('images/plane.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the left center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the plane's center.
        self.center = float(self.rect.centery)
        
        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the plane's position based on the movement flag."""
        # Update the plane's center value, not the rect.
        if self.moving_up:
            self.center -= self.p_settings.plane_speed_factor
        if self.moving_down:
            self.center += self.p_settings.plane_speed_factor

        #Update rect object from self.center.
        self.rect.centery = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
