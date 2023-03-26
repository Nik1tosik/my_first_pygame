import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480)) #flags=pygame.NOFRAME
pygame.display.set_caption("First pygame")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

square = pygame.Surface((64, 64))
square.fill('White')

running = True
while running:

    pygame.draw.circle(screen, 'Red', (320, 240), 5)
    screen.blit(square, (0, 0))

    pygame.display.update()
    screen.fill((146, 156, 148))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()