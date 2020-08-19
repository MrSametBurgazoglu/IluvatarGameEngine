from .object import Nesne


class Bullet(Nesne):
    def __init__(self):
        super().__init__()
        self.set_current_image('bullet.png')
        self.position_to_hit = (0, 0)
        self.speed = 10

    def __repr__(self):
        return str(self.id)

    def set_directional_image(self, angle):
        self.angle = angle

    def update(self, event, mouse_position, game_engine_lib):
        self.draw_object(game_engine_lib.display)
        if game_engine_lib.pause is False:
            if self.pos_x != self.position_to_hit[0]:
                if self.speed > abs(self.pos_x - self.position_to_hit[0]):  # hedefe uzaklık hızdan küçük ise
                    self.pos_x = self.position_to_hit[0]
                elif self.position_to_hit[0] > self.pos_x:  # hedef sağda ise
                    self.pos_x += self.speed
                elif self.pos_x > self.position_to_hit[0]:  # hedef solda ise
                    self.pos_x -= self.speed
            if self.pos_y != self.position_to_hit[1]:
                if self.speed > abs(self.pos_y - self.position_to_hit[1]):
                    self.pos_y = self.position_to_hit[1]
                elif self.position_to_hit[1] > self.pos_y:  # hedef yukarıda ise
                    self.pos_y += self.speed
                elif self.pos_y > self.position_to_hit[1]:  # hedef aşağıda ise
                    self.pos_y -= self.speed
            if self.pos_x == self.position_to_hit[0] and int(self.pos_y) == int(self.position_to_hit[1]):
                print(game_engine_lib.current_scene.object_list)
                print(self.__repr__())
                game_engine_lib.current_scene.object_list.remove(self.__repr__())



