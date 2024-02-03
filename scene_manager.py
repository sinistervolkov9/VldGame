from settings import *
from button import Button
from screen import Screen
from print_event import PrintEvent

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

screen_5 = Screen("background.jpg",
                  0, 0, 100, HEIGHT,
                  "тест",
                  None, "white", 50, visible=False)

# ----------------------------------------------------------------------------------------------------------------------

# Кнопка "Новая игра"
# Перехов в окно "Новая игра"
button_00_new_game = Button("Новая игра", None,
                            "white", "black", "green",
                            "b.png", "g.png", "r.png",
                            "dig_click_03.wav", "mouse_click_04.wav",
                            WIDTH / 2 - (200 / 2), 100, 200, 60)

# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_01_settings = Button("Настройки", None,
                            "white", "black", "green",
                            "b.png", "g.png", "r.png",
                            "dig_click_03.wav", "mouse_click_04.wav",
                            WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_02_exit = Button("Выход", None,
                        "white", "brown", "green",
                        "b.png", "g.png", "r.png",
                        "dig_click_03.wav", "mouse_click_04.wav",
                        WIDTH / 2 - (200 / 2), 240, 200, 60)

button_10_pause = Button("<", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         20, 20, 60, 60)

button_11_turn_1 = Button("Ход", None,
                          "white", "black", "green",
                          "b.png", "g.png", "r.png",
                          "dig_click_03.wav", "mouse_click_04.wav",
                          WIDTH / 2 - (200 / 2), 170, 200, 60)

button_11_turn_2 = Button("Ход", None,
                          "white", "black", "green",
                          "b.png", "g.png", "r.png",
                          "dig_click_03.wav", "mouse_click_04.wav",
                          WIDTH / 2 - (200 / 2), 250, 200, 60, visible=False)

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

button_23_back = Button("<", None,
                        "white", "black", "green",
                        "b.png", "g.png", "r.png",
                        "dig_click_03.wav", "mouse_click_04.wav",
                        20, 20, 60, 60)

# Кнопка "Да"
# Подтверждение выхода
button_30 = Button("Да", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   (WIDTH + WIDTH * 0.2 / 2) / 8, 200, 200, 60)
# Кнопка "Нет"
# Вернуться назад в меню
button_31 = Button("Нет", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   (WIDTH + WIDTH * 0.2 / 2) / 2, 200, 200, 60)

# Кнопка "Продолжить"
# Вернуться в игру
button_40 = Button("Продолжить", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выйти в главное меню"
# Перейти в главное меню
button_41 = Button("В меню", None,
                   "white", "black", "green",
                   "b.png", "g.png", "r.png",
                   "dig_click_03.wav", "mouse_click_04.wav",
                   WIDTH / 2 - (200 / 2), 240, 200, 60)

# ----------------------------------------------------------------------------------------------------------------------

print_event_0 = PrintEvent("Новая игра")
print_event_1 = PrintEvent("Ход")
print_event_2 = PrintEvent("В разработке")

# ----------------------------------------------------------------------------------------------------------------------

# item_1 = ScreenItem("r", 0, 0, 20, 20, None, None, None, None)

# ----------------------------------------------------------------------------------------------------------------------

scenes = [
    {"scene_0":
        [
            {"screen": [screen_0_main]},
            {"buttons":
                [
                    {button_00_new_game:
                        [
                            {"change_scene": "scene_1"},
                            {"print_text": print_event_0}
                        ]
                    },
                    {button_01_settings:
                        [
                            {"change_scene": "scene_2"},
                        ]
                    },
                    {button_02_exit:
                        [
                            {"change_scene": "scene_3"},
                        ]
                    }
                ]
            },
            {"esc_screen": "scene_3"}
        ]
    },
    {"scene_1":
        [
            {"screen": [screen_1_new_game, screen_5]},
            {"buttons":
                [
                    {button_10_pause:
                        [
                            {"change_scene": "scene_4"},
                        ]
                    },
                    {button_11_turn_1:
                        [
                            {"print_text": print_event_1},
                            {"switch_visibility": [button_11_turn_1, button_11_turn_2, screen_5]},
                            {"switch_activity": [button_10_pause]}
                        ]
                    },
                    {button_11_turn_2:
                        [
                            {"print_text": print_event_1},
                            {"switch_visibility": [button_11_turn_1, button_11_turn_2, screen_5]},
                            {"switch_activity": [button_10_pause]}
                        ]
                    }
                ]
            },
            {"esc_screen": "scene_4"}
        ]
    },
    {"scene_2":
        [
            {"screen": [screen_2_settings]},
            {"buttons":
                [
                    {button_20:
                        [
                            {"print_text": print_event_2}
                        ]
                    },
                    {button_21:
                        [
                            {"print_text": print_event_2}
                        ]
                    },
                    {button_22:
                        [
                            {"print_text": print_event_2}
                        ]
                    },
                    {button_23_back:
                        [
                            {"change_scene": "scene_0"}
                        ]
                    }
                ]
            },
            {"esc_screen": "scene_0"}
        ]
    },
    {"scene_3":
        [
            {"screen": [screen_3_exit]},
            {"buttons":
                [
                    {button_30:
                        [
                            {"change_scene": None}
                        ]
                    },
                    {button_31:
                        [
                            {"change_scene": "scene_0"}
                        ]
                    }
                ]
            },
            {"esc_screen": "scene_0"}
        ]
    },
    {"scene_4":
        [
            {"screen": [screen_4_pause]},
            {"buttons":
                [
                    {button_40:
                        [
                            {"change_scene": "scene_1"}
                        ]
                    },
                    {button_41:
                        [
                            {"change_scene": "scene_0"}
                        ]
                    }
                ]
            },
            {"esc_screen": "scene_1"}
        ]
    }
]

# ----------------------------------------------------------------------------------------------------------------------
