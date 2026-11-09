from ctypes import byref, c_int
from pathlib import Path

from pico2d import *
from sdl2.sdlttf import TTF_CloseFont, TTF_SizeUTF8
import game_framework
import game_world

font = None
text_width = 0
MESSAGE = '- Pause -'


def init():
    global font, text_width
    font = load_font(str(Path(__file__).with_name('pause_font.ttf')), 40)
    width, height = c_int(), c_int()
    TTF_SizeUTF8(font.font, MESSAGE.encode('utf-8'), byref(width), byref(height))
    text_width = width.value


def finish():
    global font
    TTF_CloseFont(font.font)
    font = None


def handle_events():
    for event in get_events():
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    font.draw((get_canvas_width() - text_width) / 2,
              get_canvas_height() / 2, MESSAGE, (255, 0, 0))
    update_canvas()
