from scene_manager import SceneMainMenu, Scene2


class Game:
    def __init__(self):
        self.current_scene = None
        # print(f'self.current_scene - {self.current_scene}')

        self.create_scenes()

    def create_scenes(self):  # А зачем этот матод? Можно все перевести в инит
        self.scene_1 = SceneMainMenu(self)
        self.scene_2 = Scene2(self)

        self.current_scene = self.scene_2

    def switch_scene(self):
        self.current_scene = self.scene_1

    def run_game(self):
        while True:
            self.current_scene.run()

    def call_button_pos(self):
        print(self.scene_1.button_1.pos)


if __name__ == "__main__":
    game = Game()
    game.run_game()
