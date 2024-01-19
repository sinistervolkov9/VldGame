scenes = [
    {scene_1:
        [
            {screen: screen},
            {buttons: [{button_1: scene_2}, {button_2: scene_3}]},
            {events: [event_1, event_2]},
            {items: [item_1, item_2]}
        ]
    }
]

scenes_history = []
current_scene = scene_1

# ----------------------------------------------------------------------------------------

scenes = [
    {"scene_0":
        [
            {"screen": screen},
            {"buttons": [
                {button_0: [
                    {"change scene": "scene_1"},
                    {"print_some": print_event_0}
                ]},
                {button_1: [
                    {"change scene": "scene_2"},
                    {"print_some": print_event_1}
                ]}
            ]},
            {events: [event_1, event_2]},
            {items: [item_1, item_2]}
        ]
    },
]
