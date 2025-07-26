import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

PURPLE = pygame.color('purple')
GREEN = pygame.color('green')
YELLOW = pygame.color('yellow')

RED = pygame.color('red')
WHITE = pygame.color('white')
BLUE = pygame.color('blue')
ORANGE = pygame.color('orange')

class Sprite(pygame.sprite.sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1])], random.choice([-1, 1])



    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >=500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit =True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_color(self):
        self.image.fill(random.choice([RED, WHITE, BLUE, ORANGE]))
def change_background_color():
    global bg_color
    bg_color = random.choice([PURPLE, GREEN, YELLOW]) 


all_sprites_list = pygame.sprite.Group()
sp1=Sprite(20,40,WHITE)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

sp2=Sprite(30,40,RED)
sp2.rect.x = random.randint(0, 480)
sp2.rect.y = random.randint(0, 370)
all_sprites_list.add(sp2)

sp3=Sprite(30,40,YELLOW)
sp3.rect.x = random.randint(0, 480)
sp3.rect.y = random.randint(0, 370)
all_sprites_list.add(sp3)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_captio('Randomise GAME')
bg_color = BLUE
screen.fill(bg_color)

exit_game = False
clock = pygame.time.clock()
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)


pygame.quit()        