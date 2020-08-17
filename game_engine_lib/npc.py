from .character import Character
from math import atan2, degrees


class NPC(Character):
    def __init__(self):
        super().__init__()
        self.connect_to_a_character = False

    #if in left return True else return False
    def check_look(self):
        if self.connect_to_a_character:
            for x in self.game_engine.current_scene.character_list:
                if x.character_id == self.connected_character and x.pos_x > self.pos_x:
                    return True
            else:
                return False

    def track_object(self):
        if self.connect_to_a_character:
            for x in self.game_engine.current_scene.character_list:
                if x.character_id == self.connected_character:
                    return self.move(x.pos_x, x.pos_y)

    def object_direction(self):
        if self.connect_to_a_character:
            for x in self.game_engine.current_scene.character_list:
                if x.character_id == self.connected_character:
                    return degrees(atan2(x.pos_x-self.pos_x, x.pos_y-self.pos_y))
