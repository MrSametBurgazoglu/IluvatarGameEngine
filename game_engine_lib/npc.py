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
                if x.id == self.connected_character and x.pos_x > self.pos_x:
                    return True
            else:
                return False

    def track_object(self):
        if self.connect_to_a_character:
            for x in self.game_engine.current_scene.character_list:
                if x.id == self.connected_character:
                    return self.move(x.pos_x, x.pos_y)

    def object_direction(self):
        if self.connect_to_a_character:
            for x in self.game_engine.current_scene.character_list:
                if x.id == self.connected_character:
                    object_pos = (x.pos_x + (x.max_list[1]-x.max_list[0])/2,
                                  x.pos_y+(x.maximum_list[3]-x.character_image.get_height()/2))
                    return degrees(atan2(object_pos[1]-self.pos_y, object_pos[0]-self.pos_x)), object_pos
