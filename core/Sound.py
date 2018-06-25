import pygame


class Sound:
    """Class to manage sound and special effects"""

    def __init__(self):
        self.master_volume = 100
        self.music_volume = 100
        self.effects_volume = 100
        self.music = "musique"

    def generate_sound(self):
        sound = pygame.mixer.Sound("./assets/music_1.wav")
        sound.play()
        self.master_volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(10)
