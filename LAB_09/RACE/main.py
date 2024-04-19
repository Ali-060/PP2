import pygame
import datetime
import random
import math

pygame.init()
clock = pygame.time.Clock()
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_icon(pygame.image.load(r'LAB_09/RACE/images/icon.png'))
pygame.display.set_caption("Crazy Racing")

car = [
    pygame.image.load(r'LAB_09/RACE/images/car1.png'), 
    pygame.image.load(r'LAB_09/RACE/images/car2.png'),
]
car = [
    pygame.transform.scale(car[0], (85, 160)),
    pygame.transform.scale(car[1], (85, 165))
]

coin = pygame.image.load(r'LAB_09/RACE/images/coin.png')
coin = pygame.transform.scale(coin, (70, 70))

road = pygame.image.load(r'LAB_09/RACE/images/road.png')
road = pygame.transform.scale(road, (700, 700))

dark = pygame.image.load(r'LAB_09/RACE/images/dark.png')
dark = pygame.transform.scale(dark, (WIDTH, HEIGHT))

road_spawn_1 = 0
road_spawn_2 = -HEIGHT

speed = 4
car_spawn_point = [360, 530]

car_W = 350
car_H = 600
car_y = coin_y = -100

car1_width, car1_height = 75, 160
car2_width, car2_height = 75, 165

value = 0
font = pygame.font.Font(None, 70)
font_score = pygame.font.Font(None, 40)
text = font.render(f'{value}', True, (255,255,255))
text_rect = text.get_rect()

running = True
while running:
    pygame.display.update()

    if car_y == -100:
        car_spawn = random.choice(car_spawn_point)
    if coin_y == -100:
        coin_spawn = random.choice(car_spawn_point)

    keys = pygame.key.get_pressed()
    screen.fill((70,200,80))

    coin1 = pygame.Rect(coin_spawn, coin_y, 70, 70)
    car1 = pygame.Rect(car_W, car_H, 75, 160)
    car2 = pygame.Rect(car_spawn, car_y, 75, 160)

    if car1.colliderect(coin1):
        coin_spawn = -100
        value += 100
        speed += 0.1

    if running:
        road_spawn_1 = (road_spawn_1 + 2)%HEIGHT
        road_spawn_2 = (road_spawn_2 + 2)%HEIGHT - HEIGHT
        screen.blit(road, (150,road_spawn_1))
        screen.blit(road, (150,road_spawn_2))

    if keys[pygame.K_w] and car_H - speed >= 0:
        car_H -= speed
    if keys[pygame.K_s] and car_H + speed <= 600:
        car_H += speed
    if keys[pygame.K_a] and car_W - speed >= 333:
        car_W -= speed
    if keys[pygame.K_d] and car_W + speed <= 580:
        car_W += speed
    else:
        car_H += (speed/4)    

    screen.blit(road, (150,road_spawn_1))
    screen.blit(road, (150,road_spawn_2))
    screen.blit(car[0], (car_W, car_H))

    screen.blit(coin, (coin_spawn, coin_y))

    screen.blit(car[1], (car_spawn, car_y))

    text = font.render(f'{value} KZT', True, (255,255,255))
    screen.blit(text, text_rect)

    if car1.colliderect(car2) or car_H > HEIGHT:
        text_end = font.render(f'YOU LOSE', True, (255,255,255))
        text_score = font_score.render(f'Total: {value} KZT (#P.S. this value is not real ;) )', True, (255,255,255))
        speed = 0
        road_spawn_1 = road_spawn_2 = 0
        screen.blit(dark, (0,0))
        screen.blit(text_end, (WIDTH/2 - 130,HEIGHT/2 - 40))
        screen.blit(text_score, (10,HEIGHT - 50))
        
    car_y += speed * 1.5
    if car_y > HEIGHT:
        car_y = -100
    coin_y += speed
    if coin_y > HEIGHT:
        coin_y = -100

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
