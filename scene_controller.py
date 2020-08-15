from pygame import KEYDOWN as pushed


class SceneController(object):
    def __init__(self):
        self.special_keywords = []
        self.user_interfaces = []
        self.pause = []
        self.make_pause = None
        self.only = False
        self.game_engine = None
        self.script = None

    def add_passage(self, keyword, interface):
        self.user_interfaces.append(interface)
        self.pause.append(interface.make_pause)
        self.special_keywords.append(keyword)

    def sets_state(self, event):
        for x, y in enumerate(self.special_keywords):
            for z in event:
                if z.type == pushed and y == z.key:
                    self.user_interfaces[x].state = not self.user_interfaces[x].state

    def update(self, event, eventg, mouse_position, game_engine_lib):
        self.sets_state(event)
        pause = False
        for x in self.user_interfaces:
            if x.state:
                if x.make_pause:
                    pause = True
                    game_engine_lib.pause = True
                x.update(eventg, event, mouse_position)
                game_engine_lib.draw_ui(x)
        if not pause:
            game_engine_lib.pause = False
        if self.script is not None:
            self.script()