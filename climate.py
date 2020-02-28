import pygame

BACKGROUND = (50, 50, 50)
WHITE = (255, 255, 255)
BLUE = (147, 194, 216)
GREY = (200, 200, 200)
DARKBLUE = (0, 30, 71)
BLACK = (0, 0, 0)


pygame.init()                                       # initiates pygame
pygame.font.init()

width = 400
height = 640
screen = pygame.display.set_mode((width, height))   # creates window object and sets the resolution of the window
pygame.display.set_caption('Climate')               # window title
clock = pygame.time.Clock()                         # timing within the window for pygame


font = pygame.font.Font('freesansbold.ttf', 32)

# create a text suface object,
# on which text is drawn on it.


# create a rectangular object for the
# text surface object


# set the center of the rectangular object.



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND)
    #pygame.draw.circle(screen, GREY, (width//2, int(height//2)), int(width//2))
    pygame.draw.polygon(screen, BLUE, [(width//8, height//4), (width//5, height//4), (width/6, height//5)]) # left up button
    pygame.draw.polygon(screen, BLUE, [(width // 8, (height // 4)+10), (width // 5, height // 4+10), (width / 6, height // 5+75)])  # left up button
    pygame.draw.polygon(screen, BLUE, [((width // 8)+250, height // 4), ((width // 4)+235, height // 4),
                                       ((width // 6)+252, height // 5)])  # left up button
    pygame.draw.polygon(screen, BLUE, [((width // 8) + 250, (height // 4)+10), ((width // 4) + 235, (height // 4)+10),
                                       ((width // 6) + 252, (height // 5)+75)])  # left up button

    text = font.render("20", True, WHITE)
    screen.blit(text, [(width / 4), height / 4-5, 50, 50])
    screen.blit(text, [(width / 2+45), height / 4 - 5, 50, 50])

    for i in range (5):
        pygame.draw.rect(screen, BLUE, [(width/6)*i+40, height/2, 50, 50])
        s = str(i+1)
        text = font.render(s, True, BLACK)
        textRect = text.get_rect()
        screen.blit(text, [(width/6)*i+55, height/2+10, 50, 50])
    pygame.draw.rect

    for i in range (3):
        pygame.draw.circle(screen, WHITE, ((width//20)*i+50, height//3+60), 5)
        pygame.draw.circle(screen, WHITE, ((width // 20) * i + 300, height // 3 + 60), 5)
    pygame.display.flip()  # displays the window

pygame.quit()                                       # uninitiates pygame
quit()