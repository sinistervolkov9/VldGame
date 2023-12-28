# Импортируем pygame
import pygame as pg

# Инициализируем pygame
pg.init()

# Создаем окно
screen = pg.display.set_mode((800, 600))

# Задаем цвет фона
background_color = (255, 255, 255)

# Определяем пользовательское событие
MYEVENT = pg.USEREVENT + 0

# Запускаем таймер, который будет посылать пользовательское событие каждую секунду
pg.time.set_timer(MYEVENT, 1000)

# Создаем переменную для хранения счетчика
counter = 0

# Создаем основной цикл
running = True
while running:
    # Обрабатываем события
    for event in pg.event.get():
        # Если нажата кнопка закрытия окна, выходим из цикла
        if event.type == pg.QUIT:
            running = False
        # Если получено пользовательское событие, увеличиваем счетчик и меняем цвет фона
        elif event.type == MYEVENT:
            counter += 1
            background_color = (counter * 10 % 256, counter * 20 % 256, counter * 30 % 256)

    # Заполняем фон цветом
    screen.fill(background_color)

    # Обновляем экран
    pg.display.flip()

# Завершаем pygame
pg.quit()
