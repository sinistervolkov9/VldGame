import pygame as pg


# Интерактивные штуки, отображаемые на экране
class ScreenItem:
    def __init__(
            self,
            image=None,
            x=0, y=0, width=50, height=50,

            text=None, font=None, text_color=None,
            text_size=None
    ):

        self.image = image  # Отображаемое изображение

        self.text = text  # Выводимый на заднем фоне текст (если надо)
        self.font = font  # Шрифт выводимого текста (будет постоянный для всех состояний текста)
        self.text_color = text_color  # Цвет выводимого текста
        self.text_size = text_size

        self.x = x  # Позиция по x-координате
        self.y = y  # Позиция по y-координате
        self.width = width  # Длина изображения
        self.height = height  # Высота изображения

        # Работа с аргументами-переменными 1:
        # image
        if self.image:
            self.image = "C:/py progects/VldGame_/resources/button_images/" + image

            # Подгрузка изображения кнопки
            self.image = pg.image.load(self.image)
            self.image = pg.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect(topleft=(x, y))  # rect

        else:
            self.image = None

        # text
        if text:
            self.text = text

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

        else:
            self.text = None

    def draw(self, screen):
        # Отображение
        if self.image:
            screen.blit(self.image, self.rect.topleft)

        if self.text:
            # Подключение шрифта (базово - базовый)
            font = pg.font.Font(self.font, int(self.text_size))

            # Рендеринг текста
            text_surface = font.render(self.text, True, self.text_color)

            # rect текста (создание невидимой обводки текста)
            text_rect = text_surface.get_rect(center=self.rect.center)

            # Вывод текста
            screen.blit(text_surface, text_rect)
