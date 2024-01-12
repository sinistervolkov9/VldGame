from settings import *
from button import Button
from screen import Screen
from event import Event
# from screen_item import ScreenItem

# ----------------------------------------------------------------------------------------------------------------------

screen_0_main = Screen("default_background.jpg",
                       0, 0, WIDTH, HEIGHT,
                       "МЕНЮ",
                       None, "white", 50)

screen_1_new_game = Screen("default_background.jpg",
                           0, 0, WIDTH, HEIGHT,
                           "ИГРА ТИПА...",
                           None, "white", 50)

screen_2_settings = Screen("default_background.jpg",
                           0, 0, WIDTH, HEIGHT,
                           "НАСТРОЙКИ",
                           None, "white", 50)

screen_3_exit = Screen("background.jpg",
                       WIDTH * 0.2 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.2, HEIGHT - HEIGHT * 0.4,
                       "ВЫЙТИ?",
                       None, "white", 50)

screen_4_pause = Screen("background.jpg",
                        WIDTH * 0.5 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.5, HEIGHT - HEIGHT * 0.4,
                        "ПАУЗА",
                        None, "white", 50)

# ----------------------------------------------------------------------------------------------------------------------

# Кнопка "Новая игра"
# Перехов в окно "Новая игра"
button_00_new_game = Button("НОВАЯ ИГРА", None,
                            "white", "black", "green",
                            "b.png", "g.png", "r.png",
                            "dig_click_03.wav", "mouse_click_04.wav",
                            WIDTH / 2 - (200 / 2), 100, 200, 60)

# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_01_settings = Button("НАСТРОЙКИ", None,
                            "white", "black", "green",
                            "b.png", "g.png", "r.png",
                            "dig_click_03.wav", "mouse_click_04.wav",
                            WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_02_exit = Button("ВЫХОД", None,
                        "white", "brown", "green",
                        "b.png", "g.png", "r.png",
                        "dig_click_03.wav", "mouse_click_04.wav",
                        WIDTH / 2 - (200 / 2), 240, 200, 60)

button_10_click = Button("должна быть кнопка хода", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         WIDTH / 2 - (300 / 2), 170, 300, 60)

button_20 = Button("Общие", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   WIDTH / 2 - (200 / 2), 100, 200, 60)
# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_21 = Button("Аудио", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_22 = Button("Видео", None,
                   "white", "brown", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   WIDTH / 2 - (200 / 2), 240, 200, 60)

# Кнопка "Да"
# Подтверждение выхода
button_30 = Button("ДА", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   (WIDTH + WIDTH * 0.2 / 2) / 8, 200, 200, 60)
# Кнопка "Нет"
# Вернуться назад в меню
button_31 = Button("НЕТ", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   (WIDTH + WIDTH * 0.2 / 2) / 2, 200, 200, 60)

# Кнопка "Продолжить"
# Вернуться в игру
button_40 = Button("ПРОДОЛЖИТЬ", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выйти в главное меню"
# Перейти в главное меню
button_41 = Button("В МЕНЮ", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   WIDTH / 2 - (200 / 2), 240, 200, 60)

# ----------------------------------------------------------------------------------------------------------------------

event_1 = Event(game=None)

# ----------------------------------------------------------------------------------------------------------------------

# item_1 = ScreenItem("r", 0, 0, 20, 20, None, None, None, None)

# ----------------------------------------------------------------------------------------------------------------------

scenes = [
    {"scene_0":
        [
            {"screen": screen_0_main},
            {"buttons": [{button_00_new_game: "scene_1"}, {button_01_settings: "scene_2"},
                         {button_02_exit: "scene_3"}]},
            {"events": []},
            {"esc_screen": "scene_3"},
            {"items": []}
        ]
    },
    {"scene_1":
        [
            {"screen": screen_1_new_game},
            {"buttons": [{button_10_click: "scene_4"}]},
            {"events": [event_1]},
            {"esc_screen": "scene_4"},
            {"items": []}
        ]
    },
    {"scene_2":
        [
            {"screen": screen_2_settings},
            {"buttons": [{button_20: None}, {button_21: None}, {button_22: None}]},
            {"events": []},
            {"esc_screen": None},
            {"items": []}
        ]
    },
    {"scene_3":
        [
            {"screen": screen_3_exit},
            {"buttons": [{button_30: None}, {button_31: "scene_0"}]},
            {"events": []},
            {"esc_screen": "scene_0"},
            {"items": []}
        ]
    },
    {"scene_4":
        [
            {"screen": screen_4_pause},  # 4. item in scene_items_list {k: v}
            {"buttons": [{button_40: "scene_1"}, {button_41: "scene_0"}]},
            {"events": []},
            {"esc_screen": "scene_1"},
            {"items": []}
        ]
    }
]

# ----------------------------------------------------------------------------------------------------------------------
