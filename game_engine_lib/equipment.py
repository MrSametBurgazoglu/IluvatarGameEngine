from .tools import get_from_list, get_data, get_position_to_draw, get_position_to_attach
from pygame import image
from pygame.transform import rotate


class Equipment(object):
    def __init__(self):
        self.id = None
        self.connected_id = None
        self.connect_type = None
        self.connected_parent = None
        self.connect_pos = (0.5, 0.5)
        self.connect_parent_pos = (0.5, 0.5)
        self.image = None
        self.width = 0
        self.height = 0
        self.rotate = 0
        self.on_hand = False
        self.gps = [0, 0, 0, 0]

    def config(self, id, connected_id, connect_pos, connect_parent_pos, image_url=None):
        self.id = id
        self.connected_id = connected_id
        self.connect_pos = connect_pos
        self.connect_parent_pos = connect_parent_pos
        if image_url is not None:
            self.image = image.load(image_url)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def get_pos_to_draw(self):
        origin_pos = (self.connect_parent_pos[0] * self.connected_parent.image.get_width(),
                      self.connect_parent_pos[1] * self.connected_parent.image.get_height())
        pos = get_position_to_attach(self.connected_parent.image, self.connected_parent.pos, origin_pos,
                                     self.connected_parent.rotate, self.connected_parent.pos_to_draw)
        origin_pos = (self.connect_pos[0] * self.width,
                      self.connect_pos[1] * self.height)
        if self.on_hand:
            self.rotate = self.connected_parent.rotate + 90
        pos_to_draw = get_position_to_draw(self.image, pos, origin_pos, self.rotate)
        self.gps = [pos_to_draw[0], pos_to_draw[1], self.width, self.height]
        return pos_to_draw

