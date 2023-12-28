from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS  # Начальное положение игрока. Проверка на количество союзников
        self.health = PLAYER_LVL
        self.speed = PLAYER_SPEED
        self.endurance = PLAYER_START_ENDURANCE

    def check_game_win(self):
        pass

    def check_game_over(self):
        if self.health < 1:
            pass

    def