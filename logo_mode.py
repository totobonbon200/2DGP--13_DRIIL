import game_framework
from pico2d import *

image = None
running = None
logo_start_time = 0.0

def init():
    global image, logo_start_time

    image = load_image('tuk_credit.png')
    running = True
    logo_start_time = get_time()

def finish():
    global image
    del image

def update():
    global running, logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.quit()

def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    #현재 이벤트들을 소비
    events = get_events()