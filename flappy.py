import sys, pygame

pygame.init()
screen = pygame.display.set_mode((576, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load("background.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)
bird_surface = pygame.image.load("bird.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 400))

gravity = 0.20
bird_movement = 0

while True:
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

    pygame.display.update()
    clock.tick(60)