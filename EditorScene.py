from game_engine_lib.scene import Scene
from scene_controller import SceneController
from game_engine_lib import UI
from pygame import image


class EditorUI(UI.UI):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 200
        self.pos_x = 200
        self.pos_y = 450
        self.state = True
        self.background_color = "transparent"
        self.set_font_size(20)


class EditorController(SceneController):
    def __init__(self):
        super().__init__()
        self.editor_ui = EditorUI()
        self.add_passage(None, self.editor_ui)


class EditorScene(Scene):
    def __init__(self):
        super().__init__()
        self.background_image = "background.png"

    def init(self):
        pass


editor_scene = EditorScene()
editor_controller = EditorController()