from pico2d import *
import random
class Ball:
    def __init__(self):
        self.x , self.y = random.randint(50,750),599
        self.ball_size = random.randint(0,1)
        if self.ball_size == 0:
            self.image = load_image('ball21x21.png')
        elif self.ball_size == 1:
            self.image = load_image('ball41x41.png')
        self.speed = random.randint(4,10)
    def update(self):
        if self.ball_size == 0:
            if self.y > 60 :
                self.y -= self.speed
        elif self.ball_size == 1:
            if self.y > 75 :
                self.y -= self.speed
    def draw(self):
        self.image.draw(self.x,self.y)
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x , self.y = 0,90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass()
team = [Boy() for i in range(11)]
running = True

balls = [Ball() for i in range(20)]


# game main loop code
while running:
    handle_events()
    boy.update()
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    delay(0.05)
# finalization

close_canvas()