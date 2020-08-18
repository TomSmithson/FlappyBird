import sys, pygame
import random

def check_boundaries():
    if bird_rect.y < -200 or bird_rect.y > 800:
        return False
    return True

def create_pipes():
    pipes = []
    x = 500
    for i in range(0, 100):
        top_y = random.randint(-100, 150)
        bottom_y = random.randint(850, 900)
        pipes.append([x, top_y, bottom_y])
        x += 300
    return pipes

pygame.init()
screen = pygame.display.set_mode((576, 800))
clock = pygame.time.Clock()

startscreen_surface = pygame.image.load("startscreen.png").convert()
startscreen_surface = pygame.transform.scale(startscreen_surface, (576, 820))

endscreen_surface = pygame.image.load("endscreen.png").convert()
endscreen_surface = pygame.transform.scale2x(endscreen_surface)

bg_surface = pygame.image.load("background.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

bird_surface = pygame.image.load("bird.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 400))

pipe_surface = pygame.image.load("pipe3.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)

font = pygame.font.SysFont(None, 40)


def game_loop():
    gravity = 0.20
    bird_movement = 0
    pipes = create_pipes()
    score = 0

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
        text_surface = font.render("Score: {}".format(score), False, (0, 0, 0))

        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)

        pipe_pos = []
        score = 0
        for i in range(0, len(pipes)):
            pipes[i][0] = pipes[i][0] - 2
            if pipes[i][0] < 600:  
                top_pipe = pipe_surface.get_rect(center = (pipes[i][0], pipes[i][1]))
                bottom_pipe = pipe_surface.get_rect(center = (pipes[i][0], pipes[i][2]))
                screen.blit(pipe_surface, top_pipe) 
                screen.blit(pipe_surface, bottom_pipe)
                pipe_pos.append([bottom_pipe, top_pipe])
            if pipes[i][0] < 0:
                del pipe_pos[0]
            if pipes[i][0] < bird_rect.x:
                score+=1

        if pipe_pos[0][0].x - 59 == bird_rect.x or pipe_pos[0][1].x + 59 == bird_rect.x:
            if (pipe_pos[0][1].y + pipe_pos[0][1].h) - bird_rect.y > 0:
                pygame.quit()
                sys.exit()
            elif (bird_rect.y in range(pipe_pos[0][0].y - 50, pipe_pos[0][0].y + 50)):
                pygame.quit()
                sys.exit()

        screen.blit(text_surface, (0, 0))

        pygame.display.update()
        clock.tick(60)

def end_screen(score):
    screen.blit(endscreen_surface, (0, 0))
    text_surface = font.render("{}".format(score), False, (0, 0, 0))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.quit()
    sys.exit()

def main_menu():
    screen.blit(startscreen_surface, (0, 0))
    pygame.display.update()
    start = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True
        if start:
            game_loop()
    pygame.display.update(screen)
    clock.tick(10)

main_menu()