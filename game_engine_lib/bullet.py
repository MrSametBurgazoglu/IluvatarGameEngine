from .object import Nesne


class Bullet(Nesne):
    def __init__(self):
        super().__init__()
        self.set_current_image('bullet.png')
        self.position_to_hit = (0, 0)
        self.speed = 10

    def set_directional_image(self, angle):
        self.angle = angle

    def update(self, event, mouse_position, game_engine_lib):
        self.draw_object(game_engine_lib.display)
        if game_engine_lib.pause is False:
            if self.pos_x != self.position_to_hit[0]:
                self.pos_x += self.speed
            if self.pos_y != self.position_to_hit[1]:
                self.pos_y += self.speed



