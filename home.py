import sys

import pygame
from datetime import datetime
import music_player
import car_info
import climate
import gps
import atexit

pygame.init()

width = 400
height = 640

home_display = pygame.display.set_mode((width, height))
background = pygame.image.load('homebackground.png').convert()
pygame.display.set_caption('Home')

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
dark_blue = (0, 30, 71)
pink = (180, 140, 145)


def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()


def button(x, y, width, height):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1:
            return True


def add_buttons():
    check_music = button(width / 4, height / 2, width // 6, width // 6)
    check_climate = button(width / 1.75, height / 2, width // 6, width // 6)
    check_car = button(width / 4, height * 2/3, width // 6, width // 6)
    check_map = button(width / 1.75, height * 2 / 3, width // 6, width // 6)
    pygame.display.update()
    if check_music:
        return 1
    if check_climate:
        return 2
    if check_car:
        return 3
    if check_map:
        return 4
    return 0


def show_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    font = pygame.font.SysFont('avenir.ttc', 70)
    text, text_rect = text_objects(current_time, font)
    text_rect.center = (width / 2), (height/5)  # find center of the text
    home_display.blit(text, text_rect)


def show_icons():
    music_icon = pygame.image.load('music.png').convert_alpha()
    music_icon = pygame.transform.scale(music_icon, (width//6, width//6))
    home_display.blit(music_icon, (width/4, height/2))

    fan_icon = pygame.image.load('fan.png').convert_alpha()
    fan_icon = pygame.transform.scale(fan_icon, (width // 6, width // 6))
    home_display.blit(fan_icon, (width / 1.75, height / 2))

    car_icon = pygame.image.load('car.png').convert_alpha()
    car_icon = pygame.transform.scale(car_icon, (width // 6, width // 6))
    home_display.blit(car_icon, (width / 4, height*2/3))

    map_icon = pygame.image.load('map.png').convert_alpha()
    map_icon = pygame.transform.scale(map_icon, (width // 6, width // 6))
    home_display.blit(map_icon, (width / 1.75, height * 2 / 3))


def switch_screen(argument):
    switcher = {
        1: music_player.music,
        2: climate.climate,
        3: car_info.car,
        4: gps.gps,
        5: home
    }
    func = switcher.get(argument)
    func()


def home():
    run_home = True
    while run_home:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        home_display.blit(background, (0, 0))
        show_time()
        show_icons()
        check_pressed = add_buttons()
        if check_pressed != 0:
            atexit.register(switch_screen(check_pressed))
            sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    home()