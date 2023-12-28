import sys
import TEST_screen_manager as sm
import pygame as pg
from settings import *

pg.init()

screen_surface = pg.display.set_mode((WIDTH, HEIGHT))

# Лучше назвать "сценарии" или тип того
# scenesss = [{scene1: [{screens: [{scr1: anim1}, {scr2: anim2}], {buttons: [{bt1: scr2}]}]}]
scenes = [
    {sm.background_main_menu: [{sm.button_new_game: sm.background_new_game}, {sm.button_settings: sm.background_settings}, {sm.button_exit: sm.background_is_exit}]},
    {sm.background_new_game: [{}]},
    {sm.background_settings: [{sm.button_settings_game: None}, {sm.button_settings_audio: None}, {sm.button_settings_video: None}]},
    {sm.background_is_exit: [{sm.button_yes: None}, {sm.button_no: sm.background_main_menu}]}
]

history_scr = []
current_screen = sm.background_main_menu
buttons_swh = []
displayed_buttons = []

history_scr.append(current_screen)

for scene in scenes:
    print("1")
    for screen, buttons in scene.items():
        print("2")
        if screen == current_screen:
            print("3")
            for button in buttons:
                print("4")
                buttons_swh.append(button)

for button in buttons_swh:
    for but, scr in button.items():
        displayed_buttons.append(but)

print(buttons_swh)
print(displayed_buttons)
print(history_scr)


# -----------------------------------------------

running = True
while running:
    current_screen.update(screen_surface)
    current_screen.draw(screen_surface)
    current_screen.handle_event()

    # -----------------------------------------------

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.USEREVENT and event.button in displayed_buttons:
            for user_button in displayed_buttons:
                if event.type == pg.USEREVENT and event.button == user_button:
                    print(user_button)
                    for button in buttons_swh:
                        for but, scr in button.items():
                            if user_button == but:
                                current_screen = scr
                                buttons_swh = []
                                displayed_buttons = []

                                for scene in scenes:
                                    print("1")
                                    for screen, buttons in scene.items():
                                        print("2")
                                        if screen == current_screen:
                                            print("3")
                                            for button in buttons:
                                                print("4")
                                                buttons_swh.append(button)

                                for button in buttons_swh:
                                    for but, scr in button.items():
                                        displayed_buttons.append(but)

                                print(buttons_swh)
                                print(displayed_buttons)

        for button in displayed_buttons:
            button.handle_event(event)

    for button in displayed_buttons:
        button.check_hover(pg.mouse.get_pos())
        button.draw(screen_surface)

    pg.display.flip()

# -----------------------------------------------

class Screen:
    def __init__(self, game):
        self.game = game

    def screen_switcher(self):
        pass

    def handle_event(self):
        pass

    def draw(self):
        current_screen.draw(screen_surface)

    def update(self):
        current_screen.update(screen_surface)
        current_screen.handle_event()
