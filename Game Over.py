import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Game Over Example")

done = False
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5

font = pygame.font.Font(None, 36)
game_over = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            game_over = True

    if game_over == False:
        rect_x += rect_change_x
        rect_y += rect_change_y

        if rect_y > 450 or rect_y < 0:
            rect_change_y = rect_change_y * -1
        if rect_x > 650 or rect_x < 0:
            rect_change_x = rect_change_x * -1

    screen.fill(black)
    pygame.draw.rect(screen, green, [rect_x, rect_y, 50, 50])

    if game_over:
        text = font.render("Game Over", True, white)
        text_rect = text.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y])
    else:
        text = font.render("Click to end game", True, white)
        text_rect = text.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y])

    clock.tick(20)
    pygame.display.flip()
pygame.quit()