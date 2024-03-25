import sys
import pygame as pg
from settings import *
from markup import Markup
from button import Button


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


# ----------------------------------------------------------------------------------------------------------------------

class SceneMainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)

    def new_game(self):
        super().new_game()

        self.button_1 = Button(self, 'Кнопка!)', SCREEN_POS['c9'], None, None, None, None, None)
        self.button_2 = Button(self, 'Кнопка!)', SCREEN_POS['c21'], None, None, None, None, None)
        self.button_3 = Button(self, 'Кнопо4ка', SCREEN_POS['c33'], None, None, None, None, None)

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


class Scene2(Scene):
    def __init__(self, game):
        super().__init__(game)

    def new_game(self):
        super().new_game()

        self.button_1 = Button(self, 'Кн', SCREEN_POS['c12'], None, None, None, None, None)
        self.button_2 = Button(self, 'Кн', SCREEN_POS['c22'], None, None, None, None, None)
        self.button_3 = Button(self, 'Кн', SCREEN_POS['c39'], None, None, None, None, None)


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


class Game:
    def __init__(self):
        self.current_scene = None
        # print(f'self.current_scene - {self.current_scene}')

        self.create_scenes()

    def create_scenes(self):  # А зачем этот матод? Можно все перевести в инит
        self.scene_1 = SceneMainMenu(self)
        self.scene_2 = Scene2(self)

        self.current_scene = self.scene_2

    def switch_scene(self):
        self.current_scene = self.scene_1

    def run_game(self):
        while True:
            self.current_scene.run()

    def call_button_pos(self):
        print(self.scene_1.button_1.pos)


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    game = Game()
    game.run_game()
