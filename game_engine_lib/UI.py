from pygame import font
from pygame import MOUSEBUTTONDOWN

font.init()


class Widget(object):
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.height = 0
        self.width = 0


class UI(object):
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
        self.background_color = "white"
        self.background_image = None
        self.widgets = []
        self.active_entry = None
        self.make_pause = False
        self.state = False
        self.font = font.SysFont('Comic Sans MS', 30)

    def add_widget(self, widget):
        self.widgets.append(widget)

    def set_font_size(self, size):
        self.font = font.SysFont('Comic Sans MS', size)

    def get_where_clicked(self, mouse_position):
        for x, y in enumerate(self.widgets):
            if self.pos_x + y.pos_x < mouse_position[0] < self.pos_x + y.pos_x + y.width and\
                    self.pos_y + y.pos_y < mouse_position[1] < self.pos_y + y.pos_y + y.height:
                return x

    def temp(self, eventx):
        for x in eventx:
            if x.type == MOUSEBUTTONDOWN and x.button == 1:
                return True

    def update(self, event, eventx, mouse_positon):
        if self.temp(eventx) is True and mouse_positon != (0, 0):
            x = self.get_where_clicked(mouse_positon)
            if x is not None:
                clicked_widget = self.widgets[x]
                if clicked_widget.type == "button_widget":
                    clicked_widget.clicked()
                elif clicked_widget.type == "entry_widget":
                    self.active_entry = clicked_widget
            else:
                self.active_entry = None
        if mouse_positon != (0, 0):
            x = self.get_where_clicked(mouse_positon)
            if x is not None:
                clicked_widget = self.widgets[x]
                if clicked_widget.type == "button_widget":
                    clicked_widget.onbutton = True
        if "keyboard_used" in event:
            if self.active_entry is not None:
                for x in event:
                    if "backspace" in x:
                        self.active_entry.text = self.active_entry.text[:-1]
                    elif "pressed" in x:
                        self.active_entry.text += x[0]

    def draw_ui(self, display, drawer):
        if self.background_color != "transparent":
            drawer.rect(display, (0, 0, 255), [self.pos_x, self.pos_y, self.width, self.height], 0)
        for x in self.widgets:
            x.draw_self(display, drawer, (self.pos_x, self.pos_y), self.font)


class TextWidget(Widget):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.type = "text_widget"
        self.font_color = (0, 0, 0)

    def draw_self(self, display, drawer, pos, Font):
        display.blit(Font.render(self.text, False, self.font_color), (self.pos_x+pos[0], self.pos_y+pos[1]))


class ButtonWidget(Widget):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.type = "button_widget"
        self.func = None
        self.args = None
        self.font_color = (0, 0, 0)
        self.onbutton = False

    def draw_self(self, display, drawer, pos, Font):
        if self.onbutton:
            drawer.line(display, (255, 255, 255),
                        (self.pos_x+pos[0], self.pos_y+pos[1]+self.height),
                        (self.pos_x+pos[0]+self.width, self.pos_y+pos[1]+self.height))
        display.blit(Font.render(self.text, False, self.font_color), (self.pos_x+pos[0], self.pos_y+pos[1]))
        self.onbutton = False

    def set_clicked(self, func, *args):
        self.func = func
        self.args = args

    def clicked(self):
        self.func(self.args)


class ImageButtonWidget(Widget):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.type = "button_widget"
        self.func = None
        self.args = None
        self.font_color = (0, 0, 0)
        self.image = None

    def draw_self(self, display, drawer, pos, Font):
        display.blit(self.image, (self.pos_x+pos[0], self.pos_y+pos[1]))
        display.blit(Font.render(self.text, False, self.font_color), (self.pos_x+pos[0], self.pos_y+pos[1]))
        self.onbutton = False

    def set_clicked(self, func, *args):
        self.func = func
        self.args = args

    def clicked(self):
        self.func(self.args)


class ImageWidget(Widget):
    def __init__(self):
        super().__init__()
        self.image = None
        self.image2 = None
        self.gif = False
        self.background = False
        self.sayac = 0

    def draw_self(self, display, drawer, pos, Font):
        if self.background:
            drawer.rect(display, (0, 0, 0),
                        [self.pos_x + pos[0], self.pos_y + pos[1],
                         self.image.get_width(), self.image.get_height()], 0)
        if self.gif:
            if self.sayac % 400 >= 200:
                display.blit(self.image, (self.pos_x + pos[0], self.pos_y + pos[1]))
            else:
                display.blit(self.image2, (self.pos_x + pos[0], self.pos_y + pos[1]))
            self.sayac += 1
        else:
            display.blit(self.image, (self.pos_x + pos[0], self.pos_y + pos[1]))


class EntryWidget(Widget):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.type = "entry_widget"
        self.font_size = 20
        self.font = font.SysFont('Comic Sans MS', self.font_size)
        self.font_color = (0, 0, 0)

    def draw_self(self, display, drawer, pos, Font):
        drawer.rect(display, (0, 0, 0), [self.pos_x+pos[0], self.pos_y+pos[1], self.width, self.height], 1)
        display.blit(Font.render(self.text[-11:], False, self.font_color), (self.pos_x+pos[0], self.pos_y+pos[1]-self.font_size/2))


class LineWidget(Widget):
    def __init__(self):
        super().__init__()
        self.type = "line_widget"
        self.bold_line = 50
        self.width = 100

    def draw_self(self, display, drawer, pos, Font):
        drawer.line(display, (200, 200, 200),
                    (self.pos_x+pos[0], self.pos_y+pos[1]+20),
                    (self.pos_x+pos[0]+self.width, self.pos_y+pos[1]+20), 10)
        drawer.line(display, (255, 255, 255),
                    (self.pos_x + pos[0], self.pos_y + pos[1] + 20),
                    (self.pos_x + pos[0]+(self.width * self.bold_line / 100), self.pos_y + pos[1] + 20), 10)


class LinerWidget(Widget):
    def __init__(self):
        super().__init__()
        self.bold = 0
        self.color = (0, 0, 0)
        self.widgets = []
        self.child_space = 20
        self.orientation = 0 #0=> vertical, 1=> horizontal
        self.type = "parent"

    def add_widgets(self, widget):
        if self.orientation == 0:
            widget.pos_x = 10
            widget.pos_y = len(self.widgets) * self.child_space + 10
        else:
            widget.pos_y = 10
            widget.pos_x = len(self.widgets) * self.child_space + 10
        self.widgets.append(widget)

    def draw_self(self, display, drawer, pos, Font):
        drawer.rect(display, self.color, [self.pos_x+pos[0], self.pos_y+pos[1], self.width, self.height],
                    self.bold)
        for x in self.widgets:
            x.draw_self(display, drawer, (pos[0]+self.pos_x, pos[1]+self.pos_y), Font)
