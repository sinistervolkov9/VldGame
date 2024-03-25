from settings import *
from button_old import ButtonOld
from screen_old import ScreenOld
from print_event import PrintEvent

# screens --------------------------------------------------------------------------------------------------------------

screen_0_main = ScreenOld("default_background.jpg",
                          0, 0, WIDTH, HEIGHT,
                          "ГЛАВНАЯ",
                          None, "white", 50)

screen_pause_menu = ScreenOld("background.jpg",
                              WIDTH * 0.5 / 2, HEIGHT * 0.2 / 2, WIDTH - WIDTH * 0.5, HEIGHT - HEIGHT * 0.2,
                              "Меню",
                              None, "white", 50)

screen_exit = ScreenOld("background.jpg",
                        WIDTH * 0.2 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.2, HEIGHT - HEIGHT * 0.4,
                        "ВЫЙТИ?",
                        None, "white", 50,
                        visible=False)

screen_sections = ScreenOld("background.jpg",
                            0, 0, 100, HEIGHT,
                            "",
                            None, "white", 50)

screen_subsections_to_play = ScreenOld("background.jpg",
                                       100, 0, 200, HEIGHT,
                                       "ИГРАТЬ",
                                       None, "white", 50, visible=False)

screen_subsections_to_collection = ScreenOld("background.jpg",
                                             100, 0, 200, HEIGHT,
                                             "КОЛЛЕКЦИЯ",
                                             None, "white", 50, visible=False)

# buttons --------------------------------------------------------------------------------------------------------------

# Кнопка "Профиль"
# Перехов в окно профиля игрока
button_00_to_profile = ButtonOld("Профиль", None,
                              "white", "black", "green",
                              "b.png", "g.png", "r.png",
                              "dig_click_03.wav", "mouse_click_04.wav",
                              20, 20, 60, 60)

#
#
button_00_to_main_menu = ButtonOld("Главная", None,
                                "white", "black", "green",
                                "b.png", "g.png", "r.png",
                                "dig_click_03.wav", "mouse_click_04.wav",
                                20, 100, 60, 60)

#
#
button_00_to_play = ButtonOld("Играть", None,
                           "white", "black", "green",
                           "b.png", "g.png", "r.png",
                           "dig_click_03.wav", "mouse_click_04.wav",
                           20, 180, 60, 60)

#
#
button_00_to_collection = ButtonOld("Коллекция", None,
                                 "white", "black", "green",
                                 "b.png", "g.png", "r.png",
                                 "dig_click_03.wav", "mouse_click_04.wav",
                                 20, 260, 60, 60)

#
#
button_00_to_pause_menu = ButtonOld("Меню", None,
                                 "white", "black", "green",
                                 "b.png", "g.png", "r.png",
                                 "dig_click_03.wav", "mouse_click_04.wav",
                                 520, 20, 60, 60)

# Кнопка "Вернуться"
#
button_01_back = ButtonOld("Вернуться", None,
                        "white", "black", "green",
                        "b.png", "g.png", "r.png",
                        "dig_click_03.wav", "mouse_click_04.wav",
                        WIDTH / 2 - (200 / 2), 120, 200, 60)

# Кнопка "Настройки"
# Перехов в окно "Настройки"
button_01_settings = ButtonOld("Настройки", None,
                            "white", "black", "green",
                            "b.png", "g.png", "r.png",
                            "dig_click_03.wav", "mouse_click_04.wav",
                            WIDTH / 2 - (200 / 2), 190, 200, 60)

# Кнопка "Выход"
# Выход из программы
button_02_exit = ButtonOld("Выход", None,
                        "white", "brown", "green",
                        "b.png", "g.png", "r.png",
                        "dig_click_03.wav", "mouse_click_04.wav",
                        WIDTH / 2 - (200 / 2), 260, 200, 60)

# Кнопка "Да"
# Подтверждение выхода
button_exit_yes = ButtonOld("Да", None,
                         "white", "black", "green",
                         "b.png", "g.png", "r.png",
                         "dig_click_03.wav", "mouse_click_04.wav",
                         (WIDTH + WIDTH * 0.2 / 2) / 8, 200, 200, 60,
                         visible=False)
# Кнопка "Нет"
# Вернуться назад в меню
button_exit_no = ButtonOld("Нет", None,
                        "white", "black", "green",
                        "b.png", "g.png", "r.png",
                        "dig_click_03.wav", "mouse_click_04.wav",
                        (WIDTH + WIDTH * 0.2 / 2) / 2, 200, 200, 60,
                        visible=False)

# Кампания
#
button_game_campaign = ButtonOld("Кампания", None,
                              "white", "black", "green",
                              "b.png", "g.png", "r.png",
                              "dig_click_03.wav", "mouse_click_04.wav",
                              125, 100, 150, 50,
                              visible=False)

# Стандартная игра
#
button_free_game = ButtonOld("Против компа", None,
                          "white", "black", "green",
                          "b.png", "g.png", "r.png",
                          "dig_click_03.wav", "mouse_click_04.wav",
                          125, 175, 150, 50,
                          visible=False)

# Боевка онли
#
button_game_combat = ButtonOld("Схватка", None,
                            "white", "black", "green",
                            "b.png", "g.png", "r.png",
                            "dig_click_03.wav", "mouse_click_04.wav",
                            125, 250, 150, 50,
                            visible=False)

# Карточки
#
button_cards = ButtonOld("Карточки", None,
                      "white", "black", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      125, 100, 150, 50,
                      visible=False)

# Колоды
#
button_decks = ButtonOld("Колоды", None,
                      "white", "black", "green",
                      "b.png", "g.png", "r.png",
                      "dig_click_03.wav", "mouse_click_04.wav",
                      125, 175, 150, 50,
                      visible=False)

# Рубашки
#
button_shirts = ButtonOld("Рубашки", None,
                       "white", "black", "green",
                       "b.png", "g.png", "r.png",
                       "dig_click_03.wav", "mouse_click_04.wav",
                       125, 250, 150, 50,
                       visible=False)

# print_events ---------------------------------------------------------------------------------------------------------

print_event_0 = PrintEvent("В разработке")

# items ----------------------------------------------------------------------------------------------------------------

# item_1 = ScreenItem("r", 0, 0, 20, 20, None, None, None, None)

# MAIN -----------------------------------------------------------------------------------------------------------------

scenes = [
    {"scene_main_menu":
        [
            {"screen": [screen_0_main,
                        screen_sections, screen_subsections_to_collection, screen_subsections_to_play]},
            {"buttons":
                [
                    {button_00_to_profile:
                        [
                            {"print_text": print_event_0}
                        ]
                    },
                    {button_00_to_main_menu:
                        [
                            {"bring_to_basic": [screen_subsections_to_collection, screen_subsections_to_play,
                                                button_game_campaign, button_free_game, button_game_combat,
                                                button_cards, button_decks, button_shirts]}
                        ]
                    },
                    {button_00_to_play:
                        [
                            {"bring_to_basic": [screen_subsections_to_collection,
                                                button_cards, button_decks, button_shirts]},
                            {"switch_visibility": [screen_subsections_to_play,
                                                   button_game_campaign, button_free_game, button_game_combat]}
                        ]
                    },
                    {button_00_to_collection:
                        [
                            {"bring_to_basic": [screen_subsections_to_play,
                                                button_game_campaign, button_free_game, button_game_combat]},
                            {"switch_visibility": [screen_subsections_to_collection,
                                                   button_cards, button_decks, button_shirts]}
                        ]
                    },
                    {button_00_to_pause_menu:
                        [
                            {"change_scene": "scene_pause_menu"}
                        ]
                    },
                    {button_game_campaign:
                        [
                            {"print_text": print_event_0}
                        ]
                    },
                    {button_free_game:
                        [
                            {"print_text": print_event_0}
                        ]
                    },
                    {button_game_combat:
                        [
                            {"print_text": print_event_0}
                        ]
                    },
                    {button_cards:
                        [
                            {"print_text": print_event_0}
                        ]
                    },
                    {button_decks:
                        [
                            {"print_text": print_event_0}
                        ]
                    },
                    {button_shirts:
                        [
                            {"print_text": print_event_0}
                        ]
                    }
                ]
            },
            {"esc_event":
                [
                    {"change_scene": "scene_pause_menu"}
                ]
            }
        ]
    },
    {"scene_pause_menu":
        [
            {"screen": [screen_pause_menu, screen_exit]},
            {"buttons":
                [
                    {button_01_back:
                        [
                            {"change_scene": None}
                        ]
                    },
                    {button_01_settings:
                        [
                            {"print_text": print_event_0}
                        ]
                    },
                    {button_02_exit:
                        [
                            {"switch_visibility": [screen_exit,
                                                   button_exit_yes, button_exit_no,
                                                   button_01_back, button_01_settings, button_02_exit]}
                        ]
                    },
                    {button_exit_yes:
                        [
                            {"change_scene": "EXIT"}
                        ]
                    },
                    {button_exit_no:
                        [
                            {"bring_to_basic": [screen_exit,
                                                button_exit_yes, button_exit_no,
                                                button_01_back, button_01_settings, button_02_exit]}
                        ]
                    }
                ]
            },
            {"esc_event":
                [
                    {"bring_to_basic": [screen_exit,
                                        button_exit_yes, button_exit_no,
                                        button_01_back, button_01_settings, button_02_exit]},
                    {"change_scene": None}
                ]
            }
        ]
    }
]

# ----------------------------------------------------------------------------------------------------------------------
