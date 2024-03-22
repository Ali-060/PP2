import pygame

pygame.init()
x = 1080
y = 720
rad = 25
moving = 20
a = x / 2 - rad
b = y / 2 - rad
screenshot = pygame.display.set_mode((x, y))


itsrunning = True
clock = pygame.time.Clock()
while itsrunning:
    pygame.display.update()
    screenshot.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and 0 < a - moving < x:
        a -= moving
    elif keys[pygame.K_RIGHT] and 0 < a + moving < x:
        a += moving
    elif keys[pygame.K_UP] and 0 < b - moving < y:
        b -= moving
    elif keys[pygame.K_DOWN] and 0 < b + moving < y:
        b += moving

    if 0 < a < x and 0 < b < y:
        sharik = pygame.draw.circle(screenshot, 'White', (a, b), rad)
    
    pygame.display.update()
    
    pygame.display.flip()
    clock.tick(30)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            itsrunning = False
            pygame.quit()
