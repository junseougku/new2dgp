import random
from pico2d import *
import game_world
import game_framework
import main_state
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint (100,1500-1), 0
        self.velocity = 0
    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x_velocity = main_state.boy.x_velocity
        self.y_velocity = main_state.boy.y_velocity
        self.y -= self.y_velocity * game_framework.frame_time
        self.x -= self.x_velocity * game_framework.frame_time

