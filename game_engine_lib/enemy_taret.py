from .npc import NPC
from pygame import image
from pygame.transform import rotate
from pygame import draw
from .tools import get_position_to_draw
from .bullet import Bullet
from math import sin, cos, radians


class Enemy(NPC):
    def __init__(self):
        super().__init__()
        self.pos_x = 350
        self.pos_y = 450
        self.healt = 1000
        self.id = "#002"
        self.character_name = "TARET"
        self.character_image = image.load("taret.png")
        self.direction = 0
        self.current_image = self.character_image
        self.connect_to_a_character = True
        self.connected_character = "#000"
        self.mana = 10
        self.pos_to_draw = (self.pos_x, self.pos_y)
        self.object_pos = None

    def fire(self, game_engine):
        if self.mana >= 10:
            bullet = Bullet()
            bullet.set_directional_image(self.direction)
            bullet.direction = (cos(radians(self.direction)), sin(radians(self.direction)))
            bullet.pos_x = self.pos_x
            bullet.pos_y = self.pos_y
            game_engine.current_scene.add_to_object_list(bullet)
            draw.line(game_engine.display, (0, 0, 255), (self.pos_x, self.pos_y), self.object_pos, 2)
            self.mana -= 10
        if self.mana < 10:
            self.mana += 0.1


    def update(self, event, mouse_position, game_engine_lib):
        #drawer, scene, pause, display
        self.draw_immobile_character(self.current_image, game_engine_lib.display, self.pos_to_draw)
        if game_engine_lib.pause is False:
            self.game_engine = game_engine_lib
            self.direction, self.object_pos = self.object_direction()
            self.pos_to_draw = get_position_to_draw(self.character_image, (self.pos_x, self.pos_y),
                                       (self.character_image.get_width()/2,
                                        self.character_image.get_height()/2),
                                       self.direction)
            self.current_image = rotate(self.character_image, -self.direction-90)
            self.fire(game_engine_lib)
