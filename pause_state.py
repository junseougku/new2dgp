import game_framework
from pico2d import *

import main_state
name = "PauseState"
image = None

coolTime = 0

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()

def pause():
    pass

def resume():
    pass

def draw():
    global coolTime
    clear_canvas()
    main_state.draw()
    if (coolTime < 70):
        image.draw(400, 300)
    update_canvas()

def update():
    global coolTime
    coolTime = (coolTime + 1) % 100
