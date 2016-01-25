import pygame
import random

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(10):
    block = Block(black, 20, 15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprites_list.add(block)

player = Block(red, 20, 15)
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
score = 0
level = 1

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in blocks_hit_list:
        score += 1
        print(score)

    if len(block_list) == 0:
        level += 1
        for i in range(level * 10):
            block = Block(black, 20, 15)
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)

            block_list.add(block)
            all_sprites_list.add(block)

    screen.fill(white)
    all_sprites_list.draw(screen)

    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, [10, 10])

    text = font.render("Level: " + str(level), True, black)
    screen.blit(text, [10, 40])

    clock.tick(20)
    pygame.display.flip()
pygame.quit()
        