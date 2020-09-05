from pygame import image
from pygame import Surface
from pygame import SRCALPHA
from .nesne import Nesne
from pygame.transform import rotate, flip
from game_engine_lib import shadow
from pygame.draw import rect as draw_rect


class Character(object):
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
        self.gps = [0, 0, 0, 0]
        self.healt = 0#WORK IN PROGRESS
        self.speed = 1#npclerin hızları
        self.characterlook = True# True => right False => left
        self.character_name = None
        self.id = None#must be unique
        self.character_logo_dir = None
        self.character_parts = []#id,image
        self.liste = []#skeletondan dönen verilerin tutulduğu liste
        self.last_data = []#son animatordan dönen veriler
        self.animator_list = []# key, animation, switcher
        self.maximum_list = []
        self.max_list = []
        self.equipment_list = []
        self.character_image = None
        self.game_engine = None
        self.connected_character = None#bir karaktere bağlanmak
        self.action_list = {}

    def move(self, x, y):
        if x > self.pos_x and self.characterlook is False: #Gideceği hedef sağ tarafta ve karakter sola bakıyor
            self.characterlook = True
            #Ayrıca sağ tarafa gidiş animasyonunun ilk resmi current image olacak
        if x < self.pos_x and self.characterlook is True: #Gideceği hedef sol tarafta ve karakter sağa bakıyor
            self.characterlook = True
            #Ayrıca sağ tarafa gidiş animasyonunun ilk resmi current image olacak
        if self.pos_x != x:
            if self.speed > abs(self.pos_x - x):#hedefe uzaklık hızdan küçük ise
                self.pos_x = x
            elif x > self.pos_x:#hedef sağda ise
                self.pos_x += self.speed
            elif self.pos_x > x:#hedef solda ise
                self.pos_x -= self.speed
        if self.pos_y != y:
            if self.speed > abs(self.pos_y - y):
                self.pos_y = y
            elif y > self.pos_y:#hedef yukarıda ise
                self.pos_y += self.speed
            elif self.pos_y > y:#hedef aşağıda ise
                self.pos_y -= self.speed
        if self.pos_x == x and self.pos_y == y:
            return True #Hareket Tamamlandı
        else:
            return False #Hareket Tamamlanmadı

    def change_character_parts(self, id, url):#character bölümlerini sonradan değiştirmeye  yarar
        img = image.load(url).convert_alpha()
        for x, y in enumerate(self.character_parts):
            self.character_parts.insert(x, [id, img])
            self.character_parts.remove(y)

    def add_character_parts(self, id, image_path):#character bölümlerini ekler
        character_part = Nesne()
        img = image.load(image_path).convert_alpha()#convert_alpha()
        character_part.id = id
        character_part.image = img
        self.character_parts.append(character_part)

    def add_equipment(self, equipment):
        for x in self.character_parts:
            if x.id == equipment.connected_id:
                equipment.connected_parent = x
                self.equipment_list.append(equipment)

    def refresh_equipment(self, equipment):
        for x in self.character_parts:
            if x.id == equipment.connected_id:
                equipment.connected_parent = x

    def remove_from_animator_list(self, animation):
        self.animator_list.remove(animation)
        self.refresh_animator_list()

    def refresh_animator_list(self):
        for x in self.character_parts:
            for y in self.animator_list:
                ids = y.get_ids()
                if x.id in ids:
                    x.animator = y

    def set_character_parts(self, skeleton):
        a = []
        for x in self.character_parts:
            a.append([x.id, x.animator.get_data(x.id)])
        self.last_data = a
        skeleton.update_pos_image(a, self.character_parts, (self.pos_x, self.pos_y))

    def draw_character_image(self, max_list):
        pos_list = [(x.pos_to_draw[0]-self.pos_x-max_list[0], x.pos_to_draw[1]-self.pos_y-max_list[2])for x in self.character_parts]
        for y, x in enumerate(self.character_parts):
            rotated_image = rotate(x.image, x.rotate)
            pos = (pos_list[y][0], pos_list[y][1])
            pos_list.append(pos)
            self.character_image.blit(rotated_image, pos)
        for x in self.equipment_list:
            a = x.get_pos_to_draw()
            pos = [a[0]-self.pos_x-max_list[0], a[1]-self.pos_y-max_list[2]]
            rotated_image = rotate(x.image, x.rotate)
            self.character_image.blit(rotated_image, pos)

    def draw_character(self, skeleton, display):
        self.set_character_parts(skeleton)
        self.max_list = shadow.get_maximum(self.character_parts, (self.pos_x, self.pos_y))
        self.width = self.max_list[1] - self.max_list[0]
        self.height = self.max_list[3] - self.max_list[2]
        self.gps[2] = self.width
        self.gps[3] = self.height
        self.character_image = Surface((self.width, self.height), SRCALPHA)
        if len(self.maximum_list) == 0:
            self.maximum_list = shadow.get_maximum(self.character_parts, (self.pos_x, self.pos_y))
        self.draw_shadow(self.maximum_list, display)
        self.set_physic()
        self.draw_character_image(self.max_list)
        img = self.character_image.convert_alpha()  # convert_alpha
        if not self.characterlook:
            img = flip(img, True, False)
        display.blit(img, (self.pos_x,
                           self.pos_y+(self.maximum_list[3]-self.character_image.get_height())))
        self.gps[0] = self.pos_x
        self.gps[1] = self.pos_y+(self.maximum_list[3]-self.character_image.get_height())

    def draw_immobile_character(self, image, display, pos):
        display.blit(image, pos)

    def draw_shadow(self, liste, display):
        shadow.get_shadow(display, liste, (self.pos_x+(self.maximum_list[1]-self.maximum_list[0])/2, self.pos_y))

    def set_physic(self):
        maxy = shadow.get_maximum_only_maxy(self.character_parts, (self.pos_x, self.pos_y))
        dif = self.maximum_list[3] - maxy
        if self.maximum_list[3] > maxy and dif > 10:
            for x in self.liste:
                x[2][1] += dif

    def get_distance_from_object(self, id):
        for x in self.game_engine.current_scene.character_list:
            if x.id == id:
                return ((x.pos_x-self.pos_x) ** 2 + (x.pos_y-self.pos_y) ** 2) ** 0.5

    def add_to_animator_list(self, key, animation):
        self.animator_list.append([key, animation, None])
        self.action_list[animation] = False
