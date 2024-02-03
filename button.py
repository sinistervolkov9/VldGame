import pygame as pg

pg.init()


# Кнопка сама по себе
class Button:
    def __init__(
            self,
            text: str = None, font=None,
            text_color=None, text_color_hover=None, text_color_click=None,
            image=None, image_hover=None, image_click=None, sound_hover=None, sound_click=None,
            x=0, y=0, width=200, height=60,
            visible=True, activity=True
    ):

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

        self.visible = visible
        self.activity = activity

        # self.functions = functions  # Список функциональных возможностей кнопки
        # self.display_trigger = {"display_trigger": True}  # Словарь для триггера видимости кнопки

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
            self.font = None

        # text_color
        if text_color:
            self.text_color = text_color
        else:
            self.text_color = "black"

        # text_color_hover
        if text_color_hover:
            self.text_color_hover = text_color_hover
        else:
            self.text_color_hover = self.text_color

        # text_color_click
        if text_color_click:
            self.text_color_click = text_color_click
        else:
            self.text_color_click = self.text_color

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
            self.sound_hover = None

        # sound_click
        if sound_click:
            if sound_click == "default":
                self.sound_click = "resources/sounds/default_sound_click.wav"
            else:
                self.sound_click = "resources/sounds/" + sound_click
        else:
            self.sound_click = None

        # Работа с аргументами-переменными 2:
        # Подгрузка изображения кнопки
        self.image = pg.image.load(self.image)
        self.image = pg.transform.scale(self.image, (width, height))

        # Изображение кнопки при наведении (если будет добавлено)
        if self.image_hover:
            self.image_hover = pg.image.load(self.image_hover)
            self.image_hover = pg.transform.scale(self.image_hover, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))  # rect

        # Изображение кнопки при нажатии (если будет добавлено)
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

    def draw(self, screen):
        """
        Метод, который позволит нарисовать кнопку.
        В него передаем экран, на котором будет рисоваться кнопка
        """
        if self.visible:
            # Чтобы понять, какую картинку и какого цвета текст необх. отобразить
            if self.is_clicked:
                current_image = self.image_click
                current_text_color = self.color_click
            elif self.is_hovered:
                current_image = self.image_hover
                current_text_color = self.color_hover
            else:
                current_image = self.image
                current_text_color = self.text_color

            # Отображение кнопки:
            screen.blit(current_image, self.rect.topleft)

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
            screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        """
        Проверяет, наведена мышка на кнопку или нет
        """
        if self.activity:
            self.is_hovered = self.rect.collidepoint(mouse_pos)
        # if self.visible:
        #     self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        """
        Метод обрабоки событий
        """
        if self.visible:

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

    def switch_visibility(self):
        """
        Меняет значение триггера видимости на противоположное
        """
        self.visible = not self.visible

    def switch_activity(self):
        self.activity = not self.activity


# ----------------------------------------------------------------------------------------------------------------------

class ButtonOld:
    def __init__(
            self,
            text: str = None, font=None,
            text_color=None, text_color_hover=None, text_color_click=None,
            image=None, image_hover=None, image_click=None, sound_hover=None, sound_click=None,
            x=0, y=0, width=200, height=60):

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

    def draw(self, screen, trigger):
        """
        Метод, который позволит нарисовать кнопку.
        В него передаем экран, на котором будет рисоваться кнопка
        """
        if bool(trigger) is True:
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
            screen.blit(current_image, self.rect.topleft)

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
            screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos, trigger):
        """
        Проверяет, наведена мышка на кнопку или нет
        """
        if bool(trigger) is True:
            self.is_hovered = self.rect.collidepoint(mouse_pos)

        # if self.rect.collidepoint(mouse_pos):
        #     self.is_hovered = True

    def handle_event(self, event, trigger):
        """
        Метод обрабоки событий
        """
        if bool(trigger) is True:
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
