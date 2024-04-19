import pygame
import math

pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BRUSH_SIZE = 10
ERASER_SIZE = 20

current_color = BLACK

# Function to draw a rectangle
def draw_rect(surface, color, start_pos, end_pos):
    pygame.draw.rect(surface, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))

# Function to draw a circle
def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

# Function to draw a square
def draw_square(surface, color, top_left, side_length):
    pygame.draw.rect(surface, color, pygame.Rect(top_left, (side_length, side_length)))

# Function to draw a right triangle
def draw_right_triangle(surface, color, top_left, base, height):
    points = [top_left, (top_left[0] + base, top_left[1]), (top_left[0], top_left[1] + height)]
    pygame.draw.polygon(surface, color, points)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(surface, color, top_point, side_length):
    height = int(side_length * (3 ** 0.5) / 2)
    points = [top_point, (top_point[0] + side_length, top_point[1]), ((top_point[0] + side_length) / 2, top_point[1] + height)]
    pygame.draw.polygon(surface, color, points)

# Function to draw a rhombus
def draw_rhombus(surface, color, top_left, width, height):
    points = [top_left, (top_left[0] + width / 2, top_left[1] + height / 2), (top_left[0] + width, top_left[1]), (top_left[0] + width / 2, top_left[1] - height / 2)]
    pygame.draw.polygon(surface, color, points)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Paint")

# Variables to track mouse button state and drawing mode
left_button_pressed = False
right_button_pressed = False
drawing_mode = "brush"
start_pos = (0, 0)

screen.fill(WHITE)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                left_button_pressed = True
                start_pos = event.pos
            elif event.button == 3:  # Right mouse button
                right_button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_button_pressed = False
            elif event.button == 3:
                right_button_pressed = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # R - draw rectangle
                drawing_mode = "rect"
            elif event.key == pygame.K_c:  # C - draw circle
                drawing_mode = "circle"
            elif event.key == pygame.K_e:  # E - use eraser
                drawing_mode = "eraser"
            elif event.key == pygame.K_b:  # B - select brush
                drawing_mode = "brush"
            elif event.key == pygame.K_t:  # T - draw right triangle
                drawing_mode = "right_triangle"
            elif event.key == pygame.K_q:  # Q - draw equilateral triangle
                drawing_mode = "equilateral_triangle"
            elif event.key == pygame.K_r:  # R - draw rhombus
                drawing_mode = "rhombus"
            elif event.key == pygame.K_k:  # K - select black color
                current_color = BLACK
            elif event.key == pygame.K_w:  # W - select white color
                current_color = WHITE
            elif event.key == pygame.K_r:  # R - select red color
                current_color = RED
            elif event.key == pygame.K_g:  # G - select green color
                current_color = GREEN
            elif event.key == pygame.K_l:  # B - select blue color
                current_color = BLUE

    # Drawing
    if left_button_pressed or right_button_pressed:
        if drawing_mode == "brush":
            if left_button_pressed:
                pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), BRUSH_SIZE)
            elif right_button_pressed:
                pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), BRUSH_SIZE * 5)
        elif drawing_mode == "rect":
            if left_button_pressed:
                draw_rect(screen, current_color, start_pos, pygame.mouse.get_pos())
        elif drawing_mode == "circle":
            if left_button_pressed:
                radius = ((pygame.mouse.get_pos()[0] - start_pos[0]) ** 2 + (pygame.mouse.get_pos()[1] - start_pos[1]) ** 2) ** 0.5
                draw_circle(screen, current_color, start_pos, int(radius))
        elif drawing_mode == "eraser":
            if left_button_pressed:
                pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), ERASER_SIZE)
        elif drawing_mode == "right_triangle":
            if left_button_pressed:
                draw_right_triangle(screen, current_color, start_pos, 100, 150)
        elif drawing_mode == "equilateral_triangle":
            if left_button_pressed:
                if drawing_mode == "equilateral_triangle":
                    side_length = ((pygame.mouse.get_pos()[0] - start_pos[0]) ** 2 + (pygame.mouse.get_pos()[1] - start_pos[1]) ** 2) ** 0.5
                    height = int(side_length * (3 ** 0.5) / 2)
                    dx = pygame.mouse.get_pos()[0] - start_pos[0]
                    dy = pygame.mouse.get_pos()[1] - start_pos[1]
                    angle = math.atan2(dy, dx)
                    top_point = (start_pos[0] + side_length / 2 * math.cos(angle),
                    start_pos[1] - side_length / 2 * math.sin(angle) - height)
                    draw_equilateral_triangle(screen, current_color, top_point, side_length)
                
        elif drawing_mode == "rhombus":
            if left_button_pressed:
                draw_rhombus(screen, current_color, start_pos, 150, 100) 
    clock.tick(240)
    pygame.display.flip()
pygame.quit()