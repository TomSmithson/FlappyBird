import sys, pygame

pygame.init()

height = 320
width = 240
black = 0, 0, 0

screen = pygame.display.set_mode((height, width))
ball = pygame.image.load("oie_oie_canvas.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        ballrect = ballrect.move([2, 2])
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()