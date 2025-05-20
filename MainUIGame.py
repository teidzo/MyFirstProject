import pygame
from ConstantsinGame import *


class UI:
    def __init__(self, x, y, width, height, text, color=Green, hover_color=(100, 255, 100)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover.color = hover_color
        self.is_hovered = False
        self.font = pygame.font.SysFont('Arial', 30)

