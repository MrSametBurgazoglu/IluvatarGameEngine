from .character import Character
from pygame.transform import rotate
from pygame import image
from .tools import get_position_to_draw
from game_engine_lib import physic
from math import sin, cos, radians
from .bullet import Bullet


class PlayerShip(Character):
    def __init__(self):
        super().__init__()
        self.pos_x = 350
        self.pos_y = 300
        self.health = 100
        self.id = "#000"
        self.character_name = "BattleStar"
        self.direction = 0
        self.character_image = image.load("fighter.png")
        self.direction_move = (0, 0, 0, 0)
        self.current_image = self.character_image
        self.pos_to_draw = (self.pos_x, self.pos_y)

    def fire(self, game_engine):
        bullet = Bullet()
        bullet.set_directional_image(self.direction)
        bullet.direction = (cos(radians(self.direction-90)), sin(radians(self.direction-90)))
        bullet.pos_x = self.pos_x
        bullet.pos_y = self.pos_y
        game_engine.current_scene.add_to_object_list(bullet)

    def update(self, event, mouse_position, game_engine_lib):
        #drawer, scene, pause, display
        self.draw_immobile_character(self.current_image, game_engine_lib.display, self.pos_to_draw)
        if game_engine_lib.pause is False:
            self.game_engine = game_engine_lib
            self.pos_to_draw = get_position_to_draw(self.character_image, (self.pos_x, self.pos_y),
                                       (self.character_image.get_width()/2,
                                        self.character_image.get_height()/2),
                                       self.direction)
            self.current_image = rotate(self.character_image, -self.direction)
            self.direction_move = (
                cos(radians(self.direction-90)),
                sin(radians(self.direction-90)),
                cos(radians(self.direction)),
                sin(radians(self.direction)),
            )

            if game_engine_lib.pause is False:
                tx = self.pos_x
                ty = self.pos_y
                if "d_pressed" in event:
                    tx += self.direction_move[2]
                    ty += self.direction_move[3]
                    self.characterlook = True
                elif "a_pressed" in event:
                    tx -= self.direction_move[2]
                    ty -= self.direction_move[3]
                    self.characterlook = False
                if "w_pressed" in event:
                    tx += 2 * self.direction_move[0]
                    ty += 2 * self.direction_move[1]
                elif "s_pressed" in event:
                    tx -= self.direction_move[0]
                    ty -= self.direction_move[1]
                if "e_pressed" in event:
                    self.direction += 1
                elif "q_pressed" in event:
                    self.direction -= 1
                if tx != self.pos_x or ty != self.pos_y:
                    event.append("character_moved")
                if "character_moved" in event:
                    event.remove("character_moved")
                if physic.is_possible(tx, ty, game_engine_lib.current_scene):
                    self.pos_x, self.pos_y = tx, ty
                if "left_click" in event:
                    self.fire(game_engine_lib)