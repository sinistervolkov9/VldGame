import pygame as pg
import random


# pg.init()
#
# #game window
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 450
#
# screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pg.display.set_caption('Drag And Drop')
#
# active_box = None
# boxes = []
# for i in range(4):
#   x = random.randint(50, 700)  # Позиция по x
#   y = random.randint(50, 350)  # Позиция по y
#   w = 70  # Ширина
#   h = 100  # Высота
#   box = pg.Rect(x, y, w, h)
#   boxes.append(box)
#
# run = True
# while run:
#
#   screen.fill("black")
#
#   #update and draw items
#   for box in boxes:
#     pg.draw.rect(screen, "white", box)
#
#   for event in pg.event.get():
#     if event.type == pg.MOUSEBUTTONDOWN:
#       if event.button == 1:
#         for num, box in enumerate(boxes):
#           if box.collidepoint(event.pos):
#             active_box = num
#
#     if event.type == pg.MOUSEBUTTONUP:
#       if event.button == 1:
#         active_box = None
#
#     if event.type == pg.MOUSEMOTION:
#       if active_box != None:
#         boxes[active_box].move_ip(event.rel)
#
#     if event.type == pg.QUIT:
#       run = False
#
#   pg.display.flip()
#
# pg.quit()

# ------------------------------------------------------------

class Gameeee:
    def __init__(self):
        self.active_box = None
        self.boxes = []
        self.create_cards()

    def create_cards(self):
        for i in range(4):
            x = random.randint(0, 600)  # Позиция по x
            y = random.randint(0, 400)  # Позиция по y
            w = 70  # Ширина
            h = 100  # Высота
            box = pg.Rect(x, y, w, h)
            self.boxes.append(box)

    def draw_cards(self, screen):
        for box in self.boxes:
            pg.draw.rect(screen, "white", box)

    def check_eventtt(self, event):
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
