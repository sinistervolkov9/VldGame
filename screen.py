import pygame as pg
from settings import RES, SCREEN_POS


class Screen:
    def __init__(self,
                 game,
                 pos=None, size=None,
                 image=None,
                 background_sound=False, sound_click=False
                 ):
        self.game = game

        self.pos = SCREEN_POS["tl"] if pos is None else pos
        self.size = RES if size is None else size

        self.image = 'resources/backgrounds/background.png' if image is None else image

        # self.background_sound = 'resources/sounds/background.wav' if background_sound is None else background_sound
        # self.sound_click = 'resources/sounds/scroll_click_1.wav'

        if background_sound is True:
            self.background_sound = 'resources/sounds/background.wav'
        elif background_sound is False:
            self.background_sound = None
        else:
            self.background_sound = background_sound

        if sound_click is True:
            self.sound_click = 'resources/sounds/scroll_click_1.wav'
        elif sound_click is False:
            self.sound_click = None
        else:
            self.sound_click = sound_click

        # ---
        self.is_hovered = False
        # self.over = False
        # ---

        self.is_hovered = False

        self.load_images()
        self.load_sounds()
        self.get_size_pos()
        self.update()  # ?

    def load_images(self):
        self.image = pg.image.load(self.image)

    def load_sounds(self):
        # self.background_sound = pg.mixer.music.load(self.background_sound)
        # self.background_sound = pg.mixer.Sound(self.sound)
        if self.sound_click:
            self.sound_click = pg.mixer.Sound(self.sound_click)

    def update(self):
        self.image = pg.transform.scale(self.image, self.size)
        self.image_rect = self.image.get_rect(topleft=self.pos)

    def get_size_pos(self):
        pass

    def draw(self):
        self.game.screen.blit(self.image, self.image_rect.topleft)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.image_rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        # pg.mixer.music.play(-1)
        # self.background_sound.play()
        if self.is_hovered and event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if self.sound_click:
                self.sound_click.play()
