import pygame


def get_data(id, data):
    for x in data:
        if x[0] == id:
            return x[1]


def get_class(id, data):
    for x in data:
        if x.id == id:
            return x

def get_position_to_draw(image, pos, originPos, angle):
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot
    origin = [pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1]]
    return origin


def get_position_to_attach(image, pos, originPos, angle, origin):
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    pivot2 = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate2 = pivot2.rotate(angle)
    pivot_move2 = pivot_rotate2 - pivot2
    origin2 = (
        pos[0] - originPos[0] + min_box[0] - pivot_move2[0], pos[1] - originPos[1] - max_box[1] + pivot_move2[1])
    origin2 = (origin[0] - origin2[0] + pos[0], origin[1] - origin2[1] + pos[1])
    return origin2


def get_from_list(id, liste):
    for x in liste:
        if x[0] == id:
            return x
