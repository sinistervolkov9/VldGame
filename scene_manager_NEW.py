import sys
import pygame as pg
from settings import *
from markup import Markup
from button import Button


class Scene:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.screen = pg.display.set_mode((600, 400))
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.grid = Markup(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(60)  # Чилсо итераций (обновлений основного цикла игры за одну секунду)
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
        while True:
            self.check_events()
            self.update()
            self.draw()


# ----------------------------------------------------------------------------------------------------------------------

class SceneMainMenu(Scene):
    def __init__(self):
        super().__init__()

    def new_game(self):
        super().new_game()

        self.button_1 = Button(self, 'Кнопка!)', None, None, None, None, None, SCREEN_POS['c9'])
        self.button_2 = Button(self, 'Кнопка!)', None, None, None, None, None, SCREEN_POS['c21'])
        self.button_3 = Button(self, 'Кнопо4ка', None, None, None, None, None, SCREEN_POS['c33'])

        # ---

        self.vis = [self.button_1, self.button_2, self.button_3]
        self.novis = []

    def update(self):
        super().update()

        for btn in self.vis:
            btn.check_hover(pg.mouse.get_pos())


    def draw(self):
        super().draw()

        # self.buttonnn.draw()

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
                    self.vis.remove(i)
                    print(self.vis)
                    print(i)


class Scene2(Scene):
    def __init__(self):
        super().__init__()

    def new_game(self):
        super().new_game()

        self.button_1 = Button(self, 'Кн', None, None, None, None, None, SCREEN_POS['c9'])
        self.button_2 = Button(self, 'Кн', None, None, None, None, None, SCREEN_POS['c21'])
        self.button_3 = Button(self, 'Кн', None, None, None, None, None, SCREEN_POS['c33'])

        # ---

        self.vis = [self.button_1, self.button_2, self.button_3]
        self.novis = []

    def update(self):
        super().update()

        for btn in self.vis:
            btn.check_hover(pg.mouse.get_pos())


    def draw(self):
        super().draw()

        # self.buttonnn.draw()

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
                    self.vis.remove(i)
                    print(self.vis)
                    print(i)

    def change_to_novis(self, obj):
        pass

# ----------------------------------------------------------------------------------------------------------------------

scene_1 = SceneMainMenu()
scene_2 = Scene2()
scenes_list = [scene_2]

class SceneInitor:
    def __init__(self, scenes: list):
        self.scenes = scenes

        self.start_scene = self.scenes[0]

    def runnnn(self):
        for i in self.scenes:
            i.run()


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    game = SceneInitor(scenes_list)
    game.runnnn()


