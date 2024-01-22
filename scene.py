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

trigger_0 = True
trigger_1 = False
trigger_2 = False

scenes = [
    {"scene_0":
        [
            {"screen": screen},
            {"buttons": [
                {button_0: [
                    {"trigger for display": trigger_0},  # Тот самый триггер, при Трушности которого кнопка будет отображаться. Не, триггер должен даваться кнопке или чему-либо при создании экземпляра класса.
                    {"change scene": "scene_1"},
                    {"print_some": print_event_0},
                    {"change trigger": [trigger_1, trigger_2]}  # Лучше списком,потому что одна кнопка может менять несколько триггеров. Например, отобраза кнопку_2, и перестань отображать саму меня
                ]},
                {button_1: [
                    {"change scene": "scene_2"},
                    {"print_some": print_event_1}
                ]}
            ]},
            {events: [event_1, event_2]},
            {items: [item_1, item_2]},
            {triggers: []}
        ]
    },
]

# ----------------------------------------------------------------------------------------

display_trigger = {
    "buttons":
        [
            {button_1: True},
            {button_2 : False},
            {button_3 : True},
            {button_4 : False},
            {button_5 : False}
        ]
}

# Кнопка : Триггер для отображения
