import sys
from settings import *
import pygame as pg
from screen import Screen
from button import Button


class Game:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.display = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

        # triggers -----------------------------------------------------------------------------------------------------
        # screens
        self.tr_screen_0 = 1
        self.tr_screen_1 = 0
        self.tr_screen_3 = 0
        self.tr_screen_4 = 0

        # buttons
        self.tr_button_00 = 1
        self.tr_button_01 = 1
        self.tr_button_02 = 1
        self.tr_button_10 = 0
        self.tr_button_11 = 0
        self.tr_button_20 = 0
        self.tr_button_30 = 0
        self.tr_button_31 = 0
        self.tr_button_40 = 0
        self.tr_button_41 = 0

        self.start_game()

    def start_game(self):
        """
        Менюшки
        """
        # screens ------------------------------------------------------------------------------------------------------
        self.screen_0 = Screen("default_background.jpg",
                               0, 0, WIDTH, HEIGHT,
                               "МЕНЮ",
                               None, "white", 50)

        self.screen_1 = Screen("background.jpg",
                               0, 0, WIDTH, HEIGHT,
                               "ТИПА ИГРА...",
                               None, "white", 50)

        self.screen_3_exit = Screen("background.jpg",
                                    WIDTH * 0.2 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.2, HEIGHT - HEIGHT * 0.4,
                                    "ВЫЙТИ?",
                                    None, "white", 50)

        self.screen_4_pause = Screen("background.jpg",
                                     WIDTH * 0.5 / 2, HEIGHT * 0.4 / 2, WIDTH - WIDTH * 0.5, HEIGHT - HEIGHT * 0.4,
                                     "ПАУЗА",
                                     None, "white", 50)

        # buttons ------------------------------------------------------------------------------------------------------
        self.button_00_new_game = Button("Новая игра", None,
                                         "white", "black", "green",
                                         "b.png", "g.png", "r.png",
                                         "dig_click_03.wav", "mouse_click_04.wav",
                                         WIDTH / 2 - (200 / 2), 100, 200, 60)

        self.button_01_settings = Button("Настройки", None,
                                         "white", "black", "green",
                                         "b.png", "g.png", "r.png",
                                         "dig_click_03.wav", "mouse_click_04.wav",
                                         WIDTH / 2 - (200 / 2), 170, 200, 60)

        self.button_02_exit = Button("Выход", None,
                                     "white", "brown", "green",
                                     "b.png", "g.png", "r.png",
                                     "dig_click_03.wav", "mouse_click_04.wav",
                                     WIDTH / 2 - (200 / 2), 240, 200, 60)

        self.button_10_pause = Button("<", None,
                                      "white", "black", "green",
                                      "b.png", "g.png", "r.png",
                                      "dig_click_03.wav", "mouse_click_04.wav",
                                      20, 20, 60, 60)

        self.button_11_turn = Button("Ход", None,
                                     "white", "black", "green",
                                     "b.png", "g.png", "r.png",
                                     "dig_click_03.wav", "mouse_click_04.wav",
                                     WIDTH / 2 - (200 / 2), 170, 200, 60)

        self.button_20_back = Button("<", None,
                                     "white", "black", "green",
                                     "b.png", "g.png", "r.png",
                                     "dig_click_03.wav", "mouse_click_04.wav",
                                     20, 20, 60, 60)

        # Кнопка "Да"
        # Подтверждение выхода
        self.button_30 = Button("ДА", None,
                                "white", "black", "green",
                                "b.png", "g.png", "r.png",
                                "dig_click_03.wav", "mouse_click_04.wav",
                                (WIDTH + WIDTH * 0.2 / 2) / 8, 200, 200, 60)
        # Кнопка "Нет"
        # Вернуться назад в меню
        self.button_31 = Button("НЕТ", None,
                                "white", "black", "green",
                                "b.png", "g.png", "r.png",
                                "dig_click_03.wav", "mouse_click_04.wav",
                                (WIDTH + WIDTH * 0.2 / 2) / 2, 200, 200, 60)

        # Кнопка "Продолжить"
        # Вернуться в игру
        self.button_40 = Button("В МЕНЮ", None,
                                "white", "black", "green",
                                "b.png", "g.png", "r.png",
                                "dig_click_03.wav", "mouse_click_04.wav",
                                WIDTH / 2 - (200 / 2), 170, 200, 60)

        # Кнопка "Выйти в главное меню"
        # Перейти в главное меню
        self.button_41 = Button("ПРОДОЛЖИТЬ", None,
                                "white", "black", "green",
                                "b.png", "g.png", "r.png",
                                "dig_click_03.wav", "mouse_click_04.wav",
                                WIDTH / 2 - (200 / 2), 240, 200, 60)

    def new_game(self):
        """
        Начало новой игры
        """
        pass

    def update(self):
        """
        Метод обновления экрана (flip)
        """
        self.button_00_new_game.check_hover(pg.mouse.get_pos(), self.tr_button_00)
        self.button_01_settings.check_hover(pg.mouse.get_pos(), self.tr_button_01)
        self.button_02_exit.check_hover(pg.mouse.get_pos(), self.tr_button_02)
        self.button_10_pause.check_hover(pg.mouse.get_pos(), self.tr_button_10)
        self.button_11_turn.check_hover(pg.mouse.get_pos(), self.tr_button_11)
        self.button_20_back.check_hover(pg.mouse.get_pos(), self.tr_button_20)
        self.button_30.check_hover(pg.mouse.get_pos(), self.tr_button_30)
        self.button_31.check_hover(pg.mouse.get_pos(), self.tr_button_31)
        self.button_40.check_hover(pg.mouse.get_pos(), self.tr_button_40)
        self.button_41.check_hover(pg.mouse.get_pos(), self.tr_button_41)

        pg.display.flip()
        self.clock.tick(FPS)  # Чилсо итераций (обновлений основного цикла игры за одну секунду)
        pg.display.set_caption("Vld Game")

    def draw(self):
        """
        Метод нанасения на экран чего-либо
        (рисование, заливка).
        Видимо здесь должны подгружаться менюшки
        """
        self.display.fill("black")

        self.screen_0.draw(self.display, self.tr_screen_0)
        self.screen_1.draw(self.display, self.tr_screen_1)
        self.screen_3_exit.draw(self.display, self.tr_screen_3)
        self.screen_4_pause.draw(self.display, self.tr_screen_4)

        self.button_00_new_game.draw(self.display, self.tr_button_00)
        self.button_01_settings.draw(self.display, self.tr_button_01)
        self.button_02_exit.draw(self.display, self.tr_button_02)
        self.button_10_pause.draw(self.display, self.tr_button_10)
        self.button_11_turn.draw(self.display, self.tr_button_11)
        self.button_20_back.draw(self.display, self.tr_button_20)
        self.button_30.draw(self.display, self.tr_button_30)
        self.button_31.draw(self.display, self.tr_button_31)
        self.button_40.draw(self.display, self.tr_button_40)
        self.button_41.draw(self.display, self.tr_button_41)

    def check_events(self):
        """
        Проверка на нажатие кнопок и т. п.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.USEREVENT:
                if event.button == self.button_00_new_game:
                    self.tr_screen_0 = False
                    self.tr_screen_1 = True
                    self.tr_button_00 = False
                    self.tr_button_01 = False
                    self.tr_button_02 = False
                    self.tr_button_10 = True
                    self.tr_button_11 = True
                if event.button == self.button_01_settings:
                    self.tr_screen_0 = True
                    self.tr_button_00 = False
                    self.tr_button_01 = False
                    self.tr_button_02 = False
                    self.tr_button_20 = True
                if event.button == self.button_02_exit:
                    self.tr_screen_3 = True
                    self.tr_button_00 = False
                    self.tr_button_01 = False
                    self.tr_button_02 = False
                    self.tr_button_30 = True
                    self.tr_button_31 = True
                if event.button == self.button_10_pause:
                    self.tr_screen_4 = True
                    self.tr_button_10 = False
                    self.tr_button_11 = False
                    self.tr_button_40 = True
                    self.tr_button_41 = True
                if event.button == self.button_11_turn:
                    print("Ход")
                if event.button == self.button_30:
                    pg.quit()
                    sys.exit()
                if event.button == self.button_31:
                    self.tr_screen_3 = False
                    self.tr_button_00 = True
                    self.tr_button_01 = True
                    self.tr_button_02 = True
                    self.tr_button_30 = False
                    self.tr_button_31 = False
                if event.button == self.button_40:
                    self.tr_screen_0 = True
                    self.tr_screen_4 = False
                    self.tr_button_00 = True
                    self.tr_button_01 = True
                    self.tr_button_02 = True
                    self.tr_button_40 = False
                    self.tr_button_41 = False
                if event.button == self.button_41:
                    self.tr_screen_4 = False
                    self.tr_button_40 = False
                    self.tr_button_41 = False
                    self.tr_button_10 = True
                    self.tr_button_11 = True
                if event.button == self.button_20_back:
                    self.tr_button_20 = False
                    self.tr_button_00 = True
                    self.tr_button_01 = True
                    self.tr_button_02 = True

            self.button_00_new_game.handle_event(event, self.tr_button_00)
            self.button_01_settings.handle_event(event, self.tr_button_01)
            self.button_02_exit.handle_event(event, self.tr_button_02)
            self.button_10_pause.handle_event(event, self.tr_button_10)
            self.button_11_turn.handle_event(event, self.tr_button_11)
            self.button_20_back.handle_event(event, self.tr_button_20)
            self.button_30.handle_event(event, self.tr_button_30)
            self.button_31.handle_event(event, self.tr_button_31)
            self.button_40.handle_event(event, self.tr_button_40)
            self.button_41.handle_event(event, self.tr_button_41)

    def run(self):
        """
        Работа программы, как процесс
        """
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
