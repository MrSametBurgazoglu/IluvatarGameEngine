import pygame
from .tools import get_data, get_from_list, get_position_to_draw, get_position_to_attach, get_class


class Skeleton(object):
    def __init__(self, filename):
        self.dosya = open(filename)
        self.lines = self.dosya.readlines()
        self.parts = []#id,bağlılığın_xi,bağlılığın_ysi,bağlılık,resmin_xi,resmin_ysi
        for x in self.lines:
            self.parts.append(x.strip().split(":"))
        self.dependence_tree = self.create_dependence_tree()

    def create_dependence_tree(self):
        first_one = None
        for x in self.parts:
            if x[3] == "None":
                first_one = x[0]
        liste = [first_one]
        temp = []
        all_list = [[first_one]]
        while len(liste) != 0:
            for x in self.parts:
                if x[3] in liste:
                    temp.append(x[0])
            liste = temp
            all_list.append(liste)
            temp = []
        all_list.pop(-1)
        return all_list

    def get_dependence(self, id):
        for x in self.parts:
            if x[0] == id:
                return x[3]

    def get_centers(self, id):
        for x in self.parts:
            if x[0] == id:
                return float(x[1]), float(x[2])

    def get_centers2(self, id):
        for x in self.parts:
            if x[0] == id:
                return float(x[4]), float(x[5])

    def update_pos_image(self, data, character_parts, character_pos):
        a = self.dependence_tree[0][0]
        sinif = get_class(a, character_parts)
        rotate = get_data(a, data)  # bölümün rotatini al
        img = sinif.image  # bölümün resmini al
        sinif.rotate = rotate
        center = self.get_centers2(a)
        origin_pos = (center[0] * img.get_width(), center[1] * img.get_height())
        pos_to_draw = get_position_to_draw(img, character_pos, origin_pos, rotate)
        sinif.pos = character_pos
        sinif.pos_to_draw = pos_to_draw
        for x in self.dependence_tree[1:]:
            for y in x:
                center = self.get_centers(y)
                dependence = self.get_dependence(y)
                sinif = get_class(dependence, character_parts)
                dependence_rotate = get_data(dependence, data)
                origin_pos = (center[0] * sinif.image.get_width(), center[1] * sinif.image.get_height())
                pos = get_position_to_attach(sinif.image, sinif.pos, origin_pos,
                                             dependence_rotate, sinif.pos_to_draw)
                sinif = get_class(y, character_parts)
                img = sinif.image
                rotate = get_data(y, data)
                sinif.rotate = rotate
                center = self.get_centers2(y)
                origin_pos = (center[0] * img.get_width(), center[1] * img.get_height())
                pos_to_draw = get_position_to_draw(img, pos, origin_pos, rotate)
                sinif.pos = pos
                sinif.pos_to_draw = pos_to_draw
