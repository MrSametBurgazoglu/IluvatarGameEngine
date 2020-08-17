from .npc import NPC
from .skeleton import Skeleton
from pygame import image
from pygame.transform import rotate
from pygame import draw
from .tools import get_position_to_draw
from math import sin, cos, radians


class Enemy(NPC):
    def __init__(self):
        super().__init__()
        self.pos_x = 350
        self.pos_y = 350
        self.healt = 1000
        self.character_id = "#002"
        self.character_name = "TARET"
        self.character_image = image.load("taret.png")
        self.direction = 0
        self.current_image = self.character_image
        self.connect_to_a_character = True
        self.connected_character = "#000"
        self.mana = 10
        self.pos_to_draw = (self.pos_x, self.pos_y)

    def fire(self, display):
        print(self.direction)
        x2 = self.pos_x + cos(radians(self.direction)+90) * 200
        y2 = self.pos_y + sin(radians(self.direction)+90) * 200
        draw.line(display, (0, 0, 255), (self.pos_x, self.pos_y), (x2, y2), 20)

    def update(self, event, mouse_position, game_engine_lib):
        #drawer, scene, pause, display
        self.draw_immobile_character(self.current_image, game_engine_lib.display, self.pos_to_draw)
        if game_engine_lib.pause is False:
            self.game_engine = game_engine_lib
            self.direction = self.object_direction() + 180
            self.pos_to_draw = get_position_to_draw(self.character_image, (self.pos_x, self.pos_y),
                                       (self.character_image.get_width()/2,
                                        self.character_image.get_height()/2),
                                       self.direction)
            self.current_image = rotate(self.character_image, self.direction)
            self.fire(game_engine_lib.display)
