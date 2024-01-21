import random
import sys
from settings import *
import pygame as pg


# ----------------------------------------------------------------------------------------------------------------------

class Button_status:
    def __init__(
            self, game, font=None,
            text_color=None, text_color_hover=None, text_color_click=None,
            image=None, image_hover=None, image_click=None, sound_hover=None, sound_click=None,
            x=0, y=0, width=200, height=60
    ):

        self.game = game
        self.text = ""
        self.font = font  # Шрифт выводимого текста (будет постоянный для всех состояний текста)
        self.text_color = text_color  # Цвет выводимого текста
        self.text_color_hover = text_color_hover  # Цвет текста при наведении на КНОПКУ
        self.text_color_click = text_color_click  # Цвет текста при нажатии на КНОПКУ
        self.image = image  # Изображение выводимой кнопки
        self.image_hover = image_hover  # Изображение кнопки при наведении на нее
        self.image_click = image_click  # Изображение кнопки при нажатии на нее
        self.sound_hover = sound_hover  # Звук кнопки при наведении на нее
        self.sound_click = sound_click  # Звук кнопки при нажатии на нее
        self.x = x  # Позиция по x-координате
        self.y = y  # Позиция по y-координате
        self.width = width  # Длина кнопки
        self.height = height  # Высота кнопки
        self.over = None  # Вспомогательный аргумент

        # Работа с аргументами-переменными 1:
        # text
        # if text:
        #     self.text = text
        # else:
        #     self.text = "text"

        # font
        if font:
            self.font = "resources/fonts/" + font
        else:
            self.font = None  # ?

        # text_color
        if text_color:
            self.text_color = text_color
        else:
            self.text_color = "black"

        # text_color_hover
        if text_color_hover:
            self.text_color_hover = text_color_hover
        else:
            self.text_color_hover = self.text_color  # or None?

        # text_color_click
        if text_color_click:
            self.text_color_click = text_color_click
        else:
            self.text_color_click = self.text_color  # or None?

        # image
        if image:
            self.image = "resources/button_images/" + image
        else:
            self.image = "resources/button_images/default_button.png"

        # image_hover
        if image_hover:
            self.image_hover = "resources/button_images/" + image_hover
        else:
            self.image_hover = self.image

        # image_click
        if image_click:
            self.image_click = "resources/button_images/" + image_click
        else:
            self.image_click = self.image

        # sound_hover
        if sound_hover:
            if sound_hover == "default":
                self.sound_hover = "resources/sounds/default_sound_hover.wav"
            else:
                self.sound_hover = "resources/sounds/" + sound_hover
        else:
            self.sound_hover = None  # ?

        # sound_click
        if sound_click:
            if sound_click == "default":
                self.sound_click = "resources/sounds/default_sound_click.wav"
            else:
                self.sound_click = "resources/sounds/" + sound_click
        else:
            self.sound_click = None  # ?

        # Работа с аргументами-переменными 2:
        # Подгрузка изображения кнопки
        self.image = pg.image.load(self.image)
        self.image = pg.transform.scale(self.image, (width, height))

        # Изображение кнопки
        # Если будет добавлено изображение кнопки при наведении
        if self.image_hover:
            self.image_hover = pg.image.load(self.image_hover)
            self.image_hover = pg.transform.scale(self.image_hover, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))  # rect

        # Если будет добавлено изображение кнопки при нажатии
        if self.image_click:
            self.image_click = pg.image.load(self.image_click)
            self.image_click = pg.transform.scale(self.image_click, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))  # rect

        # Цвет текста
        # Если будет меняться цвет текста при наведении
        if self.text_color_hover:
            self.color_hover = self.text_color_hover

        # Если будет меняться цвет текста при нажатии
        if self.text_color_click:
            self.color_click = self.text_color_click

        # Звуки при наведении и нажатии
        # Если будет добавлен звук при наведении
        if self.sound_hover:
            self.sound_hover = pg.mixer.Sound(self.sound_hover)
        else:
            self.sound_hover = None

        # Если будет добавлен звук при нажатии
        if self.sound_click:
            self.sound_click = pg.mixer.Sound(self.sound_click)
        else:
            self.sound_click = None

        # Для проверки, наведена ли мышка на кнопку
        self.is_hovered = False
        # Для проверки, наведена ли мышка на кнопку
        self.is_clicked = False

    def draw(self, previous_status, next_status):
        """
        Метод, который позволит нарисовать кнопку.
        В него передаем экран, на котором будет рисоваться кнопка
        """
        if next_status is True:
            pass
        elif previous_status is True:

            # Чтобы понять, какую картинку и какого цвета текст необх. отобразить
            # current_image = self.image_hover if self.is_hovered else self.image
            if self.is_clicked:
                current_image = self.image_click
                current_text_color = self.color_click
                # print("image_click")
            elif self.is_hovered:
                current_image = self.image_hover
                current_text_color = self.color_hover
                # print("image_hover")
            else:
                current_image = self.image
                current_text_color = self.text_color
                # print("image")

            # Отображение кнопки:
            self.game.screen.blit(current_image, self.rect.topleft)

            # Отображение текста:
            # Размер шрифта (базово - половина высоты кнопки)
            text_size = self.height / 2

            # Подключение шрифта (базово - базовый)
            font = pg.font.Font(self.font, int(text_size))

            # Рендеринг текста
            text_surface = font.render(self.text, True, current_text_color)

            # rect текста (создание невидимой обводки текста)
            text_rect = text_surface.get_rect(center=self.rect.center)

            # Вывод текста
            self.game.screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos, previous_status, next_status):
        """
        Проверяет, наведена мышка на кнопку или нет
        """
        if next_status is True:
            pass
        elif previous_status is True:
            self.is_hovered = self.rect.collidepoint(mouse_pos)

            # if self.rect.collidepoint(mouse_pos):
            #     self.is_hovered = True

    def handle_event(self, event, previous_status, next_status):
        """
        Метод обрабоки событий
        """
        if next_status is True:
            pass
        elif previous_status is True:
            # Звук наведения, если есть:
            if self.is_hovered:
                if not self.over:
                    if self.sound_hover:
                        self.sound_hover.play()
                    self.over = True
            else:
                self.over = False

            # Звук нажатия, если есть:
            pressed = pg.mouse.get_pressed()
            if pressed[0] and self.is_hovered:
                self.is_clicked = True

            if event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.is_hovered:
                if self.sound_click:
                    self.sound_click.play()
                    #  Пока не завершится анимация кнопки-клика:
                self.is_clicked = False
                pg.event.post(pg.event.Event(pg.USEREVENT, button=self))
                # print("self.is_clicked = False")
            if event.type == pg.MOUSEBUTTONUP and event.button == 1 and not self.is_hovered:
                self.is_clicked = False

    def check_status(self, status):
        if status is True:
            self.text = "-"
        else:
            self.text = "+"


# ----------------------------------------------------------------------------------------------------------------------

class Button:
    def __init__(
            self, game,
            text: str = None, font=None,
            text_color=None, text_color_hover=None, text_color_click=None,
            image=None, image_hover=None, image_click=None, sound_hover=None, sound_click=None,
            x=0, y=0, width=200, height=60
    ):

        self.game = game
        self.text = text  # Выводимый текст
        self.font = font  # Шрифт выводимого текста (будет постоянный для всех состояний текста)
        self.text_color = text_color  # Цвет выводимого текста
        self.text_color_hover = text_color_hover  # Цвет текста при наведении на КНОПКУ
        self.text_color_click = text_color_click  # Цвет текста при нажатии на КНОПКУ
        self.image = image  # Изображение выводимой кнопки
        self.image_hover = image_hover  # Изображение кнопки при наведении на нее
        self.image_click = image_click  # Изображение кнопки при нажатии на нее
        self.sound_hover = sound_hover  # Звук кнопки при наведении на нее
        self.sound_click = sound_click  # Звук кнопки при нажатии на нее
        self.x = x  # Позиция по x-координате
        self.y = y  # Позиция по y-координате
        self.width = width  # Длина кнопки
        self.height = height  # Высота кнопки
        self.over = None  # Вспомогательный аргумент

        # Работа с аргументами-переменными 1:
        # text
        if text:
            self.text = text
        else:
            self.text = "text"

        # font
        if font:
            self.font = "resources/fonts/" + font
        else:
            self.font = None  # ?

        # text_color
        if text_color:
            self.text_color = text_color
        else:
            self.text_color = "black"

        # text_color_hover
        if text_color_hover:
            self.text_color_hover = text_color_hover
        else:
            self.text_color_hover = self.text_color  # or None?

        # text_color_click
        if text_color_click:
            self.text_color_click = text_color_click
        else:
            self.text_color_click = self.text_color  # or None?

        # image
        if image:
            self.image = "resources/button_images/" + image
        else:
            self.image = "resources/button_images/default_button.png"

        # image_hover
        if image_hover:
            self.image_hover = "resources/button_images/" + image_hover
        else:
            self.image_hover = self.image

        # image_click
        if image_click:
            self.image_click = "resources/button_images/" + image_click
        else:
            self.image_click = self.image

        # sound_hover
        if sound_hover:
            if sound_hover == "default":
                self.sound_hover = "resources/sounds/default_sound_hover.wav"
            else:
                self.sound_hover = "resources/sounds/" + sound_hover
        else:
            self.sound_hover = None  # ?

        # sound_click
        if sound_click:
            if sound_click == "default":
                self.sound_click = "resources/sounds/default_sound_click.wav"
            else:
                self.sound_click = "resources/sounds/" + sound_click
        else:
            self.sound_click = None  # ?

        # Работа с аргументами-переменными 2:
        # Подгрузка изображения кнопки
        self.image = pg.image.load(self.image)
        self.image = pg.transform.scale(self.image, (width, height))

        # Изображение кнопки
        # Если будет добавлено изображение кнопки при наведении
        if self.image_hover:
            self.image_hover = pg.image.load(self.image_hover)
            self.image_hover = pg.transform.scale(self.image_hover, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))  # rect

        # Если будет добавлено изображение кнопки при нажатии
        if self.image_click:
            self.image_click = pg.image.load(self.image_click)
            self.image_click = pg.transform.scale(self.image_click, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))  # rect

        # Цвет текста
        # Если будет меняться цвет текста при наведении
        if self.text_color_hover:
            self.color_hover = self.text_color_hover

        # Если будет меняться цвет текста при нажатии
        if self.text_color_click:
            self.color_click = self.text_color_click

        # Звуки при наведении и нажатии
        # Если будет добавлен звук при наведении
        if self.sound_hover:
            self.sound_hover = pg.mixer.Sound(self.sound_hover)
        else:
            self.sound_hover = None

        # Если будет добавлен звук при нажатии
        if self.sound_click:
            self.sound_click = pg.mixer.Sound(self.sound_click)
        else:
            self.sound_click = None

        # Для проверки, наведена ли мышка на кнопку
        self.is_hovered = False
        # Для проверки, наведена ли мышка на кнопку
        self.is_clicked = False

    def draw(self):
        """
        Метод, который позволит нарисовать кнопку.
        В него передаем экран, на котором будет рисоваться кнопка
        """

        # Чтобы понять, какую картинку и какого цвета текст необх. отобразить
        # current_image = self.image_hover if self.is_hovered else self.image
        if self.is_clicked:
            current_image = self.image_click
            current_text_color = self.color_click
            # print("image_click")
        elif self.is_hovered:
            current_image = self.image_hover
            current_text_color = self.color_hover
            # print("image_hover")
        else:
            current_image = self.image
            current_text_color = self.text_color
            # print("image")

        # Отображение кнопки:
        self.game.screen.blit(current_image, self.rect.topleft)

        # Отображение текста:
        # Размер шрифта (базово - половина высоты кнопки)
        text_size = self.height / 2

        # Подключение шрифта (базово - базовый)
        font = pg.font.Font(self.font, int(text_size))

        # Рендеринг текста
        text_surface = font.render(self.text, True, current_text_color)

        # rect текста (создание невидимой обводки текста)
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Вывод текста
        self.game.screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        """
        Проверяет, наведена мышка на кнопку или нет
        """

        self.is_hovered = self.rect.collidepoint(mouse_pos)

        # if self.rect.collidepoint(mouse_pos):
        #     self.is_hovered = True

    def handle_event(self, event):
        """
        Метод обрабоки событий
        """

        # Звук наведения, если есть:
        if self.is_hovered:
            if not self.over:
                if self.sound_hover:
                    self.sound_hover.play()
                self.over = True
        else:
            self.over = False

        # Звук нажатия, если есть:
        pressed = pg.mouse.get_pressed()
        if pressed[0] and self.is_hovered:
            self.is_clicked = True

        if event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.is_hovered:
            if self.sound_click:
                self.sound_click.play()
                #  Пока не завершится анимация кнопки-клика:
            self.is_clicked = False
            pg.event.post(pg.event.Event(pg.USEREVENT, button=self))
            # print("self.is_clicked = False")
        if event.type == pg.MOUSEBUTTONUP and event.button == 1 and not self.is_hovered:
            self.is_clicked = False


# ----------------------------------------------------------------------------------------------------------------------

class Screen:
    def __init__(
            self, game,
            background,
            x=0, y=0, width=600, height=400,

            text=None, font=None, text_color=None,
            text_size=50
    ):

        self.game = game
        self.background = background  # Задний фон (Изображение)
        self.x = x  # Позиция по x-координате
        self.y = y  # Позиция по y-координате
        self.width = width  # Длина фонового изображения
        self.height = height  # Высота фонового изображения
        # self.sound = sound  # Фоновая музыка
        self.text = text  # Выводимый на заднем фоне текст (если надо)
        self.font = font  # Шрифт выводимого текста (будет постоянный для всех состояний текста)
        self.text_color = text_color  # Цвет выводимого текста
        self.text_size = text_size
        # self.text_pos = text_pos

        # text_pos = (self.width / 4)

        # Работа с аргументами-переменными 1:
        # background
        if background:
            self.background = "resources/backgrounds/" + background
        else:
            self.background = "resources/backgrounds/default_background.jpg"

        # # sound
        # if sound:
        #     self.sound = "resources/sounds/" + sound
        # else:
        #     self.sound = None

        # text
        if text:
            self.text = text
        else:
            self.text = None

        # font
        if font:
            self.font = "resources/fonts/" + font
        else:
            self.font = None

        # text_color
        if text_color:
            self.text_color = text_color
        else:
            self.text_color = "black"

        # Работа с аргументами-переменными 2:
        # Подгрузка изображения заднего фона
        self.background = pg.image.load(self.background)
        self.background = pg.transform.scale(self.background, (width, height))
        self.rect = self.background.get_rect(topleft=(x, y))  # rect

        # # Если будет добавлена фоновая музыка (звуки)
        # if self.sound:
        #     self.sound = pg.mixer.Sound(self.sound)
        # else:
        #     self.sound = None

    # def update(self, screen):
    #     """
    #     pass
    #     """
    #
    #     # ПОСТОЯННАЯ. Отображение заднего фона
    #     # screen.fill("white")
    #     screen.blit(self.background, self.rect.topleft)

    def draw(self):
        """
        pass
        """
        # ПОСТОЯННАЯ. Отображение заднего фона
        # screen.fill("white")
        self.game.screen.blit(self.background, self.rect.topleft)

        # ПОСТОЯННАЯ. Отображение текста на заднем фоне (если есть)
        if self.text:
            # Отображение текста:
            # Размер шрифта
            text_size = self.text_size

            # Подключение шрифта (базово - базовый)
            font = pg.font.Font(self.font, int(text_size))

            # Рендеринг текста
            text_surface = font.render(self.text, True, self.text_color)

            # rect текста (создание невидимой обводки текста)
            text_rect = text_surface.get_rect(center=((self.width + self.x * 2) / 2, self.y + 50))

            # Вывод текста
            self.game.screen.blit(text_surface, text_rect)

    # def handle_event(self):
    #     """
    #     Метод обрабоки событий
    #     """
    #
    #     # Фоновая музыка (звуки), если есть:
    #     if self.sound:
    #         self.sound.play()


# ----------------------------------------------------------------------------------------------------------------------

class ScreenColor:
    def __init__(
            self, game
    ):
        self.game = game
        self.width = 120  # Длина фонового изображения
        self.height = 120  # Высота фонового изображения
        self.screennnn = None

    def create_recttt(self):
        x, y = pg.mouse.get_pos()
        self.screennnn = pg.Rect(x, y, self.width, self.height)

    def draw(self, status):
        """
        pass
        """
        if status is True:
            pg.draw.rect(self.game.screen, "black", self.screennnn)


# ----------------------------------------------------------------------------------------------------------------------

class FreeText:
    def __init__(self, game, text, x):
        self.game = game
        self.text = text
        self.x = x
        if text:
            self.text = text
        else:
            self.text = None

    def draw(self):
        if self.text:
            # Отображение текста:
            # Размер шрифта
            text_size = 30

            # Подключение шрифта (базово - базовый)
            font = pg.font.Font(None, int(text_size))

            # Рендеринг текста
            text_surface = font.render(self.text, True, "white")

            # rect текста (создание невидимой обводки текста)
            text_rect = text_surface.get_rect(center=(self.x, 100))

            # Вывод текста
            self.game.screen.blit(text_surface, text_rect)


# ----------------------------------------------------------------------------------------------------------------------

class ButtonColor:
    def __init__(self, game, color, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.buttonnnn = None
        self.width = 40
        self.height = 40
        self.color = color
        self.create_rectttttttt()

    def self_color(self):
        return str(self.color)

    def check_hover_bc(self, mouse_pos):
        self.is_hovered = self.buttonnnn.collidepoint(mouse_pos)

    def handle_event_bc(self, event, status):
        if status is True:
            if event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.is_hovered:
                pg.event.post(pg.event.Event(pg.USEREVENT, button=self))

    def create_rectttttttt(self):
        x, y = pg.mouse.get_pos()
        self.buttonnnn = pg.Rect(x + self.x, y + self.y, self.width, self.height)

    def draw(self, status):
        if status is True:
            pg.draw.rect(self.game.screen, self.color, self.buttonnnn)


# ----------------------------------------------------------------------------------------------------------------------

class Participant:  # Прямоугольник, на котором будет выводиться текст. Цвет прямоугольника тоже меняется
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.participant = None
        self.create_rect()
        self.text = ""
        self.color = "white"

    def check_hover(self, mouse_pos):
        self.is_hovered = self.participant.collidepoint(mouse_pos)

    def handle_event_par(self, event, status):
        if status is True:
            if event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.is_hovered:
                pg.event.post(pg.event.Event(pg.USEREVENT, button=self))

    def create_rect(self):
        self.participant = pg.Rect(self.x, self.y, 100, 50)

    def check_status(self, status):
        if status is True:
            self.text = "player"
        else:
            self.text = None

    def get_rand_color(self, status):
        if status is True:
            self.colors_list = ["red", "gray", "blue", "aquamarine", "purple", "orange", "pink", "green"]
            index = random.randint(0, len(self.colors_list) - 1)
            self.color = self.colors_list[index]
        else:
            self.color = "white"

    def get_color(self, color):
        self.color = color

    def draw(self, status):
        if status is True:
            pg.draw.rect(self.game.screen, self.color, self.participant)

            # Размер шрифта
            text_size = 50 / 2

            # Подключение шрифта (базово - базовый)
            font = pg.font.Font(None, int(text_size))

            # Рендеринг текста
            text_surface = font.render(self.text, True, "black")

            # rect текста (создание невидимой обводки текста)
            text_rect = text_surface.get_rect(center=((100 + self.x * 2) / 2, self.y + 25))

            # Вывод текста
            self.game.screen.blit(text_surface, text_rect)


# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

class MainGame:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

        self.participant_0_active = True
        self.participant_1_active = False
        self.participant_2_active = False
        self.participant_3_active = True
        self.participant_4_active = False
        self.participant_5_active = False

        self.one_of_color_scr_open = False

        self.open_change_color_par_0 = False
        self.open_change_color_par_1 = False
        self.open_change_color_par_2 = False
        self.open_change_color_par_3 = False
        self.open_change_color_par_4 = False
        self.open_change_color_par_5 = False

        self.allies_list = []
        self.opponents_list = []

        self.new_game()

    def new_game(self):
        self.game_screen = Screen(self, "default_background.jpg",
                                  0, 0, WIDTH, HEIGHT,
                                  "Настройки игры",
                                  None, "white", 50)
        self.start_button = Button(self, "Старт", None,
                                   "white", "black", "green",
                                   "b.png", "g.png", "r.png",
                                   "dig_click_03.wav", "mouse_click_04.wav",
                                   WIDTH / 2 - (200 / 2), 320, 200, 60)
        self.freetext_allies = FreeText(self, "союзники", 100)
        self.freetext_opponents = FreeText(self, "противники", 500)

        self.participant_0 = Participant(self, 50, 120)
        self.participant_1 = Participant(self, 50, 180)
        self.participant_2 = Participant(self, 50, 240)
        self.participant_3 = Participant(self, 450, 120)
        self.participant_4 = Participant(self, 450, 180)
        self.participant_5 = Participant(self, 450, 240)

        self.add_participant_1_button = Button_status(self, None,
                                                      "white", "black", "green",
                                                      "b.png", "g.png", "r.png",
                                                      "dig_click_03.wav", "mouse_click_04.wav",
                                                      160, 180, 50, 50)
        self.add_participant_2_button = Button_status(self, None,
                                                      "white", "black", "green",
                                                      "b.png", "g.png", "r.png",
                                                      "dig_click_03.wav", "mouse_click_04.wav",
                                                      160, 240, 50, 50)
        self.add_participant_4_button = Button_status(self, None,
                                                      "white", "black", "green",
                                                      "b.png", "g.png", "r.png",
                                                      "dig_click_03.wav", "mouse_click_04.wav",
                                                      390, 180, 50, 50)
        self.add_participant_5_button = Button_status(self, None,
                                                      "white", "black", "green",
                                                      "b.png", "g.png", "r.png",
                                                      "dig_click_03.wav", "mouse_click_04.wav",
                                                      390, 240, 50, 50)

        self.screen_color_0 = ScreenColor(self)
        self.screen_color_1 = ScreenColor(self)
        self.screen_color_2 = ScreenColor(self)
        self.screen_color_3 = ScreenColor(self)
        self.screen_color_4 = ScreenColor(self)
        self.screen_color_5 = ScreenColor(self)

        self.button_color_red = ButtonColor(self, "red", 0, 0)
        self.button_color_gray = ButtonColor(self, "gray", 40, 0)
        self.button_color_blue = ButtonColor(self, "blue", 80, 0)
        self.button_color_aquamarine = ButtonColor(self, "aquamarine", 0, 40)
        self.button_color_purple = ButtonColor(self, "purple", 40, 40)
        self.button_color_orange = ButtonColor(self, "orange", 80, 40)
        self.button_color_pink = ButtonColor(self, "pink", 0, 80)
        self.button_color_green = ButtonColor(self, "green", 40, 80)
        self.button_color_yellow = ButtonColor(self, "yellow", 80, 80)

    def update(self):
        """
        Метод обновления экрана (flip)
        """
        self.add_participant_1_button.check_status(self.participant_1_active)
        self.add_participant_2_button.check_status(self.participant_2_active)
        self.add_participant_4_button.check_status(self.participant_4_active)
        self.add_participant_5_button.check_status(self.participant_5_active)

        self.participant_0.check_status(self.participant_0_active)
        self.participant_1.check_status(self.participant_1_active)
        self.participant_2.check_status(self.participant_2_active)
        self.participant_3.check_status(self.participant_3_active)
        self.participant_4.check_status(self.participant_4_active)
        self.participant_5.check_status(self.participant_5_active)

        self.start_button.check_hover(pg.mouse.get_pos())

        self.add_participant_1_button.check_hover(pg.mouse.get_pos(), self.participant_0_active,
                                                  self.participant_2_active)
        self.add_participant_2_button.check_hover(pg.mouse.get_pos(), self.participant_1_active, False)
        self.add_participant_4_button.check_hover(pg.mouse.get_pos(), self.participant_3_active,
                                                  self.participant_5_active)
        self.add_participant_5_button.check_hover(pg.mouse.get_pos(), self.participant_4_active, False)

        self.participant_0.check_hover(pg.mouse.get_pos())
        self.participant_1.check_hover(pg.mouse.get_pos())
        self.participant_2.check_hover(pg.mouse.get_pos())
        self.participant_3.check_hover(pg.mouse.get_pos())
        self.participant_4.check_hover(pg.mouse.get_pos())
        self.participant_5.check_hover(pg.mouse.get_pos())

        self.button_color_red.check_hover_bc(pg.mouse.get_pos())
        self.button_color_gray.check_hover_bc(pg.mouse.get_pos())
        self.button_color_blue.check_hover_bc(pg.mouse.get_pos())
        self.button_color_aquamarine.check_hover_bc(pg.mouse.get_pos())
        self.button_color_purple.check_hover_bc(pg.mouse.get_pos())
        self.button_color_orange.check_hover_bc(pg.mouse.get_pos())
        self.button_color_pink.check_hover_bc(pg.mouse.get_pos())
        self.button_color_green.check_hover_bc(pg.mouse.get_pos())
        self.button_color_yellow.check_hover_bc(pg.mouse.get_pos())

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

        self.participant_0.draw(self.participant_0_active)
        self.participant_1.draw(self.participant_1_active)
        self.participant_2.draw(self.participant_2_active)
        self.participant_3.draw(self.participant_3_active)
        self.participant_4.draw(self.participant_4_active)
        self.participant_5.draw(self.participant_5_active)

        self.add_participant_1_button.draw(self.participant_0_active, self.participant_2_active)
        self.add_participant_2_button.draw(self.participant_1_active, False)
        self.add_participant_4_button.draw(self.participant_3_active, self.participant_5_active)
        self.add_participant_5_button.draw(self.participant_4_active, False)

        self.screen_color_0.draw(self.open_change_color_par_0)
        self.screen_color_1.draw(self.open_change_color_par_1)
        self.screen_color_2.draw(self.open_change_color_par_2)
        self.screen_color_3.draw(self.open_change_color_par_3)
        self.screen_color_4.draw(self.open_change_color_par_4)
        self.screen_color_5.draw(self.open_change_color_par_5)

        self.button_color_red.draw(self.one_of_color_scr_open)
        self.button_color_gray.draw(self.one_of_color_scr_open)
        self.button_color_blue.draw(self.one_of_color_scr_open)
        self.button_color_aquamarine.draw(self.one_of_color_scr_open)
        self.button_color_purple.draw(self.one_of_color_scr_open)
        self.button_color_orange.draw(self.one_of_color_scr_open)
        self.button_color_pink.draw(self.one_of_color_scr_open)
        self.button_color_green.draw(self.one_of_color_scr_open)
        self.button_color_yellow.draw(self.one_of_color_scr_open)

    def chac_color_da(self, event, participant):
        if event.button == self.button_color_red:
            participant.get_color(self.button_color_red.self_color())
        if event.button == self.button_color_gray:
            participant.get_color(self.button_color_gray.self_color())
        if event.button == self.button_color_blue:
            participant.get_color(self.button_color_blue.self_color())
        if event.button == self.button_color_aquamarine:
            participant.get_color(self.button_color_aquamarine.self_color())
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

            self.participant_0.handle_event_par(event, self.participant_0_active)
            self.participant_1.handle_event_par(event, self.participant_1_active)
            self.participant_2.handle_event_par(event, self.participant_2_active)
            self.participant_3.handle_event_par(event, self.participant_3_active)
            self.participant_4.handle_event_par(event, self.participant_4_active)
            self.participant_5.handle_event_par(event, self.participant_5_active)

            self.button_color_red.handle_event_bc(event, self.one_of_color_scr_open)
            self.button_color_gray.handle_event_bc(event, self.one_of_color_scr_open)
            self.button_color_blue.handle_event_bc(event, self.one_of_color_scr_open)
            self.button_color_aquamarine.handle_event_bc(event, self.one_of_color_scr_open)
            self.button_color_purple.handle_event_bc(event, self.one_of_color_scr_open)
            self.button_color_orange.handle_event_bc(event, self.one_of_color_scr_open)
            self.button_color_pink.handle_event_bc(event, self.one_of_color_scr_open)
            self.button_color_green.handle_event_bc(event, self.one_of_color_scr_open)
            self.button_color_yellow.handle_event_bc(event, self.one_of_color_scr_open)

            if event.type == pg.USEREVENT:
                if self.open_change_color_par_0 is True:
                    self.chac_color_da(event, self.participant_0)
                if self.open_change_color_par_1 is True:
                    self.chac_color_da(event, self.participant_1)
                if self.open_change_color_par_2 is True:
                    self.chac_color_da(event, self.participant_2)
                if self.open_change_color_par_3 is True:
                    self.chac_color_da(event, self.participant_3)
                if self.open_change_color_par_4 is True:
                    self.chac_color_da(event, self.participant_4)
                if self.open_change_color_par_5 is True:
                    self.chac_color_da(event, self.participant_5)

                self.one_of_color_scr_open = False
                if event.button == self.participant_0:
                    self.one_of_color_scr_open = False
                    self.open_change_color_par_0 = True
                    self.screen_color_0.create_recttt()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rectttttttt()
                    self.button_color_gray.create_rectttttttt()
                    self.button_color_blue.create_rectttttttt()
                    self.button_color_aquamarine.create_rectttttttt()
                    self.button_color_purple.create_rectttttttt()
                    self.button_color_orange.create_rectttttttt()
                    self.button_color_pink.create_rectttttttt()
                    self.button_color_green.create_rectttttttt()
                    self.button_color_yellow.create_rectttttttt()
                else:
                    self.open_change_color_par_0 = False

                if event.button == self.participant_1:
                    self.one_of_color_scr_open = False
                    self.open_change_color_par_1 = True
                    self.screen_color_1.create_recttt()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rectttttttt()
                    self.button_color_gray.create_rectttttttt()
                    self.button_color_blue.create_rectttttttt()
                    self.button_color_aquamarine.create_rectttttttt()
                    self.button_color_purple.create_rectttttttt()
                    self.button_color_orange.create_rectttttttt()
                    self.button_color_pink.create_rectttttttt()
                    self.button_color_green.create_rectttttttt()
                    self.button_color_yellow.create_rectttttttt()
                else:
                    self.open_change_color_par_1 = False

                if event.button == self.participant_2:
                    self.one_of_color_scr_open = False
                    self.open_change_color_par_2 = True
                    self.screen_color_2.create_recttt()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rectttttttt()
                    self.button_color_gray.create_rectttttttt()
                    self.button_color_blue.create_rectttttttt()
                    self.button_color_aquamarine.create_rectttttttt()
                    self.button_color_purple.create_rectttttttt()
                    self.button_color_orange.create_rectttttttt()
                    self.button_color_pink.create_rectttttttt()
                    self.button_color_green.create_rectttttttt()
                    self.button_color_yellow.create_rectttttttt()
                else:
                    self.open_change_color_par_2 = False

                if event.button == self.participant_3:
                    self.one_of_color_scr_open = False
                    self.open_change_color_par_3 = True
                    self.screen_color_3.create_recttt()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rectttttttt()
                    self.button_color_gray.create_rectttttttt()
                    self.button_color_blue.create_rectttttttt()
                    self.button_color_aquamarine.create_rectttttttt()
                    self.button_color_purple.create_rectttttttt()
                    self.button_color_orange.create_rectttttttt()
                    self.button_color_pink.create_rectttttttt()
                    self.button_color_green.create_rectttttttt()
                    self.button_color_yellow.create_rectttttttt()
                else:
                    self.open_change_color_par_3 = False

                if event.button == self.participant_4:
                    self.one_of_color_scr_open = False
                    self.open_change_color_par_4 = True
                    self.screen_color_4.create_recttt()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rectttttttt()
                    self.button_color_gray.create_rectttttttt()
                    self.button_color_blue.create_rectttttttt()
                    self.button_color_aquamarine.create_rectttttttt()
                    self.button_color_purple.create_rectttttttt()
                    self.button_color_orange.create_rectttttttt()
                    self.button_color_pink.create_rectttttttt()
                    self.button_color_green.create_rectttttttt()
                    self.button_color_yellow.create_rectttttttt()
                else:
                    self.open_change_color_par_4 = False

                if event.button == self.participant_5:
                    self.one_of_color_scr_open = False
                    self.open_change_color_par_5 = True
                    self.screen_color_5.create_recttt()
                    self.one_of_color_scr_open = True

                    self.button_color_red.create_rectttttttt()
                    self.button_color_gray.create_rectttttttt()
                    self.button_color_blue.create_rectttttttt()
                    self.button_color_aquamarine.create_rectttttttt()
                    self.button_color_purple.create_rectttttttt()
                    self.button_color_orange.create_rectttttttt()
                    self.button_color_pink.create_rectttttttt()
                    self.button_color_green.create_rectttttttt()
                    self.button_color_yellow.create_rectttttttt()
                else:
                    self.open_change_color_par_5 = False

            self.start_button.handle_event(event)

            self.add_participant_1_button.handle_event(event, self.participant_0_active, self.participant_2_active)
            self.add_participant_2_button.handle_event(event, self.participant_1_active, False)
            self.add_participant_4_button.handle_event(event, self.participant_3_active, self.participant_5_active)
            self.add_participant_5_button.handle_event(event, self.participant_4_active, False)

            if event.type == pg.USEREVENT and event.button == self.add_participant_1_button:
                if self.participant_1_active is False:
                    self.participant_1_active = True
                    self.participant_1.get_rand_color(self.participant_1_active)
                else:
                    self.participant_1_active = False
                # print(f"self.participant_1_active = {self.participant_1_active}")
            if event.type == pg.USEREVENT and event.button == self.add_participant_2_button:
                if self.participant_2_active is False:
                    self.participant_2_active = True
                    self.participant_2.get_rand_color(self.participant_2_active)
                else:
                    self.participant_2_active = False
                # print(f"self.participant_2_active = {self.participant_2_active}")
            if event.type == pg.USEREVENT and event.button == self.add_participant_4_button:
                if self.participant_4_active is False:
                    self.participant_4_active = True
                    self.participant_4.get_rand_color(self.participant_4_active)
                else:
                    self.participant_4_active = False
                # print(f"self.participant_4_active = {self.participant_4_active}")
            if event.type == pg.USEREVENT and event.button == self.add_participant_5_button:
                if self.participant_5_active is False:
                    self.participant_5_active = True
                    self.participant_5.get_rand_color(self.participant_5_active)
                else:
                    self.participant_5_active = False
                # print(f"self.participant_5_active = {self.participant_5_active}")

            # print(self.allies_list)
            # print(self.opponents_list)

    def run(self):
        """
        Работа программы, как процесс
        """
        self.participant_0.get_rand_color(self.participant_0_active)
        self.participant_3.get_rand_color(self.participant_3_active)

        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = MainGame()
    game.run()
