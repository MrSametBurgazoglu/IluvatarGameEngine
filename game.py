import pygame

white = (255, 255, 255)
black = (0, 0, 0)

END_MUSIC_EVENT = pygame.USEREVENT + 0
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)

mouse_dict = {1: "left_click",
              2: "middle_click",
              3: "right_click",
              4: "scroll_up",
              5: "scroll_down"}


class Musichandler(object):
    def __init__(self):
        self.no = 0
        self.music_list = ["output.wav"]

    def add_to_list(self, file):
        self.music_list.append(file)

    def play(self):
        effect = pygame.mixer.Sound('output.wav')
        effect.play()
        self.no += 1


class GameEngine(object):
    def __init__(self):
        pygame.init()
        self.win_width = 800
        self.win_height = 600
        self.window_name = "Game_Engine_Test"
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.display = None
        self.current_scene = None
        self.scene_background = None
        self.characters = []
        self.auto_lightining = False
        self.scene_light = None
        self.moveable_area = (0, 0)
        self.scene_controller = None
        #self.music_handler = Musichandler()
        #self.music_handler.play()
        self.pause = False

    def set_win_wh(self, widht, height):
        self.win_width = widht
        self.win_height = height

    def get_win_wh(self):
        return self.win_width, self.win_height

    def set_window_name(self, name):
        self.window_name = name
        pygame.display.set_caption(self.window_name)

    def get_window_name(self):
        return self.window_name

    def set_fps(self, fps):
        self.fps = fps

    def get_fps(self):
        return self.fps

    def draw_ui(self, ui):
        ui.draw_ui(self.display, pygame.draw)

    def quit(self, arg):
        pygame.quit()
        exit()

    def init_engine(self):
        self.display = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption(self.window_name)

    def init_scene(self, scene):
        self.scene_background = pygame.image.load(scene.background_image)
        self.characters = scene.character_list
        self.current_scene = scene

    def draw_image(self, image, pos):
        self.display.blit(image, pos)

    def set_scene_controller(self, scene_controller):
        self.scene_controller = scene_controller

    def start_engine(self):
        eventg = []
        while 1:
            eventx = []
            self.display.fill(white)
            self.display.blit(self.scene_background, (0, 0))
            for event in pygame.event.get():
                eventx.append(event)
                self.clock.tick(self.fps)
                if event.type == pygame.MOUSEBUTTONUP:
                    eventg.remove(mouse_dict[event.button])
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        eventg.remove("left_key")
                    elif event.key == pygame.K_RIGHT:
                        eventg.remove("right_key")
                    elif event.key == pygame.K_UP:
                        eventg.remove("up_key")
                    elif event.key == pygame.K_DOWN:
                        eventg.remove("down_key")
                    elif event.key == pygame.K_0:
                        eventg.remove("0_pressed")
                    elif event.key == pygame.K_1:
                        eventg.remove("1_pressed")
                    elif event.key == pygame.K_2:
                        eventg.remove("2_pressed")
                    elif event.key == pygame.K_3:
                        eventg.remove("3_pressed")
                    elif event.key == pygame.K_4:
                        eventg.remove("4_pressed")
                    elif event.key == pygame.K_5:
                        eventg.remove("5_pressed")
                    elif event.key == pygame.K_6:
                        eventg.remove("6_pressed")
                    elif event.key == pygame.K_7:
                        eventg.remove("7_pressed")
                    elif event.key == pygame.K_8:
                        eventg.remove("8_pressed")
                    elif event.key == pygame.K_9:
                        eventg.remove("9_pressed")
                    elif event.key == pygame.K_q:
                        eventg.remove("q_pressed")
                    elif event.key == pygame.K_w:
                        eventg.remove("w_pressed")
                    elif event.key == pygame.K_e:
                        eventg.remove("e_pressed")
                    elif event.key == pygame.K_r:
                        eventg.remove("r_pressed")
                    elif event.key == pygame.K_t:
                        eventg.remove("t_pressed")
                    elif event.key == pygame.K_y:
                        eventg.remove("y_pressed")
                    elif event.key == pygame.K_u:
                        eventg.remove("u_pressed")
                    elif event.key == pygame.K_o:
                        eventg.remove("o_pressed")
                    elif event.key == pygame.K_p:
                        eventg.remove("p_pressed")
                    elif event.key == pygame.K_a:
                        eventg.remove("a_pressed")
                    elif event.key == pygame.K_s:
                        eventg.remove("s_pressed")
                    elif event.key == pygame.K_d:
                        eventg.remove("d_pressed")
                    elif event.key == pygame.K_f:
                        eventg.remove("f_pressed")
                    elif event.key == pygame.K_g:
                        eventg.remove("g_pressed")
                    elif event.key == pygame.K_h:
                        eventg.remove("h_pressed")
                    elif event.key == pygame.K_j:
                        eventg.remove("j_pressed")
                    elif event.key == pygame.K_k:
                        eventg.remove("k_pressed")
                    elif event.key == pygame.K_l:
                        eventg.remove("l_pressed")
                    elif event.key == pygame.K_z:
                        eventg.remove("z_pressed")
                    elif event.key == pygame.K_x:
                        eventg.remove("x_pressed")
                    elif event.key == pygame.K_c:
                        eventg.remove("c_pressed")
                    elif event.key == pygame.K_v:
                        eventg.remove("v_pressed")
                    elif event.key == pygame.K_b:
                        eventg.remove("b_pressed")
                    elif event.key == pygame.K_n:
                        eventg.remove("n_pressed")
                    elif event.key == pygame.K_m:
                        eventg.remove("m_pressed")
                    elif event.key == pygame.K_BACKSPACE:
                        eventg.remove("backspace_pressed")
                    elif event.key == pygame.K_SPACE:
                        eventg.remove("space_pressed")
                elif event.type == pygame.KEYDOWN:
                    eventg.append("keyboard_used")
                    if event.key == pygame.K_LEFT:
                        eventg.append("left_key")
                    elif event.key == pygame.K_RIGHT:
                        eventg.append("right_key")
                    elif event.key == pygame.K_UP:
                        eventg.append("up_key")
                    elif event.key == pygame.K_DOWN:
                        eventg.append("down_key")
                    elif event.key == pygame.K_ESCAPE:
                        eventg.append("ESC")
                    elif event.key == pygame.K_0:
                        eventg.append("0_pressed")
                    elif event.key == pygame.K_1:
                        eventg.append("1_pressed")
                    elif event.key == pygame.K_2:
                        eventg.append("2_pressed")
                    elif event.key == pygame.K_3:
                        eventg.append("3_pressed")
                    elif event.key == pygame.K_4:
                        eventg.append("4_pressed")
                    elif event.key == pygame.K_5:
                        eventg.append("5_pressed")
                    elif event.key == pygame.K_6:
                        eventg.append("6_pressed")
                    elif event.key == pygame.K_7:
                        eventg.append("7_pressed")
                    elif event.key == pygame.K_8:
                        eventg.append("8_pressed")
                    elif event.key == pygame.K_9:
                        eventg.append("9_pressed")
                    elif event.key == pygame.K_q:
                        eventg.append("q_pressed")
                    elif event.key == pygame.K_w:
                        eventg.append("w_pressed")
                    elif event.key == pygame.K_e:
                        eventg.append("e_pressed")
                    elif event.key == pygame.K_r:
                        eventg.append("r_pressed")
                    elif event.key == pygame.K_t:
                        eventg.append("t_pressed")
                    elif event.key == pygame.K_y:
                        eventg.append("y_pressed")
                    elif event.key == pygame.K_u:
                        eventg.append("u_pressed")
                    elif event.key == pygame.K_o:
                        eventg.append("o_pressed")
                    elif event.key == pygame.K_p:
                        eventg.append("p_pressed")
                    elif event.key == pygame.K_a:
                        eventg.append("a_pressed")
                    elif event.key == pygame.K_s:
                        eventg.append("s_pressed")
                    elif event.key == pygame.K_d:
                        eventg.append("d_pressed")
                    elif event.key == pygame.K_f:
                        eventg.append("f_pressed")
                    elif event.key == pygame.K_g:
                        eventg.append("g_pressed")
                    elif event.key == pygame.K_h:
                        eventg.append("h_pressed")
                    elif event.key == pygame.K_j:
                        eventg.append("j_pressed")
                    elif event.key == pygame.K_k:
                        eventg.append("k_pressed")
                    elif event.key == pygame.K_l:
                        eventg.append("l_pressed")
                    elif event.key == pygame.K_z:
                        eventg.append("z_pressed")
                    elif event.key == pygame.K_x:
                        eventg.append("x_pressed")
                    elif event.key == pygame.K_c:
                        eventg.append("c_pressed")
                    elif event.key == pygame.K_v:
                        eventg.append("v_pressed")
                    elif event.key == pygame.K_b:
                        eventg.append("b_pressed")
                    elif event.key == pygame.K_n:
                        eventg.append("n_pressed")
                    elif event.key == pygame.K_m:
                        eventg.append("m_pressed")
                    elif event.key == pygame.K_BACKSPACE:
                        eventg.append("backspace_pressed")
                    elif event.key == pygame.K_SPACE:
                        eventg.append("space_pressed")
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    eventg.append(mouse_dict[event.button])
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            mouse_position = pygame.mouse.get_pos()
            for x in self.current_scene.character_list:
                x.update(eventg, mouse_position, self)
            for x in self.current_scene.delete_object_list:
                self.current_scene.object_list.remove(x)
            self.current_scene.delete_object_list = []
            for x in self.current_scene.object_list:
                x.update(eventg, mouse_position, self)
            if not self.current_scene.auto_lightining:
                temp_surface = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
                temp_surface.fill((0, 0, 0, 255))
                for x in self.current_scene.scene_lights:
                    x.lighting(temp_surface)
                self.display.blit(temp_surface.convert_alpha(), (0, 0))
            self.scene_controller.update(eventx, eventg, mouse_position, self)
            if "keyboard_used" in eventg:
                eventg.remove("keyboard_used")
            pygame.display.flip()
