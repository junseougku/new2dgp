from pico2d import *
import random
KPU_WIDTH = 800
KPU_HEIGHT = 600

open_canvas(KPU_WIDTH , KPU_HEIGHT)

ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
running = True

def handle_events():
      global running
      events = get_events()
      for event in events:
          if event.type == SDL_QUIT:
              running = False
          elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
              running = False

x =KPU_WIDTH//2
y = KPU_HEIGHT//2
px = KPU_WIDTH//2
py = KPU_HEIGHT//2
llist = [px,py]

def draw_picture(r):
    for i in range(count):
        character.clip_draw(r * 100, 100, 100, 100, llist[0], llist[1])

tx = 0
ty = 0
count = 0
def draw_curve_5_points(p1, p2,p3,p4,p5):#좌우때문에받음
    global px
    global py
    global frame
    global tx
    global ty
    global count
    global llist
    r = 0
    for i in range(0,50,2):
        clear_canvas() 
        ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        px  = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        py = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        character.clip_draw(frame * 100, 100, 100, 100, px, py)
        draw_picture(5)
        update_canvas()
        handle_events()
        delay(0.05)
        frame = (frame + 1) % 8
    llist = [px,py]
    count += 1

    for i in range(0, 100, 2):
        clear_canvas()
        ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        px = ((-t ** 3 + 2 * t**2 -t) * p1[0] + (3 * t ** 3 - 5 * t**2+2) * p2[0] + (-3 * t ** 3 + 4*t**2+t) * p3[0] +
              (t**3-t**2)*p4[0])/2
        py = ((-t ** 3 + 2 * t**2 -t) * p1[1] + (3 * t ** 3 - 5 * t**2+2) * p2[1] + (-3 * t ** 3 + 4*t**2+t) * p3[1] +
              (t**3-t**2)*p4[1])/2
        character.clip_draw(frame * 100, 100, 100, 100, px, py)
        draw_picture(5)
        update_canvas()
        handle_events()
        delay(0.05)
        frame = (frame + 1) % 8
    llist = [px, py]
    count += 1
    for i in range(0, 100, 2):
        clear_canvas()
        ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[0] +
              (t ** 3 - t ** 2) * p5[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] +
              (t ** 3 - t ** 2) * p5[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, px, py)
        draw_picture(5)
        update_canvas()
        handle_events()
        delay(0.05)
        frame = (frame + 1) % 8
    llist= [px, py]

    count += 1

    for i in range(50,100,2):
        clear_canvas()
        ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        px  = (2*t**2-3*t+1)*p3[0]+(-4*t**2+4*t)*p4[0]+(2*t**2-t)*p5[0]
        py = (2 * t ** 2 - 3 * t + 1) * p3[1] + (-4 * t ** 2 + 4 * t) * p4[1] + (2 * t ** 2 - t) * p5[1]
        character.clip_draw(frame * 100, 100, 100, 100, px, py)
        draw_picture(5)
        update_canvas()
        handle_events()
        delay(0.05)
        frame = (frame + 1) % 8
    llist = [px, py]
    count += 1

size = 10
points = [(random.randint(0,KPU_WIDTH),random.randint(0,KPU_HEIGHT)) for i in range(size)]
frame = 0

n = 1
while running:

    draw_curve_5_points(points[n],points[n-1],points[n-2],points[n-3],points[n-4])
    n = (n + 1) % size
    points[n] = [px,py]
    handle_events()

