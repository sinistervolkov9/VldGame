import pygame as pg
import random


class FreeItem:
    pass

# ----------------------------------------------------------------------------------------------------------------------


class FreeItemText:
    def __init__(self, game, text, x):
        self.game = game
        self.text = text
        self.x = x

        if text:
            self.text = text
        else:
            self.text = "None"

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


# Прямоугольник, на котором будет выводиться текст. Цвет прямоугольника тоже меняется
class FreeItemParticipant:
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

    def get_rand_color(self):
        # if status is True:
        #     self.colors_list = ["red", "gray", "blue", "brown", "purple", "orange", "pink", "green"]
        #     index = random.randint(0, len(self.colors_list) - 1)
        #     self.color = self.colors_list[index]
        # else:
        #     self.color = "white"

        self.colors_list = ["red", "gray", "blue", "brown", "purple", "orange", "pink", "green"]
        index = random.randint(0, len(self.colors_list) - 1)
        self.color = self.colors_list[index]

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
