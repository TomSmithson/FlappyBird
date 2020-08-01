import sys, pygame
import random
import os
import time


pygame.init()
screen = pygame.display.set_mode((576, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load("background.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

bird_surface = pygame.image.load("bird.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 400))

pipe_surface = pygame.image.load("pipe.png").convert()
# pipe_rect = pipe_surface.get_rect(center = (500, 100))

# pipe_surface2 = pygame.image.load("pipe.png").convert()
# pipe_rect2 = pipe_surface2.get_rect(center = (500, 700))

gravity = 0.20
bird_movement = 0

def check_boundaries():
    if bird_rect.y < -200 or bird_rect.y > 800:
        return False
    return True


def create_pipe():
    x = 500
    top_y = random.randint(50, 200)
    bottom_y = random.randint(500, 700)
    x += 25
    return (x, top_y, bottom_y)


while True:
    pipe_movement = 0
    if not check_boundaries():
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6

    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    # pipe_movement -= 2
    # pipe_rect.centerx += pipe_movement
    # screen.blit(pipe_surface, pipe_rect)

    # pipe_rect2.centerx += pipe_movement
    # screen.blit(pipe_surface2, pipe_rect2)

    (x, top_y, bottom_y) = create_pipe()
    top_pipe = pipe_surface.get_rect(center = (x, top_y))
    bottom_pipe = pipe_surface.get_rect(center = (x, bottom_y))
    pipe_movement -= 2
    top_pipe.centerx += pipe_movement
    bottom_pipe.centerx += pipe_movement

    screen.blit(pipe_surface, top_pipe)
    screen.blit(pipe_surface, bottom_pipe)

    pygame.display.update()
    clock.tick(60)
