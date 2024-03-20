import sys
from settings import *
import pygame as pg
# from scene_init import Scene
from card import ClassCard


class Game:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        # self.mouse_pos = pg.mouse.get_pos()
        self.new_game()

    def new_game(self):
        # self.scene = Scene(current_scene="scene_main_menu")
        self.card = ClassCard(self, "resources/card_items/image/image.png",
                              "resources/card_items/description_block/description_block.png",
                              "resources/card_items/frame/frame.png", "resources/card_items/name_block/name_block.png",
                              "лёха)", "Описание",
                              0, 0,
                              3, 2, 1,
                              3, 5, 10)

    def update(self):
        """
        Метод обновления экрана (flip)
        """
        # self.scene.button_update(self.screen)
        pg.display.flip()
        self.clock.tick(FPS)  # Чилсо итераций (обновлений основного цикла игры за одну секунду)
        pg.display.set_caption("Vld Game")

        self.card.card_check_hover(pg.mouse.get_pos())

    def draw(self):
        """
        Метод нанасения на экран чего-либо
        (рисование, заливка).
        Видимо здесь должны подгружаться менюшки
        """
        self.screen.fill("black")
        # self.scene.screen_draw(self.screen)
        self.card.draw()

    def check_events(self):
        """
        Проверка на нажатие кнопок и т. п.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        # self.card.card_hover_event()

        # self.scene.esc_event(event)
        # self.scene.button_click_event(event)
        # self.scene.button_handle_event(event)
        # self.scene.click_event(event)

    def run(self):
        """
        Работа программы, как процесс
        """
        self.card.check_simbols()
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
