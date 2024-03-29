from settings import SCREEN_POS
from scene import Scene
from button import Button
from screen import Screen


# ----------------------------------------------------------------------------------------------------------------------

class SceneMainMenu(Scene):
    def __init__(self, game):
        self.click_count = 0
        super().__init__(game)

    def declare_content(self):
        super().declare_content()

        self.screen_main = Screen(self, None, None, None, False, False)
        self.screen_2 = Screen(self, None, None, 'resources/backgrounds/background_2.png', False, True)

        self.button_1 = Button(self, 'print_event', SCREEN_POS['tl11'])
        self.button_2 = Button(self, 'switch_scene', SCREEN_POS['tl31'])
        self.button_3 = Button(self, 'switch_visibility_1', SCREEN_POS['bl31'])
        self.button_4 = Button(self, 'switch_visibility_2', SCREEN_POS['bl11'])
        self.button_5 = Button(self, 'make_visible', SCREEN_POS['tl13'])
        self.button_6 = Button(self, 'make_invisible', SCREEN_POS['tl33'])
        self.button_7 = Button(self, 'click_count', SCREEN_POS['bl33'])
        self.button_8 = Button(self, 'set_count', SCREEN_POS['bl13'])
        self.button_9 = Button(self, 'switch_activity', SCREEN_POS['tr13'])
        self.button_10 = Button(self, 'switch_scr_1', SCREEN_POS['tr33'])
        self.button_11 = Button(self, 'switch_scr_2', SCREEN_POS['br33'])

        self.print_event_1 = "Кнопка 1"
        self.print_event_2 = "click_count"

        # ---

        self.scene_content = [
            {'screens': [
                self.screen_main, self.screen_2
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
                    {'change_screen_to': self.screen_main},
                ]},
                {self.button_11: [
                    {'change_screen_to': self.screen_2},
                ]},
            ]}
        ]

        # ---

        self.current_screen = self.screen_main
        self.visible_content = [self.screen_main, self.button_1, self.button_2, self.button_3, self.button_5,
                                self.button_6, self.button_7, self.button_9, self.button_10, self.button_11]
        self.invisible_content = []
        self.active_content = [self.screen_main, self.button_1, self.button_2, self.button_3, self.button_5,
                               self.button_6, self.button_7, self.button_9, self.button_10, self.button_11]

    def userevent_applying(self, action_name, action_object):
        super().userevent_applying(action_name, action_object)

        if action_object == self.print_event_2:
            self.click_count += 1
            if self.click_count >= 3:
                self.switch_visibility([self.button_7, self.button_8])
                print(f'set_count\nself.click_count = 0')
                self.click_count = 0


# ----------------------------------------------------------------------------------------------------------------------

class SceneNext(Scene):
    def __init__(self, game):
        super().__init__(game)

    def declare_content(self):
        super().declare_content()

        self.button_21 = Button(self, 'back', SCREEN_POS['c'], None, None, None, True, True)

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
