import game_framework
import random
from pico2d import *
from math import *

import game_world

timer = get_time()

# Ghost Rotation Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30cm
RADIAN_M = 3
RADIAN_P = RADIAN_M * PIXEL_PER_METER
ANGLE_PER_SECOND = 720

# Ghost Clone Speed
CLONGE_ANGLE_PER_SECOND = radians(45)



class Ghost:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.image.opacify(0.5)
        self.angle = 270
        self.clone_angle = radians(90)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.isClone = True

    def clone(self):
        if self.isClone:
            if (self.clone_angle < 0):
                self.isClone = False

            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, self.clone_angle, '', self.x - 25,
                                           self.y - 25, 100, 100)
            self.clone_angle -= CLONGE_ANGLE_PER_SECOND * game_framework.frame_time


    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, 800 + (RADIAN_P * cos(radians(self.angle))), 300 + (RADIAN_P * sin(radians(self.angle))))
        self.angle += ANGLE_PER_SECOND * game_framework.frame_time
        self.image.opacify(random.random())


    def handle_event(self, event):
        pass
