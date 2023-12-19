import pygame as pg

pg.init()  # инициализируем PyGame

WIDTH = 800  # ширина экрана
HEIGHT = 600  # высота экрана
screen = pg.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана

current_screen = None


def switch_screens(screen):  # "Переключись на (сцену)
    global current_screen
    current_screen = screen


def screen_1():

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                switch_screens(None)
                # pg.quit()
                # sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    switch_screens(screen_2)
                    running = False
                elif event.key == pg.K_ESCAPE:
                    running = False
                    switch_screens(None)
                    # pg.quit()
                    # sys.exit()
                    # switch_screens(screen_2)
                    # running = False

        screen.fill("black")

        pg.display.flip()


def screen_2():

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                switch_screens(None)
                # pg.quit()
                # sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    switch_screens(screen_3)
                    running = False
                elif event.key == pg.K_ESCAPE:
                    switch_screens(screen_1)
                    running = False

        screen.fill("white")

        pg.display.flip()


def screen_3():

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                switch_screens(None)
                # pg.quit()
                # sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    switch_screens(screen_4)
                    running = False
                elif event.key == pg.K_ESCAPE:
                    switch_screens(screen_2)
                    running = False

        screen.fill("green")

        pg.display.flip()


def screen_4():

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                switch_screens(None)
                # pg.quit()
                # sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    switch_screens(screen_4)
                    running = False
                elif event.key == pg.K_ESCAPE:
                    switch_screens(screen_3)
                    running = False

        screen.fill("blue")

        pg.display.flip()


switch_screens(screen_1)
while current_screen is not None:
    current_screen()
