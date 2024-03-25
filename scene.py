import sys
import pygame as pg
from settings import FPS, RES
from markup import Markup


class Scene:
    def __init__(self, game):
        self.game = game
        pg.init()
        self.screen = pg.display.set_mode(RES)
        # self.screen = pg.display.set_mode(RES, pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.grid = Markup(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption("Vld Game")

    def draw(self):
        self.screen.fill("black")
        self.grid.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        self.check_events()
        self.update()
        self.draw()
