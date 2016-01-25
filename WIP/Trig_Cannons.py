import sys, pygame, math
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)
brown = (139, 69, 19)
darkgrey = (128, 128, 128)

bgcolor = white

windowWidth = 640
windowHeight = 480
fps = 30

pygame.init()
fpsClock = pygame.time.Clock()
displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Trig Pointer')

cannonSurf = pygame.Surface((100, 100))
cannonSurf.fill(bgcolor)

pygame.draw.circle(cannonSurf, darkgrey, (20, 50), 20)
pygame.draw.circle(cannonSurf, darkgrey, (80, 50), 20)
pygame.draw.rect(cannonSurf, darkgrey, (20, 30, 60, 40))
pygame.draw.circle(cannonSurf, black, (80, 50), 15)
pygame.draw.circle(cannonSurf, black, (80, 50), 20, 1)
pygame.draw.circle(cannonSurf, brown, (30, 70), 20)
pygame.draw.circle(cannonSurf, black, (30, 70), 20, 1)

def getAngle(x1, y1, x2, y2):
    rise = y1 - y2
    run = x1 - x2
    angle = math.atan2(run, rise)
    angle = angle * (180 / math.pi)
    angle = (angle + 90) % 360
    return angle

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    displaySurf.fill(bgcolor)

    mousex, mousey = pygame.mouse.get_pos()
    for cannonx, cannony in ((200, 150), (50, 300), (50, 50), (200, 400)):
        degrees = getAngle(cannonx, cannony, mousex, mousey)
        rotatedSurf = pygame.transform.rotate(cannonSurf, degrees)
        rotatedRect = rotatedSurf.get_rect()
        rotatedRect.center = (cannonx, cannony)
        displaySurf.blit(rotatedSurf, rotatedRect)

    pygame.draw.line(displaySurf, black, (mousex - 10, mousey), (mousex + 10, mousey))
    pygame.draw.line(displaySurf, black, (mousex, mousey - 10), (mousex, mousey + 10))
    pygame.draw.rect(displaySurf, black, (0, 0, windowWidth, windowHeight), 1)

    pygame.display.update()
    fpsClock.tick(fps)