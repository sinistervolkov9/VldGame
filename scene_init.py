import sys
import scene_manager as sm
import pygame as pg

class Scene:
    #screen_surface = pg.display.set_mode((WIDTH, HEIGHT))

    def __init__(self, current_scene="scene_0"):
        self.current_scene = current_scene
        self.scenes_history = []
        self.current_events = []
        self.current_items = []

        self.esc_screen = []
        self.current_screen = []
        self.buttons_swh = []
        self.current_buttons = []

        self.unpacking()

    def screen_updater(self, screen_surface):
        for screennn in self.current_screen:
            screennn.update(screen_surface)
            screennn.draw(screen_surface)
            # screennn.handle_event()

    def event_updater(self, event):
        for eve in self.current_events:
            eve.moving(event)

    def event_keydown(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                for scn in self.esc_screen:
                    self.current_scene = scn
                self.unpacking()

    def user_event(self, event):
        if event.type == pg.USEREVENT and event.button in self.current_buttons:
            for user_button in self.current_buttons:
                if event.type == pg.USEREVENT and event.button == user_button:
                    for button in self.buttons_swh:
                        for but, scn in button.items():
                            if user_button == but:
                                if scn is None:
                                    pg.quit()
                                    sys.exit()
                                else:
                                    self.current_scene = scn
                                    self.unpacking()

    def unpacking(self):
        self.esc_screen = []
        self.current_screen = []
        self.buttons_swh = []
        self.current_buttons = []
        for scene in sm.scenes:
            for scene_num, scene_items_list in scene.items():
                if scene_num == self.current_scene:
                    for item in scene_items_list:
                        for k, v in item.items():
                            if k == "screen":
                                self.current_screen.append(v)
                            if k == "buttons":
                                self.buttons_swh = v
                            if k == "events":
                                self.current_events = v
                            if k == "esc_screen":
                                if v is None:
                                    self.esc_screen.append(self.scenes_history[-1])
                                else:
                                    self.esc_screen.append(v)
                            if k == "items":
                                self.current_items = v

        # Подчистка истории скринов ------------------------------------
        # if (len(self.scenes_history)) > 1:
        #     print("---len(scenes_history) > 1")
        #     for scene_in_history in self.scenes_history:
        #         print("---for scene_in_history in scenes_history")
        #         if scene_in_history == self.scenes_history[-1]:
        #             print("---scene_in_history == scenes_history[-1]")
        #             self.scenes_history.remove(scene_in_history)
        # --------------------------------------------------------------

        self.scenes_history.append(self.current_scene)

        for button in self.buttons_swh:
            for but, scr in button.items():
                self.current_buttons.append(but)

        print(f"\ncurrent_scene - {self.current_scene}")
        print(f"scenes_history - {self.scenes_history}")
        print(f"current_screen - {self.current_screen}")
        print(f"esc_screen - {self.esc_screen}")
        print(f"buttons_swh - {self.buttons_swh}")
        print(f"current_buttons - {self.current_buttons}")
        print(f"current_events - {self.current_events}")
        print(f"current_items - {self.current_items}")

    def button_handle_event(self, event):
        for button in self.current_buttons:
            button.handle_event(event)

    def button_updater(self, screen_surface):
        for button in self.current_buttons:
            button.check_hover(pg.mouse.get_pos())
            button.draw(screen_surface)
