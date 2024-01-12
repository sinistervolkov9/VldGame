import sys
from settings import *
import pygame as pg
from scene_init import Scene

class Game:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.scene = Scene(current_scene="scene_0")

    def update(self):
        '''
        Метод обновления экрана (flip)
        '''
        self.scene.screen_updater(self.screen)
        self.scene.button_updater(self.screen)
        pg.display.flip()
        self.clock.tick(FPS) # Чилсо итераций (обновлений основного цикла игры за одну секунду)
        pg.display.set_caption("Vld Game")
        # pg.display.set_caption(f"{self.clock.get_fps() :.1f}")


    def draw(self):
        '''
        Метод нанасения на экран чего-либо
        (рисование, заливка).
        Видимо здесь должны подгружаться менюшки
        '''
        self.screen.fill("black")

    def check_events(self):
        '''
        Проверка на нажатие кнопок и т. п.
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.scene.event_updater(event)
            self.scene.event_keydown(event)
            self.scene.user_event(event)
            self.scene.button_handle_event(event)

    def run(self):
        '''
        Работа программы, как процесс
        '''
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
