import sys
import pygame as pg
from settings import *
from button import Button
from scene import Scene


# ----------------------------------------------------------------------------------------------------------------------

class SceneMainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)

    def new_game(self):
        super().new_game()

        self.button_1 = Button(self, 'Кнопка!)', SCREEN_POS['t12'], None, None, None, None, None)
        self.button_2 = Button(self, 'Кнопка!)', SCREEN_POS['t21'], None, None, None, None, None)
        self.button_3 = Button(self, 'Кнопо4ка', SCREEN_POS['t33'], None, None, None, None, None)

        self.vis = [self.button_1, self.button_2, self.button_3]
        self.novis = []

    def update(self):
        super().update()

        for btn in self.vis:
            btn.check_hover(pg.mouse.get_pos())

    def draw(self):
        super().draw()

        for obj in self.vis:
            obj.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            for i in self.vis:
                i.handle_event(event)
                if event.type == pg.USEREVENT and event.button == i:
                    self.game.switch_scene()
                    # self.game.call_button_pos()

    def new_method(self):
        pass

# ----------------------------------------------------------------------------------------------------------------------

class Scene2(Scene):
    def __init__(self, game):
        super().__init__(game)

    def new_game(self):
        super().new_game()

        self.button_1 = Button(self, 'Кн', SCREEN_POS['b12'], None, None, None, None, None)
        self.button_2 = Button(self, 'Кн', SCREEN_POS['b22'], None, None, None, None, None)
        self.button_3 = Button(self, 'Кн', SCREEN_POS['b31'], None, None, None, None, None)

        self.vis = [self.button_1, self.button_2, self.button_3]
        self.novis = []

    def update(self):
        super().update()

        for btn in self.vis:
            btn.check_hover(pg.mouse.get_pos())

    def draw(self):
        super().draw()

        for i in self.vis:
            i.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            for i in self.vis:
                i.handle_event(event)
                if event.type == pg.USEREVENT and event.button == i:
                    self.game.switch_scene()

# ----------------------------------------------------------------------------------------------------------------------
