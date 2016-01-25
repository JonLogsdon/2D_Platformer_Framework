import sys, pygame, math
from pygame.locals import *

brightblue = (0, 50, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
darkred = (128, 0, 0)
yellow = (255, 255, 0)

bgcolor = white

windowWidth = 640
windowHeight = 480
win_centerX = int(windowWidth / 2)
win_centerY = int(windowHeight / 2)

fps = 160
amplitude = 100

pygame.init()
fpsClock = pygame.time.Clock()
displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Trig Circle')

step = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    displaySurf.fill(bgcolor)
    pygame.draw.line(displaySurf, black, (win_centerX, 0), (win_centerX, windowHeight))
    pygame.draw.line(displaySurf, black, (0, win_centerY), (windowWidth, win_centerY))

    xPos = math.cos(step) * amplitude
    yPos = -1 * math.sin(step) * amplitude
    #yPos = -1 * abs(math.sin(step) * amplitude)

    pygame.draw.circle(displaySurf, brightblue, (int(xPos) + win_centerX, int(yPos) + win_centerY), 20)
    pygame.draw.circle(displaySurf, darkred, (windowWidth - 30, int(yPos) + win_centerY), 20)
    pygame.draw.circle(displaySurf, darkred, (int(xPos) + win_centerX, windowHeight - 30), 20)
    pygame.draw.line(displaySurf, yellow, (windowWidth, int(yPos) + win_centerY), (0, int(yPos) + win_centerY))
    pygame.draw.line(displaySurf, yellow, (int(xPos) + win_centerX, windowHeight), (int(xPos) + win_centerX, 0))
    pygame.draw.rect(displaySurf, black, (0, 0, windowWidth, windowHeight), 1)

    pygame.display.update()
    fpsClock.tick(fps)

    step += 0.02
    step %= 2 * math.pi
    