import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
done = False

clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = 20
start_time = 90

#-------------- Main Program Loop --------------
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time: {0:02}:{1:02}".format(minutes,seconds)

    text = font.render(output_string, True, black)
    screen.blit(text, [250, 250])

    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time left: {0:02}:{1:02}".format(minutes,seconds)

    text = font.render(output_string, True, black)
    screen.blit(text, [250, 280])
    frame_count += 1
    clock.tick(frame_rate)

    pygame.display.flip()

pygame.quit()