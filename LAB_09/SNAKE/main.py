import pygame
import random

pygame.init()

''' CONTROLLERS
K_UP, DOWN, LEFT, RIGHT   for movement
K_p                       for play again
K_ESCAPE                  for quit
'''

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
orange = (135, 83, 20)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

screen = pygame.display.set_mode((dis_width, dis_height))

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15  # FPS
font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 35)

def Your_score(score):
    value = score_font.render("Length: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, orange, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_width / 2 - 30, dis_height / 2 - 20])

def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    timer = 0

    level = 1
    score = 0

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("You Lost!", (200, 34, 53))
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()
        # Food timer
        timer = timer + 1
        if timer == 100:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            timer = 0

        # Eating food
        if x1 == foodx and y1 == foody:
            timer = 0
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

        # Controle speed and level
            if score % level == 0:  
                snake_speed += 2
                score = 0
                level += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()