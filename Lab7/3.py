import pygame
import sys

# Инициализация Pygame и микшера
pygame.init()
pygame.mixer.init()

# Настройка экрана
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Simple Music Player")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифты
font = pygame.font.Font(None, 36)

# Музыкальные треки
tracks = [
    "Lab7/music/track1.mp3",
    "Lab7/music/track2.mp3",
    "Lab7/music/track3.mp3"
]
track_names = ["Track 1", "Track 2", "Track 3"]  # Названия треков
current_index = 0

# Функция для воспроизведения трека
def play_track(index):
    pygame.mixer.music.load(tracks[index])
    pygame.mixer.music.play()

play_track(current_index)

running = True
while running:
    screen.fill(WHITE)  # Очищаем экран
    
    # Отображаем название трека
    track_text = font.render(f"Now Playing: {track_names[current_index]}", True, BLACK)
    screen.blit(track_text, (20, 50))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
            # P = Play 
            if event.key == pygame.K_p:
                play_track(current_index)
            
            # S = Stop
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            
            # N = Next 
            if event.key == pygame.K_n:
                current_index = (current_index + 1) % len(tracks)
                play_track(current_index)
            
            # B = Back 
            if event.key == pygame.K_b:
                current_index = (current_index - 1) % len(tracks)
                play_track(current_index)

pygame.quit()
sys.exit()