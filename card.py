import pygame as pg
from settings import CARD_HEIGHT, CARD_WIDTH


class Card:
    def __init__(self, game, image, description_block, frame, name_block,
                 name, description):

        self.game = game
        self.w = CARD_WIDTH  # Ширина
        self.h = CARD_HEIGHT  # Высота
        self.scale = 50

        self.image = image
        self.description_block = description_block
        self.frame = frame
        self.name_block = name_block

        self.name = " ".join(name.upper().split())
        self.description = " ".join(description.split())

        # self.font_size_name = int(self.scale-self.scale*0.6)  # 40
        self.font_size_name = None
        self.font_size_description = int(self.scale - self.scale * 0.7)  # 30

        self.get_font_size_name()
        # self.get_font_size_description()

        # ---

        self.background = pg.image.load("resources/button_images/default_button.png")
        self.background = pg.transform.scale(self.background, (self.w * self.scale, self.h * self.scale))
        self.background_rect = self.background.get_rect(topleft=(0, 0))

        # self.rect = pg.Rect(0, 0, self.w, self.h)
        self.image = pg.image.load(self.image)
        self.image = pg.transform.scale(self.image, (self.w * self.scale, self.h / 2 * self.scale))
        self.image_rect = self.image.get_rect(topleft=(0, 0))

        self.description_block = pg.image.load(self.description_block)
        self.description_block = pg.transform.scale(self.description_block,
                                                    (self.w * self.scale, self.h / 2 * self.scale))
        self.description_block_rect = self.description_block.get_rect(topleft=(0, self.h / 2 * self.scale))

        self.frame = pg.image.load(self.frame)
        self.frame = pg.transform.scale(self.frame, (self.w * self.scale, self.h * self.scale))
        self.frame_rect = self.frame.get_rect(topleft=(0, 0))

        self.name_block = pg.image.load(self.name_block)
        self.name_block = pg.transform.scale(self.name_block, (self.w * self.scale - 10, self.h / 6 * self.scale))
        self.name_block_rect = self.name_block.get_rect(topleft=(5, self.h / 2 * self.scale))

    def draw(self):
        # card = self.rect
        # pg.draw.rect(self.game.screen, "white", card)

        self.game.screen.blit(self.image, self.image_rect.topleft)
        self.game.screen.blit(self.description_block, self.description_block_rect.topleft)
        self.game.screen.blit(self.frame, self.frame_rect.topleft)
        self.game.screen.blit(self.name_block, self.name_block_rect.topleft)

        #

        name_font = pg.font.Font(None, self.font_size_name)
        name_text_surface = name_font.render(str(self.name), True, "white")
        name_text_rect = name_text_surface.get_rect(center=(self.name_block_rect.centerx, self.name_block_rect.centery))
        self.game.screen.blit(name_text_surface, name_text_rect)

        description_font = pg.font.Font(None, self.font_size_description)
        description_text_surface = description_font.render(str(self.description), True, "white")
        description_text_rect = description_text_surface.get_rect(
            center=(self.description_block_rect.centerx, self.description_block_rect.centery))
        self.game.screen.blit(description_text_surface, description_text_rect)

    def check_simbols(self):
        print(f'{self.name} - simb_count: {len(self.name)} - size: {self.font_size_name}')
        print(f'{self.description} - {len(self.description)} символов')

    def get_font_size_name(self):
        number_of_reductions = 4  # 4

        start_number_of_symbols = 7  # 7
        add_symbols = 2  # 2

        symbols_scale = 0.6  # 0.6
        add_scale = 0.005  # 0.005

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

    # def get_font_size_description(self):
    #     pass
