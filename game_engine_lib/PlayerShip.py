from .character import Character
from pygame.transform import rotate
from pygame import image
from .tools import get_position_to_draw
from math import sin, cos, radians


class PlayerShip(Character):
    def __init__(self):
        super().__init__()
        self.pos_x = 350
        self.pos_y = 300
        self.health = 100
        self.id = "#000"
        self.character_name = "BattleStar"
        self.direction = 0
        self.character_image = image.load("taret.png")
        self.direction = 0
        self.current_image = self.character_image
        self.pos_to_draw = (self.pos_x, self.pos_y)

    def update(self, event, mouse_position, game_engine_lib):
        #drawer, scene, pause, display
        self.draw_immobile_character(self.current_image, game_engine_lib.display, self.pos_to_draw)
        if game_engine_lib.pause is False:
            self.game_engine = game_engine_lib
            self.pos_to_draw = get_position_to_draw(self.character_image, (self.pos_x, self.pos_y),
                                       (self.character_image.get_width()/2,
                                        self.character_image.get_height()/2),
                                       self.direction)
            self.current_image = rotate(self.character_image, -self.direction-90)