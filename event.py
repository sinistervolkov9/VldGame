import pygame as pg
import random

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


class Event:
    def __init__(self, game):
        self.game = game

    def moving(self, event):
        # for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    print("Вперед")
                elif event.key == pg.K_s:
                    print("Назад")
                elif event.key == pg.K_a:
                    print("Влево")
                elif event.key == pg.K_d:
                    print("Вправо")

    def drag_drop(self, screen):
        active_box = None
        boxes = []
        for i in range(5):
            x = random.randint(50, 700)
            y = random.randint(50, 350)
            w = random.randint(35, 65)
            h = random.randint(35, 65)
            box = pg.Rect(x, y, w, h)
            boxes.append(box)

        run = True
        while run:
            # update and draw items
            for box in boxes:
                pg.draw.rect(screen, "purple", box)

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for num, box in enumerate(boxes):
                            if box.collidepoint(event.pos):
                                active_box = num

                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        active_box = None

                if event.type == pg.MOUSEMOTION:
                    if active_box != None:
                        boxes[active_box].move_ip(event.rel)

                if event.type == pg.QUIT:
                    run = False
