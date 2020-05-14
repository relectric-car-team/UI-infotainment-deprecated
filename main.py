from home import *
from climate2 import *


run_home = True
run_climate = False
run_navigation = False
run_music = False
run_car = False


def add_bar():
    button()


def button(x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()