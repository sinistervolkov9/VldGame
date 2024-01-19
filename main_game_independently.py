import sys
from settings import *
import pygame as pg


class MainGame:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        #self.new_game()

