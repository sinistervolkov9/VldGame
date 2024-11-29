import pygame as pg
from settings import CARD_HEIGHT, CARD_WIDTH, FRAME_WIDTH, CARD_SCALE, SCREEN_POS


class CardLoot:
    def __init__(self, game,
                 image, description_block, frame, name_block,
                 name, description,
                 loot_type, rarity, renewable_type, copies_number,
                 characteristic_for_check, cost, application_speed,
                 damage, armor,
                 spells: list, perks: list):

        self.game = game

        self.image = image
        self.description_block = description_block
        self.frame = frame
        self.name_block = name_block

        self.name = " ".join(name.upper().split())
        self.description = " ".join(description.split())

        self.loot_type = loot_type  # Тип Лута (Головняк, Броник...)
        self.rarity = rarity  # Редкость (basic...)
        self.renewable_type = renewable_type  # Тип возобновляемости Лута в колоде (возобновляемая (неуничтожаемая) / одноразовая)
        self.copies_number = copies_number  # Количество копий карточки в колоде

        self.characteristic_for_check = characteristic_for_check  # Проверяемая характиристка
        self.cost = cost  # Стоимость применения
        self.application_speed = application_speed  # Скорость применения (Мгновенное, Быстрое, Медленное)

        self.damage = damage
        self.armor = armor

        self.spells = spells
        self.perks = perks

        # ---

        self.scale = CARD_SCALE  # ?
        self.w = CARD_WIDTH  # Ширина
        self.h = CARD_HEIGHT  # Высота
        self.pos_x = SCREEN_POS['c'][0] - self.w * self.scale / 2
        self.pos_y = SCREEN_POS['c'][1] - self.h * self.scale / 2
        self.scale = 100  # 100
        self.is_hovered = False

        # ---

        self.load_images()

        # ---

        # self.font_size_name = 40
        # self.font_size_description = 30
        #
        # self.font_size_damage = 30
        # self.font_size_armor = 30

        # ---

        self.get_size_pos()
        self.update()  # ?

    def load_images(self):

        self.background = pg.image.load("resources/card_items/background/background.png")
        self.image = pg.image.load(self.image)
        self.description_block = pg.image.load(self.description_block)
        self.frame = pg.image.load(self.frame)
        self.name_block = pg.image.load(self.name_block)

        self.damage_block = pg.image.load('resources/card_items/damage_block/damage_block.png')
        self.armor_block = pg.image.load('resources/card_items/armor_block/armor_block.png')

    def get_size_pos(self):

        self.size_background = (self.w * self.scale, self.h * self.scale)
        self.pos_background = (self.pos_x, self.pos_y)

        self.size_image = (self.w * self.scale, self.h / 1.5 * self.scale)
        self.pos_image = (self.pos_x, self.pos_y)

        self.size_description_block = ((self.w * self.scale) - FRAME_WIDTH,
                                       (self.h / 2 * self.scale) - (self.h / 6 * self.scale) - FRAME_WIDTH / 2)
        self.pos_description_block = (
            self.pos_x + FRAME_WIDTH / 2, self.pos_y + (self.h / 2 * self.scale) + (self.h / 6 * self.scale))

        self.size_frame = (self.w * self.scale, self.h * self.scale)
        self.pos_frame = (self.pos_x, self.pos_y)

        self.size_name_block = (self.w * self.scale - FRAME_WIDTH / 2, self.h / 6 * self.scale)
        self.pos_name_block = (self.pos_x + FRAME_WIDTH / 4, self.pos_y + self.h / 2 * self.scale)

        # ---

        self.size_damage_block = (30, 30)
        self.pos_damage_block = (5, self.h * self.scale - 35)

        self.size_armor_block = (30, 30)
        self.pos_armor_block = (self.w * self.scale - 35, self.h * self.scale - 35)

    def get_font_size_name(self):
        number_of_reductions = 4  # 4

        start_number_of_symbols = 7  # 7
        add_symbols = 2  # 2

        symbols_scale = 0.6  # 0.6
        add_scale = 0.05  # 0.05

        if len(self.name) > int(start_number_of_symbols + number_of_reductions * add_symbols - add_symbols):
            self.name = self.name[
                        :int(start_number_of_symbols + number_of_reductions * add_symbols - add_symbols) - 3] + "..."
            end_symbols_scale = symbols_scale + add_scale * (number_of_reductions - 1)
            self.font_size_name = int(self.scale - self.scale * end_symbols_scale)
        else:
            for i in range(number_of_reductions):
                if len(self.name) <= start_number_of_symbols:
                    self.font_size_name = int(self.scale - self.scale * symbols_scale)
                    break
                else:
                    symbols_scale += add_scale
                    start_number_of_symbols += add_symbols

    def get_font_size_description(self):
        number_of_reductions = 4  # 4

        start_number_of_symbols = 11  # 11
        add_symbols = 2.5  # 2.5

        symbols_scale = 0.75  # 0.75
        add_scale = 0.015  # 0.015

        if len(self.description) > int(start_number_of_symbols + number_of_reductions * add_symbols - add_symbols):
            self.description = self.description[
                               :int(
                                   start_number_of_symbols + number_of_reductions * add_symbols - add_symbols) - 3] + "..."
            end_symbols_scale = symbols_scale + add_scale * (number_of_reductions - 1)
            self.font_size_description = int(self.scale - self.scale * end_symbols_scale)
        else:
            for i in range(number_of_reductions):
                if len(self.description) <= start_number_of_symbols:
                    self.font_size_description = int(self.scale - self.scale * symbols_scale)
                    break
                else:
                    symbols_scale += add_scale
                    start_number_of_symbols += add_symbols

    def get_font_size_stats(self):
        font_scale = 0.34

        self.font_size_damage = int(self.scale * font_scale)
        self.font_size_armor = int(self.scale * font_scale)

        self.font_size_strength = int(self.scale * font_scale)
        self.font_size_dexterity = int(self.scale * font_scale)
        self.font_size_intelligence = int(self.scale * font_scale)

    def update(self):

        self.background = pg.transform.scale(self.background, self.size_background)
        self.background_rect = self.background.get_rect(topleft=self.pos_background)

        self.image = pg.transform.scale(self.image, self.size_image)
        self.image_rect = self.image.get_rect(topleft=self.pos_image)

        self.description_block = pg.transform.scale(self.description_block, self.size_description_block)
        self.description_block_rect = self.description_block.get_rect(
            topleft=self.pos_description_block)

        self.frame = pg.transform.scale(self.frame, self.size_frame)
        self.frame_rect = self.frame.get_rect(topleft=self.pos_frame)

        self.name_block = pg.transform.scale(self.name_block, self.size_name_block)
        self.name_block_rect = self.name_block.get_rect(topleft=self.pos_name_block)

        self.damage_block = pg.transform.scale(self.damage_block, self.size_damage_block)
        self.damage_block_rect = self.damage_block.get_rect(topleft=self.pos_damage_block)

        self.armor_block = pg.transform.scale(self.armor_block, self.size_armor_block)
        self.armor_block_rect = self.armor_block.get_rect(topleft=self.pos_armor_block)

        # ---

        self.get_font_size_name()
        self.get_font_size_description()
        self.get_font_size_stats()

        # ---

        name_font = pg.font.Font(None, self.font_size_name)
        self.name_text_surface = name_font.render(str(self.name), True, "white")
        self.name_text_rect = self.name_text_surface.get_rect(
            center=(self.name_block_rect.centerx, self.name_block_rect.centery))

        description_font = pg.font.Font(None, self.font_size_description)
        self.description_text_surface = description_font.render(str(self.description), True, "white")
        self.description_text_rect = self.description_text_surface.get_rect(
            center=(self.description_block_rect.centerx, self.description_block_rect.centery))

        damage_font = pg.font.Font(None, self.font_size_damage)
        self.damage_text_surface = damage_font.render(str(self.damage), True, "white")
        self.damage_text_rect = self.damage_text_surface.get_rect(
            center=(self.damage_block_rect.centerx, self.damage_block_rect.centery))

        armor_font = pg.font.Font(None, self.font_size_armor)
        self.armor_text_surface = armor_font.render(str(self.armor), True, "white")
        self.armor_text_rect = self.armor_text_surface.get_rect(
            center=(self.armor_block_rect.centerx, self.armor_block_rect.centery))

    def draw(self):

        self.game.screen.blit(self.background, self.frame_rect.topleft)
        self.game.screen.blit(self.description_block, self.description_block_rect.topleft)
        self.game.screen.blit(self.frame, self.frame_rect.topleft)
        self.game.screen.blit(self.image, self.image_rect.topleft)
        self.game.screen.blit(self.name_block, self.name_block_rect.topleft)

        self.game.screen.blit(self.damage_block, self.damage_block_rect.topleft)
        self.game.screen.blit(self.armor_block, self.armor_block_rect.topleft)

        # ---

        self.game.screen.blit(self.name_text_surface, self.name_text_rect)
        self.game.screen.blit(self.description_text_surface, self.description_text_rect)

        # ---

        self.game.screen.blit(self.damage_text_surface, self.damage_text_rect)
        self.game.screen.blit(self.armor_text_surface, self.armor_text_rect)

    def check_simbols(self):
        print(f'{self.name} - simb_count: {len(self.name)} - size: {self.font_size_name}')
        print(f'{self.description} - simb_count: {len(self.description)} - size: {self.font_size_description}')
