import sys
import scene_manager_2 as sm
import pygame as pg
from settings import *

pg.init()

screen_surface = pg.display.set_mode((WIDTH, HEIGHT))

scenes = [
    {"scene_0":
         [
             {"screen": sm.screen_0},
             {"buttons": [{sm.button_1: "scene_1"}, {sm.button_2: "scene_2"}, {sm.button_3: "scene_3"}]},
             {"events": []},
             {"esc_screen": "scene_3"},
             {"items": []}
         ]
    },
    {"scene_1":
         [
             {"screen": sm.screen_1},
             {"buttons": [{sm.button_1_1: "scene_4"}]},
             {"events": [sm.event_1]},
             {"esc_screen": "scene_4"},
             {"items": []}
         ]
    },
    {"scene_2":
         [
             {"screen": sm.screen_2},
             {"buttons": [{sm.button_2_1: None}, {sm.button_2_2: None}, {sm.button_2_3: None}]},
             {"events": []},
             {"esc_screen": None},
             {"items": []}
         ]
    },
    {"scene_3":
         [
             {"screen": sm.screen_3},
             {"buttons": [{sm.button_3_1: None}, {sm.button_3_2: "scene_0"}]},
             {"events": []},
             {"esc_screen": "scene_0"},
             {"items": []}
         ]
    },
    {"scene_4":
         [
             {"screen": sm.screen_4},  # 4. item in scene_items_list {k: v}
             {"buttons": [{sm.button_4_1: "scene_1"}, {sm.button_4_2: "scene_0"}]},
             {"events": []},
             {"esc_screen": "scene_1"},
             {"items": []}
         ]
    }
]

current_scene = "scene_0"
scenes_history = []

current_screen = []
esc_screen = []
buttons_swh = []
current_buttons = []
current_events = []
current_items = []

for scene in scenes:
    for scene_num, scene_items_list in scene.items():
        if scene_num == current_scene:
            for item in scene_items_list:
                for k, v in item.items():
                    if k == "screen":
                        current_screen.append(v)
                    if k == "buttons":
                        buttons_swh = v
                    if k == "events":
                        current_events = v
                    if k == "esc_screen":
                        if v is None:
                            esc_screen.append(scenes_history[-1])
                        else:
                            esc_screen.append(v)
                    if k == "items":
                        current_items = v

# Подчистка истории скринов ------------------------------------
# if (len(scenes_history)) > 1:
#     print("---len(scenes_history) > 1")
#     for scene_in_history in scenes_history:
#         print("---for scene_in_history in scenes_history")
#         if scene_in_history == current_scene:
#             print("---scene_in_history == scenes_history[-1]")
#             scenes_history.remove(scene_in_history)
# --------------------------------------------------------------
scenes_history.append(current_scene)

for button in buttons_swh:
    for but, scr in button.items():
        current_buttons.append(but)

print(f"\ncurrent_scene - {current_scene}")
print(f"scenes_history - {scenes_history}")

print(f"current_screen - {current_screen}")
print(f"esc_screen - {esc_screen}")
print(f"buttons_swh - {buttons_swh}")
print(f"current_buttons - {current_buttons}")
print(f"current_events - {current_events}")
print(f"current_items - {current_items}")

# -----------------------------------------------

running = True
while running:
    for screennn in current_screen:
        screennn.update(screen_surface)
        screennn.draw(screen_surface)
        # screennn.handle_event()

    # -----------------------------------------------

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                for scn in esc_screen:
                    current_scene = scn
                    current_screen = []
                    esc_screen = []
                    buttons_swh = []
                    current_buttons = []

                    for scene in scenes:
                        for scene_num, scene_items_list in scene.items():
                            if scene_num == current_scene:
                                for item in scene_items_list:
                                    for k, v in item.items():
                                        if k == "screen":
                                            current_screen.append(v)
                                        if k == "buttons":
                                            buttons_swh = v
                                        if k == "events":
                                            current_events = v
                                        if k == "esc_screen":
                                            if v is None:
                                                esc_screen.append(scenes_history[-1])
                                            else:
                                                esc_screen.append(v)
                                        if k == "items":
                                            current_items = v

                    # Подчистка истории скринов ------------------------------------
                    # if (len(scenes_history)) > 1:
                    #     print("---len(scenes_history) > 1")
                    #     for scene_in_history in scenes_history:
                    #         print("---for scene_in_history in scenes_history")
                    #         if scene_in_history == current_scene:
                    #             print("---scene_in_history == scenes_history[-1]")
                    #             scenes_history.remove(scene_in_history)
                    # --------------------------------------------------------------
                    scenes_history.append(current_scene)

                    for button in buttons_swh:
                        for but, scr in button.items():
                            current_buttons.append(but)

                    print(f"\ncurrent_scene - {current_scene}")
                    print(f"scenes_history - {scenes_history}")
                    print(f"esc_screen - {esc_screen}")
                    print(f"current_screen - {current_screen}")
                    print(f"buttons_swh - {buttons_swh}")
                    print(f"current_buttons - {current_buttons}")
                    print(f"current_events - {current_events}")
                    print(f"current_items - {current_items}")

        if event.type == pg.USEREVENT and event.button in current_buttons:
            for user_button in current_buttons:
                if event.type == pg.USEREVENT and event.button == user_button:
                    for button in buttons_swh:
                        for but, scn in button.items():
                            if user_button == but:
                                if scn is None:
                                    pg.quit()
                                    sys.exit()
                                else:
                                    current_scene = scn
                                    current_screen = []
                                    esc_screen = []
                                    buttons_swh = []
                                    current_buttons = []

                                    for scene in scenes:
                                        for scene_num, scene_items_list in scene.items():
                                            if scene_num == current_scene:
                                                for item in scene_items_list:
                                                    for k, v in item.items():
                                                        if k == "screen":
                                                            current_screen.append(v)
                                                        if k == "buttons":
                                                            buttons_swh = v
                                                        if k == "events":
                                                            current_events = v
                                                        if k == "esc_screen":
                                                            if v is None:
                                                                esc_screen.append(scenes_history[-1])
                                                            else:
                                                                esc_screen.append(v)
                                                        if k == "items":
                                                            current_items = v

                                    # Подчистка истории скринов ------------------------------------
                                    # if (len(scenes_history)) > 1:
                                    #     print("---len(scenes_history) > 1")
                                    #     for scene_in_history in scenes_history:
                                    #         print("---for scene_in_history in scenes_history")
                                    #         if scene_in_history == current_scene:
                                    #             print("---scene_in_history == scenes_history[-1]")
                                    #             scenes_history.remove(scene_in_history)
                                    # --------------------------------------------------------------
                                    scenes_history.append(current_scene)

                                    for button in buttons_swh:
                                        for but, scr in button.items():
                                            current_buttons.append(but)

                                    print(f"\ncurrent_scene - {current_scene}")
                                    print(f"scenes_history - {scenes_history}")
                                    print(f"esc_screen - {esc_screen}")
                                    print(f"current_screen - {current_screen}")
                                    print(f"buttons_swh - {buttons_swh}")
                                    print(f"current_buttons - {current_buttons}")
                                    print(f"current_events - {current_events}")
                                    print(f"current_items - {current_items}")

        for button in current_buttons:
            button.handle_event(event)

    for button in current_buttons:
        button.check_hover(pg.mouse.get_pos())
        button.draw(screen_surface)

    pg.display.flip()

# -----------------------------------------------





























