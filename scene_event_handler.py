import sys
import scene_manager as sm
import pygame as pg


class Scene:
    def __init__(self, current_scene="scene_0"):
        self.current_scene = current_scene
        self.scenes_history = []

        self.esc_events = []
        self.current_screen = []
        self.buttons_swh = []
        self.current_buttons = []

        self.unpacking()

    def screen_draw(self, screen_surface):
        for screennn in self.current_screen:
            screennn.draw(screen_surface)

    def esc_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                for eve in self.esc_events:
                    for key, value in eve.items():
                        if key == "bring_to_basic":
                            for btn in value:
                                btn.bring_to_basic_state()
                        if key == "change_scene":
                            if value is None:
                                self.current_scene = self.scenes_history[-2]
                                self.unpacking()
                            else:
                                self.current_scene = value
                                self.unpacking()
                        # elif key == "switch_visibility":  # Если есть скрипт change_display
                        #     for btn in value:  # Перебираем все кнопки в списке
                        #         btn.switch_visibility()  # Вызываем метод toggle_display для каждой кнопки
                        # self.current_scene = scn
                # self.unpacking()

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
        self.current_screen = []
        self.current_buttons = []
        self.button_objts = []
        self.esc_events = []

        for scene in sm.scenes:
            for scene_num, scene_items_list in scene.items():
                if scene_num == self.current_scene:
                    for item in scene_items_list:
                        for k, v in item.items():
                            if k == "screen":
                                for i in v:
                                    self.current_screen.append(i)
                            if k == "buttons":
                                self.current_buttons = v
                            if k == "esc_event":
                                if v is None:
                                    pass
                                else:
                                    self.esc_events = v

        self.scenes_history.append(self.current_scene)

        # Подчистка истории скринов
        if (len(self.scenes_history)) > 1:
            for scene_in_history in self.scenes_history[:-1]:
                if scene_in_history == self.scenes_history[-1]:
                    self.scenes_history.remove(scene_in_history)
                    break

        for button in self.current_buttons:
            # print(button)
            for buttons_name, buttons_actions_list in button.items():
                self.button_objts.append(buttons_name)

        print(f"\ncurrent_scene - {self.current_scene}")
        print(f"scenes_history - {self.scenes_history}")
        print(f"current_screen - {self.current_screen}")
        print(f"esc_event - {self.esc_events}")
        print(f"current_buttons - {self.current_buttons}")

    def button_handle_event(self, event):
        for button in self.button_objts:
            button.handle_event(event)

    def button_update(self, screen_surface):
        for button in self.button_objts:
            button.check_hover(pg.mouse.get_pos())

            button.draw(screen_surface)

    def button_click_event(self, event):
        if event.type == pg.USEREVENT and event.button in self.button_objts:
            for user_button in self.button_objts:
                if event.type == pg.USEREVENT and event.button == user_button:
                    for button in self.current_buttons:
                        for buttons_name, buttons_actions_list in button.items():
                            if user_button == buttons_name:
                                for eventtt in buttons_actions_list:
                                    for k, v in eventtt.items():
                                        self.check_button_events(k, v)

    # def click_event(self, event):
    #     if event.type == pg.MOUSEBUTTONUP:
    #         print("click")


    def check_button_events(self, key, value):  # Проверка событий кнопки
        if key == "bring_to_basic":
            for btn in value:
                btn.bring_to_basic_state()
        if key == "change_scene":
            if value == "EXIT":
                pg.quit()
                sys.exit()
            elif value is None:
                self.current_scene = self.scenes_history[-2]
                self.unpacking()
            else:
                self.current_scene = value
                self.unpacking()
        if key == "print_text":
            value.print_text()
        if key == "switch_visibility":
            for btn in value:
                btn.switch_visibility()
        if key == "switch_activity":
            for btn in value:
                btn.switch_activity()
