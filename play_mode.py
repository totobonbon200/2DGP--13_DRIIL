from pico2d import *
import game_world
import game_framework
import title_mode
import pause_mode
import item_mode
from boy import Boy
from grass import Grass


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            if item_mode.active:
                item_mode.finish()
            else:
                item_mode.init()
        elif (item_mode.active and event.type == SDL_KEYDOWN and
              event.key == SDLK_0):
            boy.ball_type = 0
            item_mode.finish()
        else:
            boy.handle_event(event)



def init():
    global boy
    item_mode.finish()


    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

def finish():
    item_mode.finish()
    game_world.clear()


def pause():
    global pause_started_at
    pause_started_at = get_time()
    boy.pressed_keys.clear()
    boy.dir = 0
    if boy.state == 'RUN':
        boy.stop_run()


def resume():
    boy.idle_started_at += get_time() - pause_started_at

def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    item_mode.render()
    update_canvas()

running = True
