from game_engine_lib import player as player_m, game, scene_controller as scene_controller_m
from game_engine_lib import scene as scene_m
from game_engine_lib import light as light_m
from game_engine_lib import equipment as equipment_m
from scenes.CombatScene import combat_scene, combat_controller
from game_engine_lib import UI
from pygame import K_ESCAPE
import sys

class Menu(UI.UI):
    def __init__(self):
        super().__init__()
        self.width = 200
        self.height = 200
        self.pos_x = 100
        self.pos_y = 100
        self.button1 = UI.TextWidget()
        self.button1.text = "Hello World"
        self.add_widget(self.button1)
        self.new_entry = UI.EntryWidget()
        self.new_entry.pos_x = 100
        self.new_entry.pos_y = 100
        self.new_entry.height = 20
        self.new_entry.width = 50
        self.add_widget(self.new_entry)
        self.make_pause = True


class Giris(UI.UI):
    def __init__(self):
        super().__init__()
        self.width = 200
        self.height = 200
        self.pos_x = 400
        self.pos_y = 200
        self.background_color = "transparent"
        self.begin = UI.ButtonWidget()
        self.begin.text = "Oyuna Başla"
        self.begin.font_color = (255, 255, 255)
        self.begin.width = 170
        self.begin.height = 45
        self.settings = UI.ButtonWidget()
        self.settings.text = "Ayarlar"
        self.settings.font_color = (255, 255, 255)
        self.settings.pos_y = 80
        self.settings.pos_x = 30
        self.settings.width = 110
        self.settings.height = 45
        self.exit = UI.ButtonWidget()
        self.exit.text = "Çıkış"
        self.exit.font_color = (255, 255, 255)
        self.exit.pos_y = 160
        self.exit.pos_x = 50
        self.exit.width = 70
        self.exit.height = 45
        self.deneme_button = UI.ButtonWidget()
        self.deneme_button.text = "HEADSHOT"
        self.deneme_button.pos_x = 40
        self.deneme_button.pos_y = -200
        self.deneme_button.font_color = (255, 0, 0)
        self.add_widget(self.begin)
        self.add_widget(self.settings)
        self.add_widget(self.exit)
        self.add_widget(self.deneme_button)
        self.make_pause = True


class Ayarlar(UI.UI):
    def __init__(self):
        super().__init__()
        self.width = 200
        self.height = 200
        self.pos_x = 300
        self.pos_y = 200
        self.background_color = "transparent"
        self.begin = UI.ButtonWidget()
        self.begin.text = "Geri Dön"
        self.begin.font_color = (255, 255, 255)
        self.begin.width = 120
        self.begin.height = 45
        self.begin.pos_x = 40
        self.linewidget = UI.LineWidget()
        self.linewidget.pos_y = 80
        self.linewidget.pos_x = 20
        self.linewidget.width = 200
        self.azalt = UI.ButtonWidget()
        self.azalt.text = "<"
        self.azalt.font_color = (255, 255, 255)
        self.azalt.height = 40
        self.azalt.width = 15
        self.azalt.pos_y = 80
        self.azalt.set_clicked(self.fonk1, -10)
        self.arttır = UI.ButtonWidget()
        self.arttır.text = ">"
        self.arttır.font_color = (255, 255, 255)
        self.arttır.height = 40
        self.arttır.width = 15
        self.arttır.pos_y = 80
        self.arttır.pos_x = 230
        self.arttır.set_clicked(self.fonk1, 10)
        self.add_widget(self.begin)
        self.add_widget(self.linewidget)
        self.add_widget(self.azalt)
        self.add_widget(self.arttır)

    def fonk1(self, arg):
        self.linewidget.bold_line += arg[0]


class GameTest(object):
    def __init__(self):
        self.game_engine = game.GameEngine()
        self.game_engine.set_window_name("WORK IN PROGRESS")
        self.game_engine.set_fps(60)
        self.game_engine.set_win_wh(1000, 500)
        self.game_engine.init_engine()
        self.scene0 = scene_m.Scene()
        self.scene0.background_image = "game/bg.jpg"
        self.scene_controller0 = scene_controller_m.SceneController()
        self.scene_controller0.game_engine = self.game_engine
        self.giris_ui = Giris()
        self.giris_ui.state = True
        self.giris_ui.widgets[0].set_clicked(self.fonk2, False)
        self.giris_ui.widgets[1].set_clicked(self.fonk1, False)
        self.giris_ui.widgets[2].set_clicked(self.game_engine.quit, None)
        self.scene_controller0.add_passage(None, self.giris_ui)
        self.ayarlar_ui = Ayarlar()
        self.ayarlar_ui.state = False
        self.ayarlar_ui.widgets[0].set_clicked(self.fonk1, True)
        self.scene_controller0.add_passage(None, self.ayarlar_ui)
        self.game_engine.set_scene_controller(self.scene_controller0)
        self.scene1 = scene_m.Scene()
        self.scene1.background_image = "game/bg.jpg"
        self.sword = equipment_m.Equipment()
        self.sword.config("#020", "#002", (0.5, 0.1), (0.1, 0.3), "game/karakter/sword.png")
        self.player = player_m.Player()
        self.player.add_equipment(self.sword)
        self.scene1.add_to_character_list(self.player)
        self.scene_controller = scene_controller_m.SceneController()
        self.scene_controller.game_engine = self.game_engine
        self.menu = Menu()
        self.scene_controller.add_passage(K_ESCAPE, self.menu)
        self.scene_light = light_m.Light()
        self.scene1.add_light_to_scene(self.scene_light)
        combat_scene.add_to_character_list(self.player)
        combat_controller.game_engine = self.game_engine
        self.game_engine.init_scene(self.scene0)
        self.game_engine.start_engine()

    def fonk1(self, args):
        self.giris_ui.state = args[0]
        self.ayarlar_ui.state = not args[0]

    def fonk2(self, args):
        self.game_engine.init_scene(combat_scene)
        combat_scene.init()
        self.game_engine.set_scene_controller(combat_controller)


if __name__ == "__main__":
    print(sys.path)
    game_test = GameTest()
