import os
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
done = False
pygame.display.set_caption('MP3-player :)')

music_directory = r'C:\Users\Ali\Desktop\music1'

music_files = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if file.endswith('.mp3')]

current_song_index = 0

pygame.mixer.music.load(music_files[current_song_index])

while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.circle(screen, 'white', (200, 75), 20)  # Up
    pygame.draw.circle(screen, 'white', (200, 125), 20)  # Down
    pygame.draw.circle(screen, 'white', (160, 100), 20)  # Left
    pygame.draw.circle(screen, 'white', (240, 100), 20)  # Right

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pygame.mixer.music.play(current_song_index)
        pygame.draw.circle(screen, 'gray', (200, 75), 20)
    if pressed[pygame.K_DOWN]:
        pygame.mixer.music.stop()
        pygame.draw.circle(screen, 'gray', (200, 125), 20)
    if pressed[pygame.K_LEFT]:
        if current_song_index - 1 < 0:
            current_song_index = 0
            pygame.mixer.music.load(music_files[current_song_index])
        else:
            current_song_index = (current_song_index - 1) % len(music_files)
            pygame.mixer.music.load(music_files[current_song_index])
        pygame.mixer.music.play()
        pygame.draw.circle(screen, 'gray', (160, 100), 20)
    if pressed[pygame.K_RIGHT]:
        current_song_index = (current_song_index + 1) % len(music_files)
        pygame.mixer.music.load(music_files[current_song_index])
        pygame.mixer.music.play()
        pygame.draw.circle(screen, 'gray', (240, 100), 20)
    pygame.display.flip()

pygame.quit()