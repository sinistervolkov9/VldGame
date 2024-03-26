import sys
import pygame as pg
from settings import FPS, RES
from markup import Markup


class Scene:
    def __init__(self, game):
        self.game = game
        pg.init()
        self.screen = pg.display.set_mode(RES)
        # self.screen = pg.display.set_mode(RES, pg.FULLSCREEN)
        self.clock = pg.time.Clock()

        self.scene_content = [{'screens': []}, {'buttons': [{'': []}]}]
        self.all_scene_objects = []
        self.visible_content = []
        self.invisible_content = []
        # self.active_content = self.visible_content
        self.active_content = []

        self.scene_screens = []
        self.scene_buttons_and_actions = []
        self.scene_buttons = []

        self.declare_content()
        self.content_unpacking()

        print(f'1. self.active_content - {self.active_content}')
        print(f'1. self.visible_content - {self.visible_content}')

    def declare_content(self):
        self.grid = Markup(self)

        self.scene_content = [{'screens': []}, {'buttons': [{'': []}]}]
        self.visible_content = []
        self.invisible_content = []
        # self.active_content = self.visible_content
        self.active_content = []

    def content_unpacking(self):
        self.scene_screens = []  # ?
        self.scene_buttons_and_actions = []  # ?
        self.scene_buttons = []  # ?

        for content_group in self.scene_content:
            for group_name, group_objects in content_group.items():
                if group_name == 'screens':
                    self.scene_screens = group_objects
                if group_name == 'buttons':
                    self.scene_buttons_and_actions = group_objects

        for button in self.scene_buttons_and_actions:
            for button_name, actions_list in button.items():
                self.scene_buttons.append(button_name)

        # print(f"\nscene_screens - {self.scene_screens}")
        # print(f"scene_buttons - {self.scene_buttons}")

        # ---

        for obj in self.scene_screens:
            self.all_scene_objects.append(obj)
        for obj in self.scene_buttons:
            self.all_scene_objects.append(obj)

        # print(f"all_scene_objects - {self.all_scene_objects}")

    # --- /// ---

    def content_handle_event(self, event):
        # for content_object in self.visible_content:
        for content_object in self.active_content:
            content_object.handle_event(event)

    def check_userevent(self, event):
        if event.type == pg.USEREVENT and event.button in self.all_scene_objects:
            # print(f"\nevent.button in self.all_scene_objects")
            if event.button in self.visible_content:
                # print(f"\nevent.button - {event.button}")
                for clicked_button in self.visible_content:
                    # print(f"clicked_button - {clicked_button}")
                    if event.button == clicked_button:
                        # print(f"event.button == clicked_button")
                        for button in self.scene_buttons_and_actions:
                            # print(f"button - {button}")
                            for button_name, actions_list in button.items():
                                # print(f"button_name - {button_name}")
                                # print(f"actions_list - {actions_list}")
                                if clicked_button == button_name:
                                    # print(f"clicked_button == button_name")
                                    for action in actions_list:
                                        # print(f"action - {action}")
                                        for action_name, action_object in action.items():
                                            self.userevent_applying(action_name, action_object)

    def userevent_applying(self, action_name, action_object):
        if action_name == 'print_event':
            action_object.print_text()

        if action_name == 'switch_scene':
            self.game.switch_scene(action_object)

        if action_name == 'switch_visibility':
            for obj in action_object:
                if obj in self.visible_content:
                    self.visible_content.remove(obj)
                    if obj not in self.invisible_content:
                        self.invisible_content.append(obj)
                elif obj in self.invisible_content:
                    self.invisible_content.remove(obj)
                    if obj not in self.visible_content:
                        self.visible_content.append(obj)

        if action_name == 'make_visible':
            for obj in action_object:
                if obj not in self.visible_content:
                    self.visible_content.append(obj)
                    if obj in self.invisible_content:
                        self.invisible_content.remove(obj)

        if action_name == 'make_invisible':
            for obj in action_object:
                if obj not in self.invisible_content:
                    self.invisible_content.append(obj)
                    if obj in self.visible_content:
                        self.visible_content.remove(obj)

        if action_name == 'switch_activity':
            for obj in action_object:
                if obj in self.active_content:
                    self.active_content.remove(obj)
                elif obj in self.all_scene_objects and obj not in self.active_content:
                    self.active_content.append(obj)

    # --- /// ---

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            self.content_handle_event(event)
            self.check_userevent(event)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption("Vld Game")

        for obj in self.visible_content:
            obj.check_hover(pg.mouse.get_pos())

    def draw(self):
        self.screen.fill("black")
        self.grid.draw()

        for obj in self.visible_content:
            obj.draw()

    def run(self):
        self.check_events()
        self.update()
        self.draw()
