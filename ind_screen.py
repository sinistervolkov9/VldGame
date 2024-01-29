import pygame as pg
from settings import WIDTH, HEIGHT


# Фоновое изображение
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


# ----------------------------------------------------------------------------------------------------------------------

class ScreenRect:
    def __init__(
            self, game
    ):
        self.game = game
        self.width = 120  # Длина фонового изображения
        self.height = 120  # Высота фонового изображения
        self.screennnn = None

    def create_rect_scr(self):
        x, y = pg.mouse.get_pos()

        x_1 = x + self.width
        if x_1 > WIDTH:
            x = WIDTH - 120

        y_1 = y + self.height
        if y_1 > HEIGHT:
            y = HEIGHT - 120

        self.screennnn = pg.Rect(x, y, self.width, self.height)

    def draw(self, status):
        """
        pass
        """
        if status is True:
            pg.draw.rect(self.game.screen, "black", self.screennnn)
