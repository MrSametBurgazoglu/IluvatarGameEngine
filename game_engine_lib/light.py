from pygame.draw import circle


class Light(object):
    def __init__(self):
        self.pos_x = 300
        self.pos_y = 300
        self.radius = 300
        self.inner_radius = 20
        self.inside_power = 100
        self.outer_radius = 300
        self.outside_power = 200

    def draw_inside_circle(self, surface):
        for x in range(self.inner_radius, 5, -1):
            alpha = int((self.inside_power * x) / self.inner_radius)
            circle(surface, (255, 255, 255, 255-alpha), (self.pos_x, self.pos_y), x)

    def draw_outside_circle(self, surface):
        for x in range(self.outer_radius, self.inner_radius, -1):
            alpha = int((self.outside_power * x) / self.outer_radius)
            circle(surface, (0, 0, 0, alpha), (self.pos_x, self.pos_y), x)

    def lighting(self, surface):
        self.draw_outside_circle(surface)
        self.draw_inside_circle(surface)
