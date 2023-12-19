import pygame as pg
from settings import *
from button import Button
from screen import Screen

# pg.init()

screen_surface = pg.display.set_mode((WIDTH, HEIGHT))


# pg.display.set_caption("test")



background_main_menu = Screen("default_background.jpg",
                    0, 0, WIDTH, HEIGHT,
                    None,
                    "МЕНЮ", None, "white",
                    50)

# Кнопка "Новая игра"
# Перехов в окно "Новая игра"
button_new_game = Button("Новая игра", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 100, 200, 60)
# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_settings = Button("Настройки", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_exit = Button("Выход", None,
                     "white", "brown", "green",
                     "b.png", "g.png", "r.png",
                     "dig_click_03.wav", "mouse_click_04.wav",
                     WIDTH / 2 - (200 / 2), 240, 200, 60)

background_new_game = Screen("default_background.jpg",
                    0, 0, WIDTH, HEIGHT,
                    None,
                    "ИГРА...", None, "white",
                    50)

background_settings = Screen("default_background.jpg",
                    0, 0, WIDTH, HEIGHT,
                    None,
                    "НАСТРОЙКИ", None, "white",
                    50)

button_settings_game = Button("Общие", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 100, 200, 60)
# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_settings_audio = Button("Аудио", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_settings_video = Button("Видео", None,
                     "white", "brown", "green",
                     "b.png", "g.png", "r.png",
                     "dig_click_03.wav", "mouse_click_04.wav",
                     WIDTH / 2 - (200 / 2), 240, 200, 60)

background_is_exit = Screen("background.jpg",
                    WIDTH * 0.2 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.2, HEIGHT - HEIGHT * 0.4,
                    None,
                    "ВЫЙТИ ИЗ ИГРЫ?", None, "white",
                    50)

# Кнопка "Да"
# Подтверждение выхода
button_yes = Button("Да", None,
                    "white", "black", "green",
                    "b.png", "g.png", "r.png",
                    "dig_click_03.wav", "mouse_click_04.wav",
                    (WIDTH + WIDTH * 0.2 / 2) / 8, 200, 200, 60)
# Кнопка "Нет"
# Вернуться назад в меню
button_no = Button("Нет", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   (WIDTH + WIDTH * 0.2 / 2) / 2, 200, 200, 60)

background_pause = Screen("background.jpg",
                    WIDTH * 0.5 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.5, HEIGHT - HEIGHT * 0.4,
                    None,
                    "ПАУЗА", None, "white",
                    50)

# Кнопка "Продолжить"
# Вернуться в игру
button_continue = Button("Продолжить", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выйти в главное меню"
# Перейти в главное меню
button_main_menu = Button("В главное меню", None,
                          "white", "black", "green",
                          "b.png", "g.png", "r.png",
                          "dig_click_03.wav", "mouse_click_04.wav",
                          WIDTH / 2 - (200 / 2), 240, 200, 60)

# ----------------------------------------------------------------------------------------------------------------------


# start_screen = None
#
#
# def start_game(screen):
#     global start_screen
#     start_screen = screen
#     # pass
