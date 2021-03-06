from .character import Character
from .animator import Animator
from .animator import Switcher
from .skeleton import Skeleton
from game_engine_lib import physic


class Player(Character):
    def __init__(self):
        super().__init__()
        self.pos_x = 350
        self.pos_y = 300
        self.health = 100
        self.id = "#000"
        self.character_name = "HERO"
        self.idle_animation = Animator("game/animations/player_idle.animation", True, False)
        self.walking_animation = Animator("game/animations/player_walking.animation", True, False)
        self.stabbing_animation = Animator("game/animations/player_stabbing.animation", True, True)
        self.take_sword_animation = Animator("game/animations/player_take_sword.animation", True, True)
        self.take_sword_animation.scripts.append([89, self.take_hand_sword])
        self.swing_sword_animation = Animator("game/animations/player_swing_sword.animation", True, True)
        self.tumble_animation = Animator("game/animations/player_tumble.animation", True, True, True)
        self.add_to_animator_list(None, self.idle_animation)
        self.add_to_animator_list('character_moved', self.walking_animation)
        self.add_to_animator_list('q_pressed', self.stabbing_animation)
        self.add_to_animator_list('e_pressed', self.take_sword_animation)
        self.add_to_animator_list('w_pressed', self.swing_sword_animation)
        self.add_to_animator_list('space_pressed', self.tumble_animation)
        #self.animator_list.append([None, self.idle_animation, None])
        #self.animator_list.append(['character_moved', self.walking_animation, None])
        #self.animator_list.append(['q_pressed', self.stabbing_animation, None])
        #self.animator_list.append(['e_pressed', self.take_sword_animation, None])
        #self.animator_list.append(['w_pressed', self.swing_sword_animation, None])
        #self.animator_list.append(['space_pressed', self.tumble_animation, None])
        self.skeleton = Skeleton("game/skeletons/player.skeleton")
        self.add_character_parts("#004", "game/karakter/l_arm.png")
        self.add_character_parts("#006", "game/karakter/l_foot.png")
        self.add_character_parts("#008", "game/karakter/l_knee.png")
        self.add_character_parts("#010", "game/karakter/l_leg.png")
        self.add_character_parts("#012", "game/karakter/l_hand.png")
        self.add_character_parts("#002", "game/karakter/body.png")
        self.add_character_parts("#001", "game/karakter/head.png")
        self.add_character_parts("#003", "game/karakter/r_arm.png")
        self.add_character_parts("#007", "game/karakter/r_knee.png")
        self.add_character_parts("#009", "game/karakter/r_leg.png")
        self.add_character_parts("#005", "game/karakter/r_foot.png")
        self.add_character_parts("#011", "game/karakter/r_hand.png")
        for x in self.character_parts:
            self.last_data.append([x.id, x.rotate])
        self.mana = 10.0
        self.animator_list[0][2] = self.switch_to_animation(self.animator_list[0][1])

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

    def animator_controller(self, event):
        act = False
        for x in self.animator_list:  # TODO PERFORMANCE ISSUES MOST BE SOLVED
            if x[0] in event and not self.is_untouchable():
                if x[2] is None:
                    x[2] = self.switch_to_animation(x[1])
                else:
                    if not x[2].switch_animation.is_working():
                        x[2] = self.switch_to_animation(x[1])
            if x[2] is not None:
                self.action_list[x[1]] = x[2].switch_animation.working
                if x[2].switch_animation.is_working():
                    x[2].next()
                    if x[2].switch_animation.finishable:
                        act = True
        keywords = [x[0] for x in self.animator_list]
        if self.action_list[self.idle_animation] is False and not any(item in keywords for item in event) and not act \
                and "character_moved" not in event and not self.is_untouchable():
            self.animator_list[0][2] = self.switch_to_animation(self.animator_list[0][1])

    def is_untouchable(self):
        for x in self.action_list:
            if self.action_list[x] and x.untouchable:
                return True
        return False

    def switch_to_animation(self, animation):
        switcher = Switcher(self.last_data, animation, 30, animation.finishable)
        ids = switcher.switch_animation.get_ids()
        for x in self.character_parts:
            if x.id in ids:
                try:
                    x.animator.switch_animation.working = False
                except AttributeError:
                    pass
                x.animator = switcher
                x.animator.switch_animation.working = True
        return switcher

    def get_attacked(self):
        self.health -= 10

    def update(self, event, mouse_position, game_engine_lib):
        #drawer, scene, pause, display
        self.draw_character(self.skeleton, game_engine_lib.display)
        if game_engine_lib.pause is False:
            tx = self.pos_x
            ty = self.pos_y
            if "right_key" in event:
                tx += 1.5
                self.characterlook = True
            elif "left_key" in event:
                tx -= 1.5
                self.characterlook = False
            if "up_key" in event:
                ty -= 1.5
            elif "down_key" in event:
                ty += 1.5
            if tx != self.pos_x or ty != self.pos_y:
                event.append("character_moved")
            self.animator_controller(event)
            if "character_moved" in event:
                event.remove("character_moved")
            if physic.is_possible(tx, ty, game_engine_lib.current_scene):
                self.pos_x, self.pos_y = tx, ty
