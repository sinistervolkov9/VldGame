import pygame as pg
from settings import BASE_HP, HEALTH_COEFFICIENT, HEALTH_DECREASE_FACTOR, BASE_SPEED, SPEED_COEFFICIENT, \
    SPEED_DECREASE_FACTOR


class Player:
    def __init__(self, game,
                 card_class,
                 level,
                 strength, dexterity, intelligence,
                 stamina):

        if strength < 1 or dexterity < 1 or intelligence < 1:
            raise ValueError("Аргументы strength, dexterity, intelligence должны быть больше 0")

        # ---

        self.game = game

        self.level = level

        self.card_class = card_class

        self.strength = self.card_class.strength + strength
        self.dexterity = self.card_class.dexterity + dexterity
        self.intelligence = self.card_class.intelligence + intelligence

        self.stamina = stamina

        # ---

        self.base_hp = BASE_HP
        self.health_coefficient = HEALTH_COEFFICIENT
        self.health_decrease_factor = HEALTH_DECREASE_FACTOR

        self.base_speed = BASE_SPEED
        self.speed_coefficient = SPEED_COEFFICIENT
        self.speed_decrease_factor = SPEED_DECREASE_FACTOR

        # ---

        self.hit_points = self.calculate_hit_points()
        self.speed = self.calculate_speed()

    def calculate_hit_points(self):
        hit_points = self.base_hp
        decrease_factor = self.health_decrease_factor

        for i in range(self.strength - 1):
            hit_points += int(self.health_coefficient / (1 + decrease_factor))
            decrease_factor += self.health_decrease_factor

            # increase_from_base = hit_points - self.base_hp
            # print(f"Strength = {self.strength}: Hit Points = {hit_points} (Увеличение: +{increase_from_base} от базового значения)")

        return hit_points

    def calculate_speed(self):
        speed = self.base_speed
        decrease_factor = self.speed_decrease_factor

        for i in range(self.dexterity - 1):
            speed += int(self.speed_coefficient / (1 + decrease_factor))
            decrease_factor += self.speed_decrease_factor

            # increase_from_base = speed - self.base_speed
            # print(f"dexterity = {self.dexterity}: Hit Points = {speed} (Увеличение: +{increase_from_base} от базового значения)")

        return speed

    def print_stats(self):
        print(
            f'Сила - {self.strength}; Ловкость - {self.dexterity}; Интеллект - {self.intelligence}; Стамина - {self.stamina}')
        print(f'Урон - {self.card_class.damage}; Броня - {self.card_class.armor}')
        print(f'ХП - {self.hit_points}; Скорость - {self.speed}')
