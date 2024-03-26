import pygame as pg
from settings import SCREEN_POS
from scene import Scene
from button import Button
from screen import Screen
from print_event import PrintEvent


# ----------------------------------------------------------------------------------------------------------------------

class SceneMainMenu(Scene):
    def __init__(self, game):
        self.click_count = 0
        super().__init__(game)

    def declare_content(self):
        super().declare_content()

        self.screen_main = Screen(self, None, None, None)
        self.button_1 = Button(self, 'PrintEvent', SCREEN_POS['tl11'], None, None, None, None, None)
        self.button_2 = Button(self, 'switch_scene', SCREEN_POS['tl31'], None, None, None, None, None)
        self.button_3 = Button(self, 'switch_visibility', SCREEN_POS['bl31'], None, None, None, None, None)
        self.button_4 = Button(self, 'sw_vis_scene', SCREEN_POS['bl11'], None, None, None, None, None)
        self.button_5 = Button(self, 'make_visible', SCREEN_POS['tl13'], None, None, None, None, None)
        self.button_6 = Button(self, 'make_invisible', SCREEN_POS['tl33'], None, None, None, None, None)
        self.button_7 = Button(self, 'click_count', SCREEN_POS['bl33'], None, None, None, None, None)
        self.button_8 = Button(self, 'set_count', SCREEN_POS['bl13'], None, None, None, None, None)
        self.button_9 = Button(self, 'switch_activity', SCREEN_POS['tr13'], None, None, None, None, None)
        self.button_10 = Button(self, 'PrintEvent', SCREEN_POS['tr33'], None, None, None, None, None)
        self.print_event_1 = PrintEvent("Кнопка 1")
        self.print_event_2 = PrintEvent(f"click_count")
        self.print_event_3 = PrintEvent(f"Кнопка 10")

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
                    {'switch_scene': 'scene_2'},
                ]},
                {self.button_3: [
                    {'switch_visibility': [self.button_3, self.button_4]},
                ]},
                {self.button_4: [
                    {'switch_visibility': [self.button_3, self.button_4]},
                    {'switch_scene': 'scene_2'},
                ]},
                {self.button_5: [
                    {'make_visible': [self.button_3]},
                ]},
                {self.button_6: [
                    {'make_invisible': [self.button_4]},
                ]},
                {self.button_7: [
                    {'print_event': self.print_event_2},
                ]},
                {self.button_8: [
                    {'switch_visibility': [self.button_7, self.button_8]},
                ]},
                {self.button_9: [
                    {'switch_activity': [self.button_10]},
                ]},
                {self.button_10: [
                    {'print_event': self.print_event_3},
                ]},
            ]}
        ]

        # ---

        self.visible_content = [self.screen_main, self.button_1, self.button_2, self.button_3, self.button_5,
                                self.button_6, self.button_7, self.button_9, self.button_10]
        self.invisible_content = [self.button_4, self.button_8]
        # self.active_content = self.visible_content
        self.active_content = [self.screen_main, self.button_1, self.button_2, self.button_3, self.button_4,
                               self.button_5, self.button_6, self.button_7, self.button_8, self.button_9,
                               self.button_10]

    def userevent_applying(self, action_name, action_object):
        super().userevent_applying(action_name, action_object)

        if action_object == self.print_event_2:
            self.click_count += 1
            print(self.click_count)
            if self.click_count >= 3:
                print(f'self.click_count >= 3')
                if self.button_7 in self.all_scene_objects:
                    print(f'self.button_7 in self.all_scene_objects')
                    if self.button_7 in self.visible_content:
                        print(f'self.button_7 in self.visible_content')
                        self.visible_content.remove(self.button_7)
                        if self.button_7 not in self.invisible_content:
                            print(f'self.button_7 not in self.invisible_content')
                            self.invisible_content.append(self.button_7)
                            print(self.button_7)
                            print(self.invisible_content)

                if self.button_8 in self.all_scene_objects:
                    print(f'self.button_8 in self.all_scene_objects')
                    if self.button_8 in self.invisible_content:
                        print(f'self.button_8 in self.invisible_content')
                        self.invisible_content.remove(self.button_8)
                        if self.button_8 not in self.visible_content:
                            print(f'self.button_8 not in self.visible_content')
                            self.visible_content.append(self.button_8)
                            print(self.button_8)
                            print(self.visible_content)

        if action_name == 'switch_visibility':
            for obj in action_object:
                if obj == self.button_8:
                    print(f'set_count\nself.click_count = 0')
                    self.click_count = 0


# ----------------------------------------------------------------------------------------------------------------------

class SceneNext(Scene):
    def __init__(self, game):
        super().__init__(game)

    def declare_content(self):
        super().declare_content()

        self.button_21 = Button(self, 'back', SCREEN_POS['c'], None, None, None, None, None)

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
        self.active_content = [self.button_21]

# ----------------------------------------------------------------------------------------------------------------------
