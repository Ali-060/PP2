import os
import pygame
import datetime

pygame.init()
pygame.display.set_caption('Mickey Clock :)')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
print(os.getcwd())

Clock = pygame.image.load(os.path.normpath('Clock/mickey.png'))
Clock = pygame.transform.scale(Clock, (500, 500))
img_seconds = pygame.image.load(os.path.normpath('Clock/seconds.png'))
img_seconds = pygame.transform.scale(img_seconds, (150, 400))
img_minute = pygame.image.load(os.path.normpath('Clock/minute.png'))
img_minute = pygame.transform.scale(img_minute, (150, 300))
rect = Clock.get_rect(center=(250, 250))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(Clock, (0, 0))
   
    time = datetime.datetime.now()
    angle_seconds = -(time.second * (360 / 60))
    angle_minute = -(time.minute * (360 / 60))

    minute = pygame.transform.rotate(img_minute, angle_minute)
    minute_rect = minute.get_rect(center=rect.center)
    
    screen.blit(minute, minute_rect.topleft)
    
    seconds = pygame.transform.rotate(img_seconds, angle_seconds)
    seconds_rect = seconds.get_rect(center=rect.center)
    screen.blit(seconds, seconds_rect.topleft)

    clock.tick(1)
    pygame.display.flip()

pygame.quit()