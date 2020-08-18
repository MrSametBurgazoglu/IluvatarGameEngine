from pygame import Surface
from pygame.transform import rotate
from pygame.image import save
from pygame import SRCALPHA
from pygame.transform import flip
from pygame.draw import ellipse


def get_maximum(liste, character_pos):
    max_y = 0
    min_y = 900
    max_x = 0
    min_x = 1400
    for x in liste:
        img = rotate(x.image, x.rotate)
        width = img.get_width()
        height = img.get_height()
        b = x.pos_to_draw[1]
        if b + height > max_y:
            max_y = b + height
        if b < min_y:
            min_y = b
        c = x.pos_to_draw[0]
        if c + width > max_x:
            max_x = c + width
        if c < min_x:
            min_x = c
    return [min_x-character_pos[0], max_x-character_pos[0], min_y-character_pos[1], max_y-character_pos[1]]


def get_maximum_only_maxy(liste, character_pos):
    max_y = 0
    for x in liste:
        height = x.image.get_height()
        b = x.pos[1]
        if b + height > max_y:
            max_y = b + height
    return max_y-character_pos[1]


def get_shadow(display, maximum_list, character_pos):
    x = int((maximum_list[1] + maximum_list[0])/2) + character_pos[0]
    y = maximum_list[3] + character_pos[1]
    surface = Surface((100, 40), SRCALPHA)
    ellipse(surface, (0, 0, 0, 150), (10, 5, 80, 32))
    display.blit(surface.convert_alpha(), (x-40, y-20))
