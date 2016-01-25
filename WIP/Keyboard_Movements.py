import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

def draw_stick_figure(screen, x, y):
    #Head
    pygame.draw.ellipse(screen, black, [1+x, y, 10, 10], 0)

    #Legs
    pygame.draw.line(screen, black, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, black, [5+x, 17+y], [x, 27+y], 2)

    #Body
    pygame.draw.line(screen, red, [5+x, 17+y], [5+x, 7+y], 2)

    #Arms
    pygame.draw.line(screen, red, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, red, [5+x, 7+y], [1+x, 17+y], 2)

pygame.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
background_image = pygame.image.load("C:/Users/Jon Logsdon/Scripts/PY GAMES/test_background.gif").convert()
background_position = [0, 0]

done = False
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

#-------Main Program Loop ----------
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    screen.fill(white)
    draw_stick_figure(screen, x_coord, y_coord)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
