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

        self.grid = None

        self.scene_content = [{'screens': []}, {'buttons': [{'': []}]}]
        self.all_scene_objects = []

        self.scene_soundtrack = None
        self.current_screen = None

        self.visible_content = []
        self.invisible_content = []
        self.active_content = []
        self.inactive_content = []

        self.scene_sounds = []
        self.scene_screens = []
        self.scene_buttons_and_actions = []
        self.scene_buttons = []

        self.declare_content()
        self.content_unpacking(self.scene_content)

    def declare_content(self):
        self.grid = Markup(self)

        self.scene_content = [{'sounds': []}, {'screens': []}, {'buttons': [{'': []}]}]
        self.all_scene_objects = []

        self.scene_soundtrack = None
        self.current_screen = None

        self.visible_content = []
        self.invisible_content = []
        self.active_content = []
        self.inactive_content = []

        self.screen_window = None

    def content_unpacking(self, content):
        # self.scene_sounds = []  # ?
        # self.scene_screens = []  # ?
        # self.scene_buttons_and_actions = []  # ?
        # self.scene_buttons = []  # ?

        for content_group in content:
            # {'screens': []}, {'buttons': [{'': []}]}
            for group_name, group_objects in content_group.items():
                # {'sounds': []}
                if group_name == 'sounds':
                    # {'sounds': []}
                    self.scene_sounds = group_objects
                    # []
                # {'screens': []}
                if group_name == 'screens':
                    # {'screens': []}
                    self.scene_screens = group_objects
                    # []
                if group_name == 'buttons':
                    # {'buttons': [{'': []}]}
                    self.scene_buttons_and_actions = group_objects
                    # [{'': []}]

        for button in self.scene_buttons_and_actions:
            # {'': []}
            for button_name, actions_list in button.items():
                # {'': []}
                self.scene_buttons.append(button_name)
                # ''

        for obj in self.scene_screens:
            self.all_scene_objects.append(obj)
        for obj in self.scene_buttons:
            self.all_scene_objects.append(obj)

        for obj in self.all_scene_objects:
            if obj not in self.visible_content:
                self.invisible_content.append(obj)

        for obj in self.all_scene_objects:
            if obj not in self.active_content:
                self.inactive_content.append(obj)

        print(f'\nscene_soundtrack - {self.scene_soundtrack}')
        print(f'current_screen - {self.current_screen}')
        print(f"scene_screens - {self.scene_screens}")
        print(f"scene_buttons - {self.scene_buttons}")
        print(f"all_scene_objects - {self.all_scene_objects}")
        print(f"visible_content - {self.visible_content}")
        print(f"invisible_content - {self.invisible_content}")
        print(f"active_content - {self.active_content}")
        print(f"inactive_content - {self.inactive_content}")

    # --- /// ---

    def content_handle_event(self, event):
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
            self.print_event(action_object)

        if action_name == 'switch_scene':
            self.game.switch_scene(action_object)

        if action_name == 'switch_visibility':
            self.switch_visibility(action_object, True)

        if action_name == 'make_visible':
            self.make_visible(action_object, True)

        if action_name == 'make_invisible':
            self.make_invisible(action_object, True)

        if action_name == 'switch_activity':
            self.switch_activity(action_object)

        # if action_name == 'change_screen_to':
        #     self.change_screen_to(action_object)

        if action_name == 'open_window':
            self.open_window(action_object)

        if action_name == 'play_sound':
            self.play_sound(action_object)

    # ---

    def print_event(self, action_object):
        print(str(action_object))

    def switch_visibility(self, action_object, activity_too=True):
        print(f'\naction_object - {action_object}')
        for obj in action_object:
            if obj in self.visible_content:
                self.visible_content.remove(obj)
                print(f'visible_content.remove({obj})')
                if activity_too is True:
                    if obj in self.active_content:
                        self.active_content.remove(obj)
                        print(f'active_content.remove({obj})')
                        self.inactive_content.append(obj)
                        print(f'inactive_content.append({obj})')
                if obj not in self.invisible_content:
                    self.invisible_content.append(obj)
                    print(f'invisible_content.append({obj})')
            elif obj in self.invisible_content:
                self.invisible_content.remove(obj)
                print(f'invisible_content.remove({obj})')
                if activity_too is True:
                    if obj not in self.active_content:
                        self.inactive_content.remove(obj)
                        print(f'inactive_content.remove({obj})')
                        self.active_content.append(obj)
                        print(f'active_content.append({obj})')
                if obj not in self.visible_content:
                    self.visible_content.append(obj)
                    print(f'visible_content.append({obj})')

        print(f'\nvisible_content - {self.visible_content}')
        print(f'invisible_content - {self.invisible_content}')
        print(f"active_content - {self.active_content}")
        print(f"inactive_content - {self.inactive_content}")

    def make_visible(self, action_object, activity_too=True):
        print(f'\naction_object - {action_object}')
        for obj in action_object:
            if obj in self.invisible_content:
                self.invisible_content.remove(obj)
                print(f'invisible_content.remove({obj})')
                if activity_too is True:
                    if obj not in self.active_content:
                        self.inactive_content.remove(obj)
                        print(f'inactive_content.remove({obj})')
                        self.active_content.append(obj)
                        print(f'active_content.append({obj})')
                if obj not in self.visible_content:
                    self.visible_content.append(obj)
                    print(f'visible_content.append({obj})')

        print(f'\nvisible_content - {self.visible_content}')
        print(f'invisible_content - {self.invisible_content}')
        print(f"active_content - {self.active_content}")
        print(f"inactive_content - {self.inactive_content}")

    def make_invisible(self, action_object, activity_too=True):
        print(f'\naction_object - {action_object}')
        for obj in action_object:
            if obj in self.visible_content:
                self.visible_content.remove(obj)
                print(f'visible_content.remove({obj})')
                if activity_too is True:
                    if obj in self.active_content:
                        self.active_content.remove(obj)
                        print(f'active_content.remove({obj})')
                        self.inactive_content.append(obj)
                        print(f'inactive_content.append({obj})')
                if obj not in self.invisible_content:
                    self.invisible_content.append(obj)
                    print(f'invisible_content.append({obj})')

        print(f'\nvisible_content - {self.visible_content}')
        print(f'invisible_content - {self.invisible_content}')
        print(f"active_content - {self.active_content}")
        print(f"inactive_content - {self.inactive_content}")

    def switch_activity(self, action_object):
        print(f'\naction_object - {action_object}')
        for obj in action_object:
            if obj in self.active_content:
                self.active_content.remove(obj)
                print(f'active_content.remove({obj})')
                if obj not in self.inactive_content:
                    self.inactive_content.append(obj)
                    print(f'inactive_content.append({obj})')
            elif obj in self.inactive_content:
                self.inactive_content.remove(obj)
                print(f'inactive_content.remove({obj})')
                if obj not in self.active_content:
                    self.active_content.append(obj)
                    print(f'active_content.append({obj})')

        print(f"active_content - {self.active_content}")
        print(f"inactive_content - {self.inactive_content}")

    # def change_screen_to(self, action_object, activity_too=True):  # Зачем?
    #     # print(f'current_screen - {self.current_screen}')
    #     if self.current_screen != action_object:
    #         if self.current_screen in self.visible_content:
    #             self.visible_content.remove(self.current_screen)
    #             # print(f'self.visible_content.remove({self.current_screen})')
    #             self.invisible_content.append(self.current_screen)
    #             # print(f'self.invisible_content.append({self.current_screen})')
    #             if activity_too is True:
    #                 if self.current_screen in self.active_content:
    #                     self.active_content.remove(self.current_screen)
    #                     # print(f'self.active_content.remove({self.current_screen})')
    #
    #         self.visible_content.insert(0, action_object)  # !
    #         self.current_screen = action_object
    #         if activity_too is True:
    #             if self.current_screen not in self.active_content:
    #                 self.active_content.append(self.current_screen)
    #                 # print(f'self.active_content.append({self.current_screen})')
    #
    #         # print(f'NEW current_screen - {self.current_screen}')

    # def open_window(self, action_object, activity_too=True):
    #     for obj in action_object:
    #         self.visible_content.append(obj)
    #         self.active_content.append(obj)
    #
    #     for obj in self.all_scene_objects:
    #         if obj not in action_object:
    #             if obj in self.active_content:
    #                 self.active_content.remove(obj)

    def play_sound(self, action_object):
        action_object.play_soundtrack()

    # ---

    # --- sound ---

    def play_soundtrack(self):  # 2
        if self.scene_soundtrack and self.soundtrack_playing is False:  # Трек есть и он НЕ играет?
            # print(f'2. Трек {self.scene_soundtrack} есть и он НЕ играет')  # Трек есть и он НЕ играет
            pg.mixer.music.load(self.scene_soundtrack)
            pg.mixer.music.play(-1)
            self.soundtrack_playing = True
            # print(f'3. Теперь трек {self.scene_soundtrack} играет')
        # else:
        #     print(f'5. Либо нет трека {self.scene_soundtrack}, либо он уже играет ')  # Либо нет трека, либо он уже играет

    def check_soundtrack_playing(self):  # 1
        if pg.mixer.music.get_busy() is False:  # Трек не играет?
            # print(f'1. Трек {self.scene_soundtrack} не играет')
            self.soundtrack_playing = False  # Трек не играет
        # else:
        #     print(f'4. Трек {self.scene_soundtrack} играет')  # Трек играет

    def stop_soundtrack(self):
        pg.mixer.music.stop()
        self.soundtrack_playing = False  # Теперь трек не играет
        # print(f'6. Теперь трек {self.scene_soundtrack} не играет')

    # --- sound ---

    def check_window_close(self, event):
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     if not self.screen_window.image_rect.collidepoint(event.pos):
        #         self.visible_content.remove(self.screen_window)
        pass

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            self.content_handle_event(event)
            self.check_userevent(event)
            self.check_window_close(event)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption("Vld Game")

        for obj in self.active_content:
            obj.check_hover(pg.mouse.get_pos())

    def draw(self):
        self.screen.fill("black")
        self.grid.draw()

        for obj in self.visible_content:
            obj.draw()

    def run(self):
        self.check_soundtrack_playing()
        self.play_soundtrack()
        self.check_events()
        self.update()
        self.draw()
