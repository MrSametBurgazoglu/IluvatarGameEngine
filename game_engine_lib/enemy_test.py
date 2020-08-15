from .npc import NPC
from .animator import Animator
from .animator import Switcher
from .skeleton import Skeleton
from game_engine_lib import physic


class Enemy(NPC):
    def __init__(self):
        super().__init__()
        self.pos_x = 750
        self.pos_y = 350
        self.healt = 1000
        self.character_id = "#001"
        self.character_name = "ENEMY"
        self.idle_animation = Animator("player_idle.animation", True, False)
        self.idle_switcher = None
        self.walking_animation = Animator("player_walking.animation", True, False)
        self.walking_switcher = None
        self.take_sword_animation = Animator("player_take_sword.animation", True, True)
        self.take_sword_switcher = None
        self.take_sword_animation.scripts.append([90, self.take_hand_sword])
        self.take_sword_animation.scripts.append([179, lambda: self.remove_from_animator_list(self.take_sword_switcher)])
        self.stabbing_animation = Animator("player_stabbing.animation", True, True)
        self.stabbing_switcher = None
        self.stabbing_animation.scripts.append([88, lambda: self.remove_from_animator_list(self.stabbing_switcher)])
        self.get_stabbing_animation = Animator("player_get_stabbing.animation", True, True)
        self.get_stabbing_switcher = None  # TODO WRITE ANIMATOR CONTROLLER FOR NPC
        self.tumble_animation = Animator("player_tumble.animation", True, True)
        self.swing_sword_animation = Animator("player_swing_sword.animation", True, True)
        self.skeleton = Skeleton("player.skeleton")
        self.add_character_parts("#004", "karakter/l_arm.png")
        self.add_character_parts("#006", "karakter/l_foot.png")
        self.add_character_parts("#008", "karakter/l_knee.png")
        self.add_character_parts("#010", "karakter/l_leg.png")
        self.add_character_parts("#012", "karakter/l_hand.png")
        self.add_character_parts("#002", "karakter/body.png")
        self.add_character_parts("#001", "karakter/head.png")
        self.add_character_parts("#003", "karakter/r_arm.png")
        self.add_character_parts("#007", "karakter/r_knee.png")
        self.add_character_parts("#009", "karakter/r_leg.png")
        self.add_character_parts("#005", "karakter/r_foot.png")
        self.add_character_parts("#011", "karakter/r_hand.png")
        for x in self.character_parts:
            self.last_data.append([x.id, x.rotate])
        self.switch_to_idle_animation()
        self.connect_to_a_character = True
        self.connected_character = "#000"
        self.mana = 10
        self.moving = False

    def switch_to_walk_animation(self):
        switcher = Switcher(self.last_data, self.walking_animation, 30, False)
        ids = switcher.switch_animation.get_ids()
        self.walking_switcher = switcher
        self.animator_list.append(switcher)
        for x in self.character_parts:
            if x.id in ids:
                x.animator = switcher

    def switch_to_idle_animation(self):
        switcher = Switcher(self.last_data, self.idle_animation, 60)
        self.idle_switcher = switcher
        ids = switcher.switch_animation.get_ids()
        self.animator_list.append(switcher)
        for x in self.character_parts:
            if x.id in ids:
                x.animator = switcher

    def switch_to_take_sword_animation(self):
        switcher = Switcher(self.last_data, self.take_sword_animation, 30, True)
        ids = switcher.switch_animation.get_ids()
        self.take_sword_switcher = switcher
        self.animator_list.append(switcher)
        for x in self.character_parts:
            if x.id in ids:
                x.animator = switcher

    def switch_to_stabbing_animation(self):
        if self.mana >= 4:
            switcher = Switcher(self.last_data, self.stabbing_animation, 30, True)
            ids = switcher.switch_animation.get_ids()
            self.stabbing_switcher = switcher
            self.stabbing_switcher.switch_animation.current_fps = 0
            self.animator_list.append(switcher)
            for x in self.character_parts:
                if x.id in ids:
                    x.animator = switcher
            self.mana -= 4

    def switch_to_get_stabbing_animation(self):
        switcher = Switcher(self.last_data, self.get_stabbing_animation, 30, True)
        ids = switcher.switch_animation.get_ids()
        self.get_stabbing_switcher = switcher
        self.get_stabbing_switcher.switch_animation.current_fps = 0
        self.animator_list.append(switcher)
        for x in self.character_parts:
            if x.id in ids:
                x.animator = switcher

    def take_hand_sword(self):
        for x in self.equipment_list:
            if x.on_hand:
                x.config("#020", "#002", (0.5, 0.1), (0.1, 0.3))
                x.on_hand = False
                x.rotate = 0
            else:
                x.config("#020", "#011", (0.5, 0.1), (0.5, 0.6))
                x.on_hand = True
            self.refresh_equipment(x)

    def switch_to_swing_sword_animation(self):
        switcher = Switcher(self.current_animation, self.swing_sword_animation, 90)
        self.switcher_animation = switcher
        self.switcher_on = True
        self.current_animation.current_fps = 0
        self.current_animation = self.swing_sword_animation
        self.animation_ongoing = True

    def update(self, event, mouse_position, game_engine_lib):
        #drawer, scene, pause, display
        self.draw_character(self.skeleton, game_engine_lib.display)
        if game_engine_lib.pause is False:
            self.game_engine = game_engine_lib
            self.characterlook = self.check_look()
            a = True
            if self.get_distance_from_object(self.connected_character) >= 100:
                a = self.track_object()
            if not a and not self.moving:#burayı düzelt sürekli switch etmesin
                self.switch_to_walk_animation()
                self.moving = True
            if a:
                self.moving = False
            if self.stabbing_switcher is not None:
                pass
            if self.stabbing_switcher not in self.animator_list and self.get_distance_from_object(
                    self.connected_character) <= 100:
                self.switch_to_stabbing_animation()
            for x in self.animator_list:
                x.next()
