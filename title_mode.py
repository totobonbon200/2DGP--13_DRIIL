from pico2d import *
import game_framework
import play_mode

image = None


def init():
    global image
    image = load_image('title.png')


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
                return
            elif event.key in (SDLK_SPACE, SDLK_RETURN):
                game_framework.change_mode(play_mode)
                return


def update():
    pass


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def pause():
    pass


def resume():
    pass
