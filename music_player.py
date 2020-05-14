import atexit
import sys

import pygame
import home
import climate
import car_info
import gps

pygame.init()

width = 400
height = 640

music_display = pygame.display.set_mode((width, height))
background = pygame.image.load('homebackground.png').convert()
pygame.display.set_caption('Music')

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
dark_blue = (0, 30, 71)
pink = (180, 140, 145)
grey = (200, 200, 200)


def round_rect(surf, rect, rad, color, thick=0):
    trans = (255, 255, 0)
    if not rad:
        pygame.draw.rect(surf, color, rect, thick)
        return
    elif rad > rect.width / 2 or rad > rect.height / 2:
        rad = min(rect.width / 2, rect.height / 2)

    if thick > 0:
        r = rect.copy()
        x, r.x = r.x, 0
        y, r.y = r.y, 0
        buf = pygame.surface.Surface((rect.width, rect.height)).convert()
        buf.set_colorkey(trans)
        buf.fill(trans)
        round_rect(buf, r, rad, color, 0)
        r = r.inflate(-thick * 2, -thick * 2)
        round_rect(buf, r, rad, trans, 0)
        surf.blit(buf, (x, y))


    else:
        r = rect.inflate(-rad * 2, -rad * 2)
        for corn in (r.topleft, r.topright, r.bottomleft, r.bottomright):
            pygame.draw.circle(surf, color, corn, rad)
        pygame.draw.rect(surf, color, r.inflate(rad * 2, 0))
        pygame.draw.rect(surf, color, r.inflate(0, rad * 2))

    music_icon = pygame.image.load('music.png').convert_alpha()
    music_icon = pygame.transform.scale(music_icon, (width//12, width//12))
    music_display.blit(music_icon, (width*0.1, height*0.92))

    fan_icon = pygame.image.load('fan.png').convert_alpha()
    fan_icon = pygame.transform.scale(fan_icon, (width//12, width//12))
    music_display.blit(fan_icon, (width *0.28, height*0.92))

    car_icon = pygame.image.load('car.png').convert_alpha()
    car_icon = pygame.transform.scale(car_icon, (width//12, width//12))
    music_display.blit(car_icon, (width*0.63, height*0.92))

    map_icon = pygame.image.load('map.png').convert_alpha()
    map_icon = pygame.transform.scale(map_icon, (width//12, width//12))
    music_display.blit(map_icon, (width *0.816, height * 0.92))

    pygame.draw.circle(surf, grey, (int(width / 2), int(height * 0.95)), width//24)



def add_bar_buttons():
    check_music = home.button(width*0.1, height*0.92, width//12, width//12)
    check_climate = home.button(width *0.28, height*0.92, width//12, width//12)
    check_car = home.button(width*0.63, height*0.92, width//12, width//12)
    check_map = home.button(width *0.816, height * 0.92, width//12, width//12)
    check_home = home.button(width / 2 - width // 24, height * 0.95 - width // 24, width // 12, width // 12)
    pygame.display.update()
    if check_music:
        return 1
    if check_climate:
        return 2
    if check_car:
        return 3
    if check_map:
        return 4
    if check_home:
        return 5
    return 0


def music():
    run_music = True
    while run_music:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        music_display.blit(background, (0, 0))

        round_rect(music_display, pygame.Rect(0, height * .9, width, height * 0.1), 20, (0, 51, 61))
        # show_time()
        check_pressed = add_bar_buttons()
        if check_pressed != 0:
            atexit.register(home.switch_screen(check_pressed))
            sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    music()