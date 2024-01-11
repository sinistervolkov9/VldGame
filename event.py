# class Event:
#     pass
#
# class EscEvent(Event):
#     def __init__(self):
#         pass
#
#     def
#     for event in pg.event.get():
#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_ESCAPE:
#                 scenes_history.pop()
#                 current_scene = scenes_history[-1]
#
# class SoundEvent(Event):
#     # Фоновая музыка (звуки), если есть:
#     if self.sound:
#         self.sound.play()

import pygame as pg


class Event:
    def __init__(self, game):
        self.game = game

    def moving(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    print("Вперед")
                elif event.key == pg.K_s:
                    print("Назад")
                elif event.key == pg.K_a:
                    print("Влево")
                elif event.key == pg.K_d:
                    print("Вправо")
