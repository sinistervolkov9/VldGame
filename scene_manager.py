from settings import *
from button import ButtonOld
from screen_old_ver import Screen


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
# class Trigger:
#     def __init__(self, booll):
#         self.booll = booll
#
#     def prrrr(self):
#         return bool(self.booll)
#
#     def change_trigger(self):
#         if self.booll == 1:
#             self.booll = 0
#         else:
#             self.booll = 1
#
#
# trigger_11 = Trigger(1)
# trigger_12 = Trigger(0)

# ----------------------------------------------------------------------------------------------------------------------

# Кнопка "Новая игра"
# Перехов в окно "Новая игра"
button_00_new_game = ButtonOld("НОВАЯ ИГРА", None,
                               "white", "black", "green",
                               "b.png", "g.png", "r.png",
                               "dig_click_03.wav", "mouse_click_04.wav",
                               WIDTH / 2 - (200 / 2), 100, 200, 60)

# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_01_settings = ButtonOld("НАСТРОЙКИ", None,
                               "white", "black", "green",
                               "b.png", "g.png", "r.png",
                               "dig_click_03.wav", "mouse_click_04.wav",
                               WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_02_exit = ButtonOld("ВЫХОД", None,
                           "white", "brown", "green",
                           "b.png", "g.png", "r.png",
                           "dig_click_03.wav", "mouse_click_04.wav",
                           WIDTH / 2 - (200 / 2), 240, 200, 60)

button_10_pause = ButtonOld("<", None,
                            "white", "black", "green",
                            "b.png", "g.png", "r.png",
                            "dig_click_03.wav", "mouse_click_04.wav",
                            20, 20, 60, 60)

button_11_turn_1 = ButtonOld("Ход", None,
                             "white", "black", "green",
                             "b.png", "g.png", "r.png",
                             "dig_click_03.wav", "mouse_click_04.wav",
                             WIDTH / 2 - (200 / 2), 170, 200, 60)

button_20 = ButtonOld("Общие", None,
                      "white", "black", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      WIDTH / 2 - (200 / 2), 100, 200, 60)

# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_21 = ButtonOld("Аудио", None,
                      "white", "black", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_22 = ButtonOld("Видео", None,
                      "white", "brown", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      WIDTH / 2 - (200 / 2), 240, 200, 60)

# Кнопка "Да"
# Подтверждение выхода
button_30 = ButtonOld("ДА", None,
                      "white", "black", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      (WIDTH + WIDTH * 0.2 / 2) / 8, 200, 200, 60)
# Кнопка "Нет"
# Вернуться назад в меню
button_31 = ButtonOld("НЕТ", None,
                      "white", "black", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      (WIDTH + WIDTH * 0.2 / 2) / 2, 200, 200, 60)

# Кнопка "Продолжить"
# Вернуться в игру
button_40 = ButtonOld("ПРОДОЛЖИТЬ", None,
                      "white", "black", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      WIDTH / 2 - (200 / 2), 170, 200, 60)

# Кнопка "Выйти в главное меню"
# Перейти в главное меню
button_41 = ButtonOld("В МЕНЮ", None,
                      "white", "black", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      WIDTH / 2 - (200 / 2), 240, 200, 60)


# ----------------------------------------------------------------------------------------------------------------------

class PEvent:
    def __init__(self, text):
        self.text = text

    def print_some(self):
        print(str(self.text))


print_event_0 = PEvent("Новая игра")
print_event_1 = PEvent("Ход")
print_event_3 = PEvent("В разработке")

# ----------------------------------------------------------------------------------------------------------------------

# item_1 = ScreenItem("r", 0, 0, 20, 20, None, None, None, None)


# ----------------------------------------------------------------------------------------------------------------------

scenes = [
    {"scene_0":
        [
            {"screen": screen_0_main},
            {"buttons":
                [
                    {button_00_new_game:
                        [
                            {"change_scene": "scene_1"},
                            {"print_some": print_event_0}
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
            {"screen": screen_1_new_game},
            {"buttons":
                [
                    {button_10_pause:
                        [
                            {"change_scene": "scene_4"},
                        ]
                    },
                    {button_11_turn_1:
                        [
                            {"print_some": print_event_1}
                        ]
                    }
                ]
            },
            {"esc_screen": "scene_4"}
        ]
    },
    {"scene_2":
        [
            {"screen": screen_2_settings},
            {"buttons":
                [
                    {button_20:
                        [
                            {"print_some": print_event_3}
                        ]
                    },
                    {button_21:
                        [
                            {"print_some": print_event_3}
                        ]
                    },
                    {button_22:
                        [
                            {"print_some": print_event_3}
                        ]
                    }
                ]
            },
            {"esc_screen": "scene_0"}
        ]
    },
    {"scene_3":
        [
            {"screen": screen_3_exit},
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
            {"screen": screen_4_pause},
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
