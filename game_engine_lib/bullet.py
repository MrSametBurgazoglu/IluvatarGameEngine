from .object import Nesne


class Bullet(Nesne):
    def __init__(self):
        super().__init__()
        self.set_current_image('bullet.png')
        self.direction = (0, 0)
        self.speed = 10

    def set_directional_image(self, angle):
        self.angle = angle

    def update(self, event, mouse_position, game_engine_lib):
        self.draw_object(game_engine_lib.display)
        if game_engine_lib.pause is False:# TODO bu sorguyu oyun motorunda yap.
            print(self.direction)
            self.pos_x += int(self.direction[0] * self.speed)
            self.pos_y += int(self.direction[1] * self.speed)
            wh = game_engine_lib.get_win_wh()
            if not (0 < self.pos_x < wh[0] and 0 < self.pos_y < wh[1]):
                game_engine_lib.current_scene.delete_object_list.append(self)



