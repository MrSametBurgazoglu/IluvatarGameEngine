from game_engine_lib.scene import Scene
from game_engine_lib.enemy_test import Enemy
from game_engine_lib.equipment import Equipment
from scene_controller import SceneController
from game_engine_lib import UI
from pygame import image


class CardsPart(UI.UI):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 200
        self.pos_x = 200
        self.pos_y = 450
        self.state = True
        self.background_color = "transparent"
        self.set_font_size(20)

        self.mana_bar = UI.TextWidget()
        self.mana_bar.text = "0.0"
        self.mana_bar.pos_x = 500
        self.mana_bar.pos_y = 100
        self.mana_bar.font_color = (255, 255, 255)

        self.icon = UI.ImageWidget()
        self.icon.image = image.load("icon.png")
        self.icon.pos_y = 70
        self.icon.pos_x = 150
        self.icon.background = True

        self.character_stats = UI.LinerWidget()
        self.character_stats.pos_x = -50
        self.character_stats.pos_y = 0
        self.character_stats.width = 200
        self.character_stats.height = 150
        self.character_stats.child_space = 30

        self.health_text = UI.TextWidget()
        self.health_text.text = "Health:50"
        self.health_text.font_color = (255, 255, 255)
        self.character_stats.add_widgets(self.health_text)

        self.armor_text = UI.TextWidget()
        self.armor_text.text = "Armor:50"
        self.armor_text.font_color = (255, 255, 255)
        self.character_stats.add_widgets(self.armor_text)

        self.add_widget(self.mana_bar)
        self.add_widget(self.icon)
        self.add_widget(self.character_stats)


class CombatController(SceneController):
    def __init__(self):
        super().__init__()
        self.combat_ui = CardsPart()
        self.add_passage(None, self.combat_ui)
        self.script = self.update_system

    def update_system(self):
        for x in self.game_engine.current_scene.character_list:
            if x.mana < 10:
                x.mana += 0.01
        for x in self.game_engine.current_scene.character_list:
            if x.character_id == "#000":
                self.combat_ui.mana_bar.text = str(int(x.mana))


class CombatScene(Scene):
    def __init__(self):
        super().__init__()
        self.background_image = "background.png"

    def init(self):
        enemy_character = Enemy()
        sword = Equipment()
        sword.config("#020", "#002", (0.5, 0.1), (0.1, 0.3), "karakter/sword.png")
        enemy_character.add_equipment(sword)
        self.add_to_character_list(enemy_character)
        # self.character_list[0].switch_to_take_sword_animation()
        enemy_character.switch_to_take_sword_animation()


combat_scene = CombatScene()
combat_controller = CombatController()