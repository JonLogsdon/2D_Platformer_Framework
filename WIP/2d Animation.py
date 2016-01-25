import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    frame = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,9):
            img = pygame.image.load("C:/Users/Jon Logsdon/Scripts/PY GAMES/cat_walk.jpg").convert()
            img.set_colorkey(white)
            self.images.append(img)

        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.y += self.change_y
        self.rect.x += self.change_x

        if self.change_x < 0:
            self.frame += 1
            if self.frame > 3 * 4:
                self.frame = 0

        self.image = self.images[self.frame // 4]

        if self.change_x > 0:
            self.frame += 1
            if self.frame > 3 * 4:
                self.frame = 0
            self.image = self.images[self.frame // 4+4]

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
all_sprites_list = pygame.sprite.Group()

player = Player()
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()
score = 0

#-------- Main Program Loop ------------
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, -3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, 3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    screen.fill(white)
    player.update()
    all_sprites_list.draw(screen)
    clock.tick(20)
    pygame.display.flip()

pygame.quit()
        