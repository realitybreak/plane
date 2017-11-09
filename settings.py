class Settings():
    """A class to store all settings for airplane."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 250)

        # plane settings.
        self.plane_speed_factor = 1.5