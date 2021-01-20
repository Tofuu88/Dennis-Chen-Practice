import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)

pygame.mixer.init()
pygame.init()

# Sprite object for Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()  # this superclass inherits the behavior of Sprite
        self.surf = pygame.image.load('jet.png').convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()  # get a rectangular area

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # add some control logic here to keep self.rect inside the SCREEN_WIDTH, SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load('missile.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):  # update the position of the enemy sprite rect based on speed
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load('cloud.png').convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)  #  The RLEACCEL constant is an optional parameter that helps pygame render more quickly on non-accelerated displays
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # this returns the surface object to be processed later

# custom events
add_enemy = pygame.USEREVENT + 1  # the last event pygame reserves is USEREVENT, so + 1 makes add_enemy unique???
pygame.time.set_timer(add_enemy, 250)  # every 250 miliseconds.  pygame.time fires add_enemy at 250 miliseconds rate

add_cloud = pygame.USEREVENT + 2
pygame.time.set_timer(add_cloud, 500)  # every second it's added


# create a player object (instance of Player)
player = Player()

# sprite group creation  
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# pygame event system handles user input within the gameloop
# events are user inputs which are placed in event queues and event handler handles them
# event also have types, which I think are essentially different types of user inputs
# keydown is an event type with a variable key to define which key on keyboard generates the event keydown

# event queues are accessed via pygame.event.get()
clock = pygame.time.Clock()

pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == add_enemy:
            new_enemy = Enemy()
            enemies.add(new_enemy)  # the sprite group is added with a new enemy instance of the Enemy class
            all_sprites.add(new_enemy)  # why is this needed?

        elif event.type == add_cloud:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    screen.fill((135, 206, 250))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()  # update enemy position
    clouds.update()  # update cloud every loop 
    
    # create a surf object
    surf = pygame.Surface((50, 50))  # a surface object is 50 pixel by 50 pixel
    surf.fill((125, 125, 125))  # fill it black
    rect = surf.get_rect()

    surf_center = ((SCREEN_WIDTH - surf.get_width()) / 2, (SCREEN_HEIGHT - surf.get_height()) / 2)
    player_location = (0, (SCREEN_HEIGHT - player.surf.get_height())/2)
    # block transfer putting surface onto another surface
    # screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))  # this only puts the top corner of the surface object
    # screen.blit(surf, surf_center)  # this copies surface onto the screen, at exactly the center of the screen
    # screen.blit(player.surf, player.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        running = False

    pygame.display.flip()

    clock.tick(60)  # this is 60 FPS limits per loop

pygame.mixer.music.stop()
pygame.mixer.quit()
    # To do this, .tick() calculates the number of milliseconds each frame should take, 
    # based on the desired frame rate. Then, it compares that number to the number of milliseconds 
    # that have passed since the last time .tick() was called. If not enough time has passed, then .tick() 
    # delays processing to ensure that it never exceeds the specified frame rate


