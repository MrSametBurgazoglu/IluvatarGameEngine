from math import sqrt


def is_possible(x, y, scene):
    result = True
    for nesne in scene.object_list:
        if nesne.type == 0:
            if is_possible_kare(x, y, nesne) is False:
                return False
        elif nesne.type == 1:
            if is_possible_kare(x, y, nesne) is False:
                return False

    return True


def is_possible_kare(x, y, nesne):
    if nesne.pos_x < x < nesne.pos_x + nesne.width and nesne.pos_y < y < nesne.pos_y + nesne.height and nesne.physic_on:
        return False
    else:
        return True


def find_distance(x, y, center_x, center_y):
    a = abs(center_x - x)**2
    b = abs(center_y - y)**2
    return sqrt(a+b)


def is_possible_daire(x, y, nesne):
    if find_distance(x, y, nesne.x, nesne.y) <= nesne.yaricap and nesne.physic_on:
        return False
    else:
        return True


def find_which_one(x, y, scene):
    for nesne in scene:
        if nesne.pos_x < x < nesne.pos_x + nesne.width and nesne.pos_y < y < nesne.pos_y + nesne.height:
            return nesne.id
