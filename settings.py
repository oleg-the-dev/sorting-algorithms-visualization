import pygame

pygame.init()


class Settings:
    # Window size
    WIDTH = 900
    HEIGHT = 600

    # Colors
    GRAPHITE = (30, 40, 45)
    BLUE = (0, 0, 205)
    RED = (255, 0, 0)
    BACKGROUND_COLOR = GRAPHITE
    GRADIENTS = (
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192),
    )

    # Data
    MIN_SIZE = 2
    MAX_SIZE = 700
    SIZE = 100
    MIN_VAL = 10
    MAX_VAL = 390

    # FPS
    MIN_FPS = 15
    MAX_FPS = 240
    FPS = 60
