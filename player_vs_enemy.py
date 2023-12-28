import random


class Character:
    def __init__(self, speed):
        self.speed = speed

    def action(self):
        input("Введите цифру 1:")


def game():
    player = Character(random.randint(1, 10))
    enemy = Character(random.randint(1, 10))

    print(f"Ваша скорость: {player.speed}")
    print(f"Скорость противника: {enemy.speed}")

    if player.speed > enemy.speed:
        # Если у игрока больше speed, то он ходит первым
        print("Вы ходите первым!")
        # Вызываем метод action для игрока
        player.action()
        # Затем вызываем метод action для противника
        enemy.action()
    elif player.speed < enemy.speed:
        # Если у противника больше speed, то он ходит первым
        print("Противник ходит первым!")
        # Вызываем метод action для противника
        enemy.action()
        # Затем вызываем метод action для игрока
        player.action()
    else:
        # Если у обоих одинаковый speed, то выбираем случайно, кто ходит первым
        print("Ничья! Выбираем случайно, кто ходит первым!")
        # Генерируем случайное число от 0 до 1
        coin = random.randint(0, 1)
        if coin == 0:
            # Если выпало 0, то ходит игрок
            print("Вы ходите первым!")
            # Вызываем метод action для игрока
            player.action()
            # Затем вызываем метод action для противника
            enemy.action()
        else:
            # Если выпало 1, то ходит противник
            print("Противник ходит первым!")
            # Вызываем метод action для противника
            enemy.action()
            # Затем вызываем метод action для игрока
            player.action()


if __name__ == "__main__":
    game()
