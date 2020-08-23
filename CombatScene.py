from game_engine_lib.scene import Scene
from game_engine_lib.enemy_taret import Enemy
from game_engine_lib.equipment import Equipment
from scene_controller import SceneController
from game_engine_lib import UI
from pygame import image
from random import choice


class LoseUI(UI.UI):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 200
        self.pos_x = 300
        self.pos_y = 250
        self.state = True
        self.background_color = "transparent"
        self.set_font_size(100)
        self.message = UI.TextWidget()
        self.message.text = "CBG Sunar"
        self.message.pos_x = 0
        self.message.pos_y = 0
        self.message.font_color = (255, 255, 255)
        self.add_widget(self.message)
        self.state = True
        self.make_pause = True


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
        self.lose_ui = LoseUI()
        self.add_passage(None, self.combat_ui)
        self.script = self.update_system
        self.ym = 0

    def update_system(self):
        for x in self.game_engine.current_scene.character_list:
            if x.mana < 10:
                x.mana += 0.01
            if x.id == "#000":
                self.combat_ui.mana_bar.text = str(int(x.mana))
                self.combat_ui.health_text.text = "Health: {}".format(x.health)
                if x.health <= 0:
                    self.add_passage(None, self.lose_ui)
                    self.game_engine.pause = True
        if self.ym >= 10:
            liste = self.game_engine.current_scene.character_list[1:]
            c = choice(liste)
            c.fire(self.game_engine)
        else:
            self.ym += 0.1


class CombatScene(Scene):
    def __init__(self):
        super().__init__()
        self.background_image = "background.png"

    def init(self):
        enemy_character = Enemy()
        enemy_character2 = Enemy()
        enemy_character2.id = "#003"
        enemy_character2.pos_x = 600
        enemy_character2.pos_y = 200
        enemy_character2.mana = 5
        enemy_character3 = Enemy()
        enemy_character3.id = "#004"
        enemy_character3.pos_x = 200
        enemy_character3.pos_y = 200
        enemy_character3.mana = 0
        enemy_character4 = Enemy()
        enemy_character4.id = "#005"
        enemy_character4.pos_x = 300
        enemy_character4.pos_y = 300
        enemy_character4.mana = 0
        enemy_character5 = Enemy()
        enemy_character5.id = "#006"
        enemy_character5.pos_x = 400
        enemy_character5.pos_y = 400
        enemy_character5.mana = 0
        #sword = Equipment()
        #sword.config("#020", "#002", (0.5, 0.1), (0.1, 0.3), "karakter/sword.png")
        #enemy_character.add_equipment(sword)
        self.add_to_character_list(enemy_character)
        self.add_to_character_list(enemy_character2)
        self.add_to_character_list(enemy_character3)
        # self.character_list[0].switch_to_take_sword_animation()
        #enemy_character.switch_to_take_sword_animation()


combat_scene = CombatScene()
combat_controller = CombatController()