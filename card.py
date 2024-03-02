import pygame as pg


class Card:
    def __init__(self, game, value):
        self.game = game
        self.value = value
        self.w = 70  # Ширина
        self.h = 100  # Высота
        self.rect = pg.Rect(0, 0, self.w, self.h)

    def draw(self):
        card = self.rect  # используем атрибут self.rect вместо вызова метода self.rect()
        pg.draw.rect(self.game.screen, "white", card)

        # Подключение шрифта (базово - базовый)
        font = pg.font.Font(None, 50)
        # Рендеринг текста
        text_surface = font.render(str(self.value), True, "black")
        # rect текста (создание невидимой обводки текста)
        text_rect = text_surface.get_rect(center=(card.centerx, card.centery))  # центрируем текст по центру карточки
        # Вывод текста
        self.game.screen.blit(text_surface, text_rect)

    # def rect(self):
    #     return pg.Rect(0, 0, self.w, self.h)

    def card_value(self):
        return str(self.value)
