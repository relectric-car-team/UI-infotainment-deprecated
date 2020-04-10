import pygame

pygame.init()
climateRun = True

width = 1280
height = 720

climate_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Climate')

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
dark_blue = (0, 30, 71)
pink = (180, 140, 145)

background = pygame.image.load('background1.jpg').convert()

temp_left = 20
temp_right = 20
temp_max = 25
temp_min = 18


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def button(text, x, y, width, height, colour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(climate_display, colour, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(climate_display, colour, (x, y, width, height))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((x +(width / 2)), (y + (height/2)))
    climate_display.blit(TextSurf, TextRect)


def regular_button():
    print("Clicked a button.")


def temp_up_right():
    global temp_right
    global temp_max
    if temp_right < temp_max:
        temp_right += 1
    else:
        temp_right = temp_max


def temp_up_left():
    global temp_left
    global temp_max
    if temp_left < temp_max:
        temp_left += 1
    else:
        temp_left = temp_max


def temp_down_right():
    global temp_right
    global temp_min
    if temp_right > temp_min:
        temp_right -= 1
    else:
        temp_right = temp_min


def temp_down_left():
    global temp_left
    global temp_min
    if temp_left > temp_min:
        temp_left -= 1
    else:
        temp_left = temp_min


def show_title():
    font = pygame.font.SysFont(None, 120)
    text = "Relectric"
    title = font.render(text, True, green)
    climate_display.blit(title, (width/2-150, 40, 50, 50))


def show_temp():
    global temp_left
    global temp_right
    font = pygame.font.SysFont(None, 100)
    left_temp = font.render(str(temp_left), True, white)
    right_temp = font.render(str(temp_right), True, white)
    climate_display.blit(left_temp, ((width / 2) - 100, height / 2 - 130, 50, 50))
    climate_display.blit(right_temp, ((width / 2 + 100), height / 2 - 130, 50, 50))


def add_buttons():
    button("1", 33, height - 200, 150, 150, black, regular_button)
    button("2", (width / 5) + 33, height - 200, 150, 150, black, regular_button)
    button("3", (width / 5) * 2 + 33, height - 200, 150, 150, black, regular_button)
    button("4", (width / 5) * 3 + 33, height - 200, 150, 150, black, regular_button)
    button("5", (width / 5) * 4 + 33, height - 200, 150, 150, black, regular_button)
    button("Up", (width / 2) - 300, height / 2 - 180, 75, 75, black, temp_up_left)
    button("Down", (width / 2) - 300, height / 2 - 80, 75, 75, black, temp_down_left)
    button("Up", (width / 2) + 300, height / 2 - 180, 75, 75, black, temp_up_right)
    button("Down", (width / 2) + 300, height / 2 - 80, 75, 75, black, temp_down_right)

    pygame.display.update()


def climate():

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        climate_display.fill(white)
        climate_display.blit(background, (0, 0))
        show_temp()
        add_buttons()
        show_title()

        pygame.display.update()

climate()
