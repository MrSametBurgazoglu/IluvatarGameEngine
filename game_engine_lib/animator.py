class Switcher(object):
    def __init__(self, data, animation2, total_fps, finishable=True):
        self.switch_fps = 0
        self.total_fps = total_fps
        data2 = []
        ids = animation2.get_ids()
        for x in data:
            if x[0] in ids:
                data2.append(x)
        for x in data2:
            if x[1] < -180:
                x[1] += 360
        self.new_animation = animation2
        data2.insert(0, 0)
        self.animation_data = [data2]
        for x in self.new_animation.animation_data:
            a = [x[0] + total_fps]
            a.extend(x[1:])
            self.total_fps = x[0]
            self.animation_data.append(a)
        self.total_fps += total_fps
        self.switch_animation = Animator(self.animation_data, False, finishable)
        self.switch_animation.scripts = self.new_animation.scripts
        self.switch_animation.animation_total_fps = self.total_fps
        self.switch_animation.start_fps = total_fps

    def next(self):
        self.switch_animation.next()

    def get_all_data(self):
        return self.switch_animation.get_all_data()

    def get_data(self, id):
        return self.switch_animation.get_data(id)

    def get_ids(self):
        return self.switch_animation.get_ids()


class Animator(object):
    def __init__(self, animation_file, file=True, finishable=False):
        self.current_fps = 0
        self.lastfps = 0
        self.finishable = finishable
        self.fixed_point = []
        self.scripts = []
        self.ids = []
        self.start_fps = 0
        self.working = False
        self.animation_data = []  # A list of objects id,rotate for every fps
        self.animation_total_fps = 0
        if file:
            dosya = open(animation_file, "r")
            data = dosya.readlines()
            self.animation_data_line = []
            for x in data:
                x = x.strip()
                if "!" in x:
                    self.animation_total_fps = int(x[1:])
                    self.animation_data_line.append(self.animation_total_fps)
                    self.fixed_point.append(self.animation_total_fps)
                elif ">" in x:
                    self.animation_data.append(self.animation_data_line)
                    self.animation_data_line = []
                else:
                    y = x.strip()
                    a = y.split(":")
                    self.animation_data_line.append([a[0], float(a[1])])
                    self.ids.append(a[0])
        else:
            self.animation_data = animation_file
            temp = [x[0] for x in self.animation_data]
            for x in temp:
                self.fixed_point.append(x)
            for x in self.animation_data[1][1:]:
                self.ids.append(x[0])

    def get_data_from_fps(self, fps):
        for x in self.animation_data:
            if x[0] == fps:
                return x

    def get_ids(self):
        return self.ids

    def get_data(self, id):
        if self.current_fps in self.fixed_point:
            self.lastfps = self.current_fps
            for x in self.animation_data:
                if x[0] == self.current_fps:
                    for y in x[1:]:
                        if y[0] == id:
                            return y[1]
        else:
            next_fps = self.fixed_point[self.fixed_point.index(self.lastfps)+1]
            fps_dif = next_fps - self.lastfps
            previous_fps_object = self.get_data_from_fps(self.lastfps)
            next_fps_object = self.get_data_from_fps(next_fps)
            a1 = None
            a2 = None
            for x in previous_fps_object[1:]:
                if x[0] == id:
                    a1 = x
            for x in next_fps_object[1:]:
                if x[0] == id:
                    a2 = x
            rotate = a1[1] + (a2[1] - a1[1]) / fps_dif * (self.current_fps-self.lastfps)
            return rotate

    def get_all_data(self):
        if self.current_fps in self.fixed_point:
            self.lastfps = self.current_fps
            for x in self.animation_data:
                if x[0] == self.current_fps:
                    return x[1:]
        else:
            next_fps = self.fixed_point[self.fixed_point.index(self.lastfps)+1]
            fps_dif = next_fps - self.lastfps
            previous_fps_object = self.get_data_from_fps(self.lastfps)
            next_fps_object = self.get_data_from_fps(next_fps)
            liste = []
            for (x, y, z) in zip(previous_fps_object[1:], next_fps_object[1:], self.animation_data[0][1:]):
                a1 = x
                a2 = y
                rotate = a1[1] + (a2[1] - a1[1]) / fps_dif * (self.current_fps - self.lastfps)
                liste.append([z[0], rotate])
            return liste

    def next(self):
        for x in self.scripts:
            if x[0] == self.current_fps:
                x[1]()
        if self.current_fps == self.animation_total_fps-1:
            if self.finishable is False:
                self.current_fps = self.start_fps
            else:
                self.working = False
        else:
            self.current_fps += 1

    def is_working(self):
        return self.working
