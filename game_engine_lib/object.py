from pygame import image
from .tools import get_position_to_draw
from pygame.transform import rotate


class Nesne(object):
    def __init__(self):
        self.id = 0
        self.type = "kare"#0 = kare, 1 = daire
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
        self.yaricap = 5
        self.angle = 0
        self.physic_on = True
        self.object_image = image.load('taret.png')
        self.current_image = self.object_image
        self.pos_to_draw = (self.pos_x, self.pos_y)

    def set_current_image(self, path):
        self.object_image = image.load(path)

    def draw_object(self, display):
        self.pos_to_draw = get_position_to_draw(self.object_image, (self.pos_x, self.pos_y),
                                                (self.object_image.get_width() / 2,
                                                 self.object_image.get_height() / 2),
                                                self.angle)
        self.current_image = rotate(self.object_image, self.angle)
        display.blit(self.current_image, self.pos_to_draw)
