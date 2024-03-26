import pygame as pg
from settings import SCREEN_POS
from scene import Scene
from button import Button
from screen import Screen
from print_event import PrintEvent


# ----------------------------------------------------------------------------------------------------------------------

class SceneMainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)

    def declare_content(self):
        super().declare_content()

        self.screen_main = Screen(self, None, None, None)
        self.button_1 = Button(self, 'Кнопка 1', SCREEN_POS['tc3'], None, None, None, None, None)
        self.button_2 = Button(self, 'Кнопка 2', SCREEN_POS['bc3'], None, None, None, None, None)
        self.button_3 = Button(self, 'Сменить сцену', SCREEN_POS['bc1'], None, None, None, None, None)
        self.print_event_1 = PrintEvent("Кнопка 1")
        self.print_event_2 = PrintEvent("Кнопка 2")

        # ---

        self.scene_content = [
            {'screens': [
                self.screen_main
            ]},
            {'buttons': [
                {self.button_1: [
                    {'print_event': self.print_event_1},
                ]},
                {self.button_2: [
                    {'print_event': self.print_event_2},
                ]},
                {self.button_3: [
                    {'switch_scene': 'scene_2'},
                ]}
            ]}
        ]

        self.visible_content = [self.screen_main, self.button_1, self.button_2, self.button_3]
        self.invisible_content = []

    def content_unpacking(self):
        super().content_unpacking()

        pass

    def update(self):
        super().update()

        for btn in self.visible_content:
            btn.check_hover(pg.mouse.get_pos())

    def draw(self):
        super().draw()

        for obj in self.visible_content:
            obj.draw()

    def new_method(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------

class SceneNext(Scene):
    def __init__(self, game):
        super().__init__(game)

    def declare_content(self):
        super().declare_content()

        self.button_21 = Button(self, 'Кн', SCREEN_POS['tc1'], None, None, None, None, None)

        # ---

        self.scene_content = [
            {'screens': [
                None
            ]},
            {'buttons': [
                {self.button_21: [
                    {'switch_scene': 'scene_1'},
                ]}
            ]}
        ]
        self.visible_content = [self.button_21]
        self.invisible_content = []

    def update(self):
        super().update()

        for btn in self.visible_content:
            btn.check_hover(pg.mouse.get_pos())

    def draw(self):
        super().draw()

        for obj in self.visible_content:
            obj.draw()


# ----------------------------------------------------------------------------------------------------------------------
