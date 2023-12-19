import sys
import screen_manager_test as sm
import pygame as pg
from settings import *

pg.init()

screen_surface = pg.display.set_mode((WIDTH, HEIGHT))

scenes = [
    {sm.background_main_menu: [{sm.button_new_game: sm.background_new_game}, {sm.button_settings: sm.background_settings}, {sm.button_exit: sm.background_is_exit}]},
    {sm.background_new_game: []},
    {sm.background_settings: [{sm.button_settings_game: None}, {sm.button_settings_audio: None}, {sm.button_settings_video: None}]},
    {sm.background_is_exit: [sm.button_yes, sm.button_no]}
]

current_screen = sm.background_main_menu
current_buttons = []
current_buttons_only = []

for scene in scenes:
    print("1")
    for screen, buttons in scene.items():
        print("2")
        if screen == current_screen:
            print("3")
            for button in buttons:
                print("4")
                current_buttons.append(button)
                print(current_buttons)
                break

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

        for button in current_buttons:
            for but, swithc_screen in button.items():
                # current_buttons_only.append(but)
                # break
                if event.type == pg.USEREVENT and event.button == but:
                    running = False
                    current_screen = swithc_screen

                for button in current_buttons_only:
                    button.handle_event(event)

    for button in current_buttons_only:
        button.check_hover(pg.mouse.get_pos())
        button.draw(screen_surface)

    pg.display.flip()