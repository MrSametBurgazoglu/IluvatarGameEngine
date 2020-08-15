class Nesne(object):
    def __init__(self):
        self.id = 0
        self.type = "kare"#0 = kare, 1 = daire
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
        self.yaricap = 5
        self.physic_on = True

    def update(self, event, drawer):
        pass
