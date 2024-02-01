import sys
import pygame as pg
from settings import *
from ind_button import Button, ButtonColor, ButtonTrigger
from ind_screen import Screen, ScreenRect
from ind_free_item import FreeItemText, FreeItemParticipant


class MainGame:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        # self.mouse_pos = pg.mouse.get_pos()

        # self.allies_list = []
        # self.opponents_list = []

        self.new_game()

        # def triggers(self):
        # Участие в игре
        self.par_0l_in = True
        self.par_1l_in = False
        self.par_2l_in = False
        self.par_0r_in = True
        self.par_1r_in = False
        self.par_2r_in = False

        self.col_pal_0l_isopen = False
        self.col_pal_1l_isopen = False
        self.col_pal_2l_isopen = False
        self.col_pal_0r_isopen = False
        self.col_pal_1r_isopen = False
        self.col_pal_2r_isopen = False

    def new_game(self):
        # def screens(self):
        self.game_screen = Screen(self, "default_background.jpg",
                                  0, 0, WIDTH, HEIGHT,
                                  "Настройки игры",
                                  None, "white", 50)

        self.color_palette_screen_0l = ScreenRect(self)
        self.color_palette_screen_1l = ScreenRect(self)
        self.color_palette_screen_2l = ScreenRect(self)
        self.color_palette_screen_0r = ScreenRect(self)
        self.color_palette_screen_1r = ScreenRect(self)
        self.color_palette_screen_2r = ScreenRect(self)

        # def buttons(self):
        self.start_button = Button(self, "Старт", None,
                                   "white", "black", "green",
                                   "b.png", "g.png", "r.png",
                                   "dig_click_03.wav", "mouse_click_04.wav",
                                   WIDTH / 2 - (200 / 2), 320, 200, 60)

        self.add_par_1l_button = ButtonTrigger(self, None,
                                               "white", "black", "green",
                                               "b.png", "g.png", "r.png",
                                               "dig_click_03.wav", "mouse_click_04.wav",
                                               160, 180, 50, 50)
        self.add_par_2l_button = ButtonTrigger(self, None,
                                               "white", "black", "green",
                                               "b.png", "g.png", "r.png",
                                               "dig_click_03.wav", "mouse_click_04.wav",
                                               160, 240, 50, 50)
        self.add_par_1r_button = ButtonTrigger(self, None,
                                               "white", "black", "green",
                                               "b.png", "g.png", "r.png",
                                               "dig_click_03.wav", "mouse_click_04.wav",
                                               390, 180, 50, 50)
        self.add_par_2r_button = ButtonTrigger(self, None,
                                               "white", "black", "green",
                                               "b.png", "g.png", "r.png",
                                               "dig_click_03.wav", "mouse_click_04.wav",
                                               390, 240, 50, 50)

        self.button_color_red = ButtonColor(self, "red", 0, 0)
        self.button_color_gray = ButtonColor(self, "gray", 40, 0)
        self.button_color_blue = ButtonColor(self, "blue", 80, 0)
        self.button_color_brown = ButtonColor(self, "brown", 0, 40)
        self.button_color_purple = ButtonColor(self, "purple", 40, 40)
        self.button_color_orange = ButtonColor(self, "orange", 80, 40)
        self.button_color_pink = ButtonColor(self, "pink", 0, 80)
        self.button_color_green = ButtonColor(self, "green", 40, 80)
        self.button_color_yellow = ButtonColor(self, "yellow", 80, 80)

        # def free_items(self):
        self.freetext_allies = FreeItemText(self, "союзники", 100)
        self.freetext_opponents = FreeItemText(self, "противники", 500)

        self.par_0l = FreeItemParticipant(self, 50, 120)
        self.par_1l = FreeItemParticipant(self, 50, 180)
        self.par_2l = FreeItemParticipant(self, 50, 240)
        self.par_0r = FreeItemParticipant(self, 450, 120)
        self.par_1r = FreeItemParticipant(self, 450, 180)
        self.par_2r = FreeItemParticipant(self, 450, 240)

    def color_palette_screen_status(self):
        self.one_of_color_scr_open = False
        col_pal_sttatus_list = [self.col_pal_0l_isopen, self.col_pal_1l_isopen, self.col_pal_2l_isopen,
                                self.col_pal_0r_isopen, self.col_pal_1r_isopen, self.col_pal_2r_isopen]
        for i in col_pal_sttatus_list:
            if i is True:
                self.one_of_color_scr_open = True

        return self.one_of_color_scr_open

    # def new_game(self):
    #     self.screens()
    #     self.buttons()
    #     self.free_items()

    def update(self):
        """
        Метод обновления экрана (flip)
        """
        # Отслеживает статус игрока выше для корректного отображения кнопки
        self.add_par_1l_button.check_status(self.par_1l_in)
        self.add_par_2l_button.check_status(self.par_2l_in)
        self.add_par_1r_button.check_status(self.par_1r_in)
        self.add_par_2r_button.check_status(self.par_2r_in)

        # Отслеживает статус своего же игрока для корректного отображения кнопки-участника
        self.par_0l.check_status(self.par_0l_in)
        self.par_1l.check_status(self.par_1l_in)
        self.par_2l.check_status(self.par_2l_in)
        self.par_0r.check_status(self.par_0r_in)
        self.par_1r.check_status(self.par_1r_in)
        self.par_2r.check_status(self.par_2r_in)

        self.start_button.check_hover(pg.mouse.get_pos())

        self.par_0l.check_hover(pg.mouse.get_pos())
        self.par_1l.check_hover(pg.mouse.get_pos())
        self.par_2l.check_hover(pg.mouse.get_pos())
        self.par_0r.check_hover(pg.mouse.get_pos())
        self.par_1r.check_hover(pg.mouse.get_pos())
        self.par_2r.check_hover(pg.mouse.get_pos())

        self.button_color_red.check_hover_bc(pg.mouse.get_pos())
        self.button_color_gray.check_hover_bc(pg.mouse.get_pos())
        self.button_color_blue.check_hover_bc(pg.mouse.get_pos())
        self.button_color_brown.check_hover_bc(pg.mouse.get_pos())
        self.button_color_purple.check_hover_bc(pg.mouse.get_pos())
        self.button_color_orange.check_hover_bc(pg.mouse.get_pos())
        self.button_color_pink.check_hover_bc(pg.mouse.get_pos())
        self.button_color_green.check_hover_bc(pg.mouse.get_pos())
        self.button_color_yellow.check_hover_bc(pg.mouse.get_pos())

        self.add_par_1l_button.check_hover(pg.mouse.get_pos(), self.par_0l_in, self.par_2l_in)
        self.add_par_2l_button.check_hover(pg.mouse.get_pos(), self.par_1l_in, False)
        self.add_par_1r_button.check_hover(pg.mouse.get_pos(), self.par_0r_in, self.par_2r_in)
        self.add_par_2r_button.check_hover(pg.mouse.get_pos(), self.par_1r_in, False)

        pg.display.flip()
        self.clock.tick(FPS)  # Чилсо итераций (обновлений основного цикла игры за одну секунду)
        pg.display.set_caption("Vld Game")

    def draw(self):
        """
        Метод нанасения на экран чего-либо
        (рисование, заливка).
        Видимо здесь должны подгружаться менюшки
        """
        self.screen.fill("black")

        self.game_screen.draw()
        self.start_button.draw()

        self.freetext_allies.draw()
        self.freetext_opponents.draw()

        self.par_0l.draw(self.par_0l_in)
        self.par_1l.draw(self.par_1l_in)
        self.par_2l.draw(self.par_2l_in)
        self.par_0r.draw(self.par_0r_in)
        self.par_1r.draw(self.par_1r_in)
        self.par_2r.draw(self.par_2r_in)

        self.add_par_1l_button.draw(self.par_0l_in, self.par_2l_in)
        self.add_par_2l_button.draw(self.par_1l_in, False)
        self.add_par_1r_button.draw(self.par_0r_in, self.par_2r_in)
        self.add_par_2r_button.draw(self.par_1r_in, False)

        self.color_palette_screen_0l.draw(self.col_pal_0l_isopen)
        self.color_palette_screen_1l.draw(self.col_pal_1l_isopen)
        self.color_palette_screen_2l.draw(self.col_pal_2l_isopen)
        self.color_palette_screen_0r.draw(self.col_pal_0r_isopen)
        self.color_palette_screen_1r.draw(self.col_pal_0r_isopen)
        self.color_palette_screen_2r.draw(self.col_pal_0r_isopen)

        self.button_color_red.draw(self.color_palette_screen_status())
        self.button_color_gray.draw(self.color_palette_screen_status())
        self.button_color_blue.draw(self.color_palette_screen_status())
        self.button_color_brown.draw(self.color_palette_screen_status())
        self.button_color_purple.draw(self.color_palette_screen_status())
        self.button_color_orange.draw(self.color_palette_screen_status())
        self.button_color_pink.draw(self.color_palette_screen_status())
        self.button_color_green.draw(self.color_palette_screen_status())
        self.button_color_yellow.draw(self.color_palette_screen_status())

    def change_participants_color(self, event, participant):
        if event.button == self.button_color_red:
            participant.get_color(self.button_color_red.self_color())
        if event.button == self.button_color_gray:
            participant.get_color(self.button_color_gray.self_color())
        if event.button == self.button_color_blue:
            participant.get_color(self.button_color_blue.self_color())
        if event.button == self.button_color_brown:
            participant.get_color(self.button_color_brown.self_color())
        if event.button == self.button_color_purple:
            participant.get_color(self.button_color_purple.self_color())
        if event.button == self.button_color_orange:
            participant.get_color(self.button_color_orange.self_color())
        if event.button == self.button_color_pink:
            participant.get_color(self.button_color_pink.self_color())
        if event.button == self.button_color_green:
            participant.get_color(self.button_color_green.self_color())
        if event.button == self.button_color_yellow:
            participant.get_color(self.button_color_yellow.self_color())

    def check_events(self):
        """
        Проверка на нажатие кнопок и т. п.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.USEREVENT:
                if self.col_pal_0l_isopen is True:
                    self.change_participants_color(event, self.par_0l)
                if self.col_pal_1l_isopen is True:
                    self.change_participants_color(event, self.par_1l)
                if self.col_pal_2l_isopen is True:
                    self.change_participants_color(event, self.par_2l)
                if self.col_pal_0r_isopen is True:
                    self.change_participants_color(event, self.par_0r)
                if self.col_pal_1r_isopen is True:
                    self.change_participants_color(event, self.par_1r)
                if self.col_pal_2r_isopen is True:
                    self.change_participants_color(event, self.par_2r)

                self.one_of_color_scr_open = False

                if event.button == self.par_0l:
                    self.one_of_color_scr_open = False
                    self.col_pal_0l_isopen = True
                    self.color_palette_screen_0l.create_rect_scr()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rect_btn()
                    self.button_color_gray.create_rect_btn()
                    self.button_color_blue.create_rect_btn()
                    self.button_color_brown.create_rect_btn()
                    self.button_color_purple.create_rect_btn()
                    self.button_color_orange.create_rect_btn()
                    self.button_color_pink.create_rect_btn()
                    self.button_color_green.create_rect_btn()
                    self.button_color_yellow.create_rect_btn()
                else:
                    self.open_change_color_par_0 = False

                if event.button == self.par_1l:
                    self.one_of_color_scr_open = False
                    self.col_pal_1l_isopen = True
                    self.color_palette_screen_1l.create_rect_scr()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rect_btn()
                    self.button_color_gray.create_rect_btn()
                    self.button_color_blue.create_rect_btn()
                    self.button_color_brown.create_rect_btn()
                    self.button_color_purple.create_rect_btn()
                    self.button_color_orange.create_rect_btn()
                    self.button_color_pink.create_rect_btn()
                    self.button_color_green.create_rect_btn()
                    self.button_color_yellow.create_rect_btn()
                else:
                    self.open_change_color_par_1 = False

                if event.button == self.par_2l:
                    self.one_of_color_scr_open = False
                    self.col_pal_2l_isopen = True
                    self.color_palette_screen_2l.create_rect_scr()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rect_btn()
                    self.button_color_gray.create_rect_btn()
                    self.button_color_blue.create_rect_btn()
                    self.button_color_brown.create_rect_btn()
                    self.button_color_purple.create_rect_btn()
                    self.button_color_orange.create_rect_btn()
                    self.button_color_pink.create_rect_btn()
                    self.button_color_green.create_rect_btn()
                    self.button_color_yellow.create_rect_btn()
                else:
                    self.open_change_color_par_2 = False

                if event.button == self.par_0r:
                    self.one_of_color_scr_open = False
                    self.col_pal_0r_isopen = True
                    self.color_palette_screen_0r.create_rect_scr()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rect_btn()
                    self.button_color_gray.create_rect_btn()
                    self.button_color_blue.create_rect_btn()
                    self.button_color_brown.create_rect_btn()
                    self.button_color_purple.create_rect_btn()
                    self.button_color_orange.create_rect_btn()
                    self.button_color_pink.create_rect_btn()
                    self.button_color_green.create_rect_btn()
                    self.button_color_yellow.create_rect_btn()
                else:
                    self.open_change_color_par_3 = False

                if event.button == self.par_1r:
                    self.one_of_color_scr_open = False
                    self.col_pal_1r_isopen = True
                    self.color_palette_screen_1r.create_rect_scr()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rect_btn()
                    self.button_color_gray.create_rect_btn()
                    self.button_color_blue.create_rect_btn()
                    self.button_color_brown.create_rect_btn()
                    self.button_color_purple.create_rect_btn()
                    self.button_color_orange.create_rect_btn()
                    self.button_color_pink.create_rect_btn()
                    self.button_color_green.create_rect_btn()
                    self.button_color_yellow.create_rect_btn()
                else:
                    self.open_change_color_par_4 = False

                if event.button == self.par_2r:
                    self.one_of_color_scr_open = False
                    self.col_pal_2r_isopen = True
                    self.color_palette_screen_2r.create_rect_scr()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rect_btn()
                    self.button_color_gray.create_rect_btn()
                    self.button_color_blue.create_rect_btn()
                    self.button_color_brown.create_rect_btn()
                    self.button_color_purple.create_rect_btn()
                    self.button_color_orange.create_rect_btn()
                    self.button_color_pink.create_rect_btn()
                    self.button_color_green.create_rect_btn()
                    self.button_color_yellow.create_rect_btn()
                else:
                    self.open_change_color_par_5 = False

                # --------------

                if event.button == self.add_par_1l_button:
                    if self.par_1l_in is False:
                        self.par_1l_in = True
                        self.par_1l.get_rand_color()
                    else:
                        self.par_1l_in = False
                if event.button == self.add_par_2l_button:
                    if self.par_2l_in is False:
                        self.par_2l_in = True
                        self.par_2l.get_rand_color()
                    else:
                        self.par_2l_in = False
                if event.button == self.add_par_1r_button:
                    if self.par_1r_in is False:
                        self.par_1r_in = True
                        self.par_1r.get_rand_color()
                    else:
                        self.par_1r_in = False
                if event.button == self.add_par_2r_button:
                    if self.par_2r_in is False:
                        self.par_2r_in = True
                        self.par_2r.get_rand_color()
                    else:
                        self.par_2r_in = False

            self.start_button.handle_event(event)

            self.par_0l.handle_event_par(event, self.par_0l_in)
            self.par_1l.handle_event_par(event, self.par_1l_in)
            self.par_2l.handle_event_par(event, self.par_2l_in)
            self.par_0r.handle_event_par(event, self.par_0r_in)
            self.par_1r.handle_event_par(event, self.par_1r_in)
            self.par_2r.handle_event_par(event, self.par_2r_in)

            self.button_color_red.handle_event_bt(event, self.color_palette_screen_status())
            self.button_color_gray.handle_event_bt(event, self.color_palette_screen_status())
            self.button_color_blue.handle_event_bt(event, self.color_palette_screen_status())
            self.button_color_brown.handle_event_bt(event, self.color_palette_screen_status())
            self.button_color_purple.handle_event_bt(event, self.color_palette_screen_status())
            self.button_color_orange.handle_event_bt(event, self.color_palette_screen_status())
            self.button_color_pink.handle_event_bt(event, self.color_palette_screen_status())
            self.button_color_green.handle_event_bt(event, self.color_palette_screen_status())
            self.button_color_yellow.handle_event_bt(event, self.color_palette_screen_status())

            self.add_par_1l_button.handle_event(event, self.par_0l_in, self.par_2l_in)
            self.add_par_2l_button.handle_event(event, self.par_1l_in, False)
            self.add_par_1r_button.handle_event(event, self.par_0r_in, self.par_2r_in)
            self.add_par_2r_button.handle_event(event, self.par_1r_in, False)

    def run(self):
        """
        Работа программы, как процесс
        """
        self.par_0l.get_rand_color()
        self.par_0r.get_rand_color()

        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = MainGame()
    game.run()
