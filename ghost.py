import game_framework
import random
from pico2d import *

import math

timer = get_time()

PIXEL_PER_METER = (10.0 / 0.3)
RADIAN_MLN = 3
RADIAN_P = RADIAN_MLN * PIXEL_PER_METER
ANGLE_PER_SECOND = 540

CLONGE_ANGLE_PER_SECOND = math.radians(45)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Ghost:
    def __init__(self,_x,_y):
        self.x, self.y = _x,_y
        self.image = load_image('animation_sheet.png')
        self.image.opacify(0.5)
        self.angle = 270
        self.clone_angle = math.radians(90)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.newghost = True

    def create(self):
        if self.newghost:

            if (self.clone_angle < 0):
                self.newghost = False
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, self.clone_angle, '', self.x - 60,
                                           self.y - 25, 100, 100)
            self.clone_angle -= CLONGE_ANGLE_PER_SECOND * game_framework.frame_time


    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x + (RADIAN_P * math.cos(math.radians(self.angle))), self.y + (RADIAN_P * math.sin(math.radians(self.angle))))
        self.angle += ANGLE_PER_SECOND * game_framework.frame_time
        self.image.opacify(random.random())  


    def handle_event(self, event):
        pass
