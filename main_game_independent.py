import sys
from settings import *
import pygame as pg


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

class Area:
    def __init__(self, x, y, w, h, color):
        self.area = None
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.create_area()

    def create_area(self):
        self.area = pg.Rect(self.x, self.y, self.w, self.h)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.area)


# ----------------------------------------------------------------------------------------------------------------------

class Player:
    pass


# ----------------------------------------------------------------------------------------------------------------------

class Deck:
    def __init__(self, game, number_of_cards):
        self.game = game
        self.number_of_cards = number_of_cards
        self.active_box = None
        self.boxes = []
        self.create_cards()

    def create_cards(self):
        for i in range(self.number_of_cards):
            x = self.check_players_num()  # Позиция по x (зависит от количества игроков !!!и порядкового номера игрока)
            y = 250  # Позиция по y
            w = 70  # Ширина
            h = 100  # Высота
            card = pg.Rect(x, y, w, h)
            self.boxes.append(card)

    def check_players_num(self):  # еще зависит от порядкого номера игрока
        return WIDTH / 2 - (70 * self.game.players / 2)

    def draw(self):
        for box in self.boxes:
            pg.draw.rect(self.game.screen, "white", box)

    def check_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(self.boxes):
                    if box.collidepoint(event.pos):
                        self.active_box = num

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                self.active_box = None

        if event.type == pg.MOUSEMOTION:
            if self.active_box != None:
                self.boxes[self.active_box].move_ip(event.rel)


# ----------------------------------------------------------------------------------------------------------------------

class MainGame:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

        self.players = 1

        self.new_game()

    def players(self):
        player_1 = Player()
        player_2 = Player()
        player_3 = None

        playerssss = [{"player_1": player_1}, {"player_2": player_2}, {"player_3": player_3}]

    def new_game(self):
        self.game_screen = Screen(self, "default_background.jpg",
                                  0, 0, WIDTH, HEIGHT,
                                  "ИГРА ТИПА...",
                                  None, "white", 50)
        self.turn_button = Button(self, "Ход", None,
                                  "white", "black", "green",
                                  "b.png", "g.png", "r.png",
                                  "dig_click_03.wav", "mouse_click_04.wav",
                                  500, 170, 60, 60)
        self.player_hand_area = Area(WIDTH / 2 - (300 / 2), 350, 300, 100, "blue")
        self.enemy_hand_area = Area(WIDTH / 2 - (300 / 2), -50, 300, 100, "red")
        self.allies_area = Area(WIDTH / 2 - (420 / 2), 250, 420, 100, "blue")
        self.enemys_area = Area(WIDTH / 2 - (420 / 2), 50, 420, 100, "red")
        self.game_cards_area = Area(WIDTH / 2 - (500 / 2), 150, 500, 100, "green")
        self.deck = Deck(self, 5)

    def update(self):
        """
        Метод обновления экрана (flip)
        """
        self.turn_button.check_hover(pg.mouse.get_pos())

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
        self.turn_button.draw()

        self.player_hand_area.draw(self.screen)
        self.enemy_hand_area.draw(self.screen)
        self.allies_area.draw(self.screen)
        self.enemys_area.draw(self.screen)
        self.game_cards_area.draw(self.screen)

        self.deck.draw()

    def check_events(self):
        """
        Проверка на нажатие кнопок и т. п.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.turn_button.handle_event(event)
            self.deck.check_event(event)

    def run(self):
        """
        Работа программы, как процесс
        """
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = MainGame()
    game.run()
