import pygame as pg
import sys
from settings import *
from button import Button
from screen import Screen

pg.init()

screen_surface = pg.display.set_mode((WIDTH, HEIGHT))
# pg.display.set_caption("test")

def screen_main_menu():
    background = Screen("default_background.jpg",
                        0, 0, WIDTH, HEIGHT,
                        "МЕНЮ",
                        None, "white", 50)

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

    # ПОСТОЯННАЯ. Запуск самой программы отображения
    running = True
    while running:
        for screen in [background]:
            screen.update(screen_surface)
            screen.draw(screen_surface)
            # screen.handle_event()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # screen_new_game()
            elif event.type == pg.USEREVENT and event.button == button_new_game:
                running = False
                screen_new_game()
            # screen_settings()
            # elif event.type == pg.USEREVENT and event.button == button_settings:
            #     running = False
            #     screen_settings()
            # screen_exit()
            elif event.type == pg.USEREVENT and event.button == button_exit:
                # Добавить затемнение
                screen_exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # Добавить затемнение
                    screen_exit()
            for button in [button_new_game, button_settings, button_exit]:
                button.handle_event(event)

        for button in [button_new_game, button_settings, button_exit]:
            button.check_hover(pg.mouse.get_pos())
            button.draw(screen_surface)

        pg.display.flip()


def screen_new_game():
    background = Screen("default_background.jpg",
                        0, 0, WIDTH, HEIGHT,
                        "ИГРА...",
                        None, "white",50)

    # Кнопка "Ход"
    # Передача хода (игра)"
    button_round = Button("Ход", None,
                             "white", "black", "green",
                             "b.png", "g.png", "r.png",
                             "dig_click_03.wav", "mouse_click_04.wav",
                             WIDTH / 2 - (100 / 2), 170, 100, 60)

    # ПОСТОЯННАЯ. Запуск самой программы отображения
    running = True
    while running:
        for screen in [background]:
            screen.update(screen_surface)
            screen.draw(screen_surface)
            # screen.handle_event()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # screen_pause()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    screen_pause()
            elif event.type == pg.USEREVENT and event.button == button_round:
                print("Ход")
            for button in [button_round]:
                button.handle_event(event)

        for button in [button_round]:
            button.check_hover(pg.mouse.get_pos())
            button.draw(screen_surface)

        pg.display.flip()


def screen_exit():
    background = Screen("background.jpg",
                        WIDTH * 0.2 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.2, HEIGHT - HEIGHT * 0.4,
                        "ВЫЙТИ ИЗ ИГРЫ?",
                        None, "white", 50)

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

    # ПОСТОЯННАЯ. Запуск самой программы отображения
    running = True
    while running:
        for screen in [background]:
            screen.update(screen_surface)
            screen.draw(screen_surface)
            # screen.handle_event()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # screen_main_menu()
            elif event.type == pg.USEREVENT and event.button == button_no:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            # exit
            elif event.type == pg.USEREVENT and event.button == button_yes:
                running = False
                pg.quit()
                sys.exit()

            for button in [button_yes, button_no]:
                button.handle_event(event)

        for button in [button_yes, button_no]:
            button.check_hover(pg.mouse.get_pos())
            button.draw(screen_surface)

        pg.display.flip()


def screen_pause():
    background = Screen("background.jpg",
                        WIDTH * 0.5 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.5, HEIGHT - HEIGHT * 0.4,
                        "ПАУЗА",
                        None, None, 50)

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

    # ПОСТОЯННАЯ. Запуск самой программы отображения
    running = True
    while running:
        for screen in [background]:
            screen.update(screen_surface)
            screen.draw(screen_surface)
            # screen.handle_event()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # screen_main_menu()
            elif event.type == pg.USEREVENT and event.button == button_main_menu:
                running = False
                screen_main_menu()
            # exit
            elif event.type == pg.USEREVENT and event.button == button_continue:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

            for button in [button_continue, button_main_menu]:
                button.handle_event(event)

        for button in [button_continue, button_main_menu]:
            button.check_hover(pg.mouse.get_pos())
            button.draw(screen_surface)

        pg.display.flip()


# ----------------------------------------------------------------------------------------------------------------------


start_screen = screen_main_menu()


def start_game(screen):
    global start_screen
    start_screen = screen
