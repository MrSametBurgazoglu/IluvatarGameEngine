class Scene:
    def __init__(self):
        self.background_image = None
        self.moveable_area = (800, 600)
        self.character_list = []
        self.object_list = []
        self.equipment_list = []
        self.auto_lightining = True
        self.scene_lights = []

    def add_to_character_list(self, character):
        self.character_list.append(character)

    def add_to_object_list(self, object):
        self.object_list.append(object)

    def add_light_to_scene(self, light):
        self.scene_lights.append(light)
