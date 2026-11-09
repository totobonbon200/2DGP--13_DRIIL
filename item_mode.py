from pico2d import get_canvas_height, get_canvas_width, load_image


active = False
image = None


def init():
    global active, image
    if image is None:
        image = load_image('item_select.png')
    active = True


def finish():
    global active
    active = False


def render():
    if active:
        image.draw(get_canvas_width() / 2, get_canvas_height() / 2)
