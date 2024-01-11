# import pygame as pg
from settings import *
from button import Button
from screen import Screen
from event import Event
from screen_item import ScreenItem

# pg.init()

# screen_surface = pg.display.set_mode((WIDTH, HEIGHT))


# pg.display.set_caption("test")



screen_0 = Screen("default_background.jpg",
                    0, 0, WIDTH, HEIGHT,
                    "screen_0",
                    None, "white", 50)

# Кнопка "Новая игра"
# Перехов в окно "Новая игра"
button_1 = Button("to_scr_1", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 100, 200, 60)

# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_2 = Button("to_scr_2", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_3 = Button("to_scr_3", None,
                     "white", "brown", "green",
                     "b.png", "g.png", "r.png",
                     "dig_click_03.wav", "mouse_click_04.wav",
                     WIDTH / 2 - (200 / 2), 240, 200, 60)

screen_1 = Screen("default_background.jpg",
                    0, 0, WIDTH, HEIGHT,
                    "screen_1",
                    None, "white", 50)

button_1_1 = Button("to_scr_4", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 170, 200, 60)

screen_2 = Screen("default_background.jpg",
                    0, 0, WIDTH, HEIGHT,
                    None,
                    "screen_2", "white", 50)

button_2_1 = Button("Общие", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 100, 200, 60)
# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_2_2 = Button("Аудио", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_2_3 = Button("Видео", None,
                     "white", "brown", "green",
                     "b.png", "g.png", "r.png",
                     "dig_click_03.wav", "mouse_click_04.wav",
                     WIDTH / 2 - (200 / 2), 240, 200, 60)

screen_3 = Screen("background.jpg",
                    WIDTH * 0.2 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.2, HEIGHT - HEIGHT * 0.4,
                    "screen_3",
                    None, "white", 50)

# Кнопка "Да"
# Подтверждение выхода
button_3_1 = Button("exit", None,
                    "white", "black", "green",
                    "b.png", "g.png", "r.png",
                    "dig_click_03.wav", "mouse_click_04.wav",
                    (WIDTH + WIDTH * 0.2 / 2) / 8, 200, 200, 60)
# Кнопка "Нет"
# Вернуться назад в меню
button_3_2 = Button("to_scr_0", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   (WIDTH + WIDTH * 0.2 / 2) / 2, 200, 200, 60)

screen_4 = Screen("background.jpg",
                    WIDTH * 0.5 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.5, HEIGHT - HEIGHT * 0.4,
                    "screen_4",
                    None, "white", 50)

# Кнопка "Продолжить"
# Вернуться в игру
button_4_1 = Button("to_scr_1", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выйти в главное меню"
# Перейти в главное меню
button_4_2 = Button("to_scr_0", None,
                          "white", "black", "green",
                          "b.png", "g.png", "r.png",
                          "dig_click_03.wav", "mouse_click_04.wav",
                          WIDTH / 2 - (200 / 2), 240, 200, 60)

# ---

event_1 = Event(game=None)

# item_1 = ScreenItem("r", 0, 0, 20, 20, None, None, None, None)

# ----------------------------------------------------------------------------------------------------------------------


# start_screen = None
#
#
# def start_game(screen):
#     global start_screen
#     start_screen = screen
#     # pass
