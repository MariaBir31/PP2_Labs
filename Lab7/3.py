# import pygame
# import sys

# # Инициализация Pygame и микшера
# pygame.init()
# pygame.mixer.init()

# # Настройка экрана
# WIDTH, HEIGHT = 400, 200
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Super Simple Music Player")

# # Цвета
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Шрифты
# font = pygame.font.Font(None, 36)

# # Музыкальные треки
# tracks = [
#     "Lab7/music/track1.mp3",
#     "Lab7/music/track2.mp3",
#     "Lab7/music/track3.mp3"
# ]
# track_names = ["Track 1", "Track 2", "Track 3"]  # Названия треков
# current_index = 0

# # Функция для воспроизведения трека
# def play_track(index):
#     pygame.mixer.music.load(tracks[index])
#     pygame.mixer.music.play()

# play_track(current_index)

# running = True
# while running:
#     screen.fill(WHITE)  # Очищаем экран
    
#     # Отображаем название трека
#     track_text = font.render(f"Now Playing: {track_names[current_index]}", True, BLACK)
#     screen.blit(track_text, (20, 50))
    
#     pygame.display.flip()
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False
            
#             # P = Play 
#             if event.key == pygame.K_p:
#                 play_track(current_index)
            
#             # S = Stop
#             if event.key == pygame.K_s:
#                 pygame.mixer.music.stop()
            
#             # N = Next 
#             if event.key == pygame.K_n:
#                 current_index = (current_index + 1) % len(tracks)
#                 play_track(current_index)
            
#             # B = Back 
#             if event.key == pygame.K_b:
#                 current_index = (current_index - 1) % len(tracks)
#                 play_track(current_index)

# pygame.quit()
# sys.exit()
import pygame
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Список треков
tracks = [
    "Lab7/music/track1.mp3",
    "Lab7/music/track2.mp3",
    "Lab7/music/track3.mp3"
]
current_index = 0

# Создание окна
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифт
font = pygame.font.Font(None, 36)

def play_track(index):
    pygame.mixer.music.load(tracks[index])
    pygame.mixer.music.play()

def draw_buttons():
    screen.fill(WHITE)
    
    # Кнопки
    buttons = {
        "Play": (50, 150),
        "Pause": (150, 150),
        "Next": (250, 150),
        "Prev": (350, 150)
    }
    
    for text, pos in buttons.items():
        pygame.draw.rect(screen, GRAY, (pos[0] - 40, pos[1] - 20, 80, 40))
        label = font.render(text, True, BLACK)
        screen.blit(label, (pos[0] - label.get_width() // 2, pos[1] - label.get_height() // 2))
    
    # Название трека
    track_text = font.render(f"Track: {current_index + 1}", True, BLACK)
    screen.blit(track_text, (WIDTH // 2 - track_text.get_width() // 2, 50))
    
    pygame.display.flip()

play_track(current_index)
draw_buttons()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            if 10 < x < 90 and 130 < y < 170:  # Play
                play_track(current_index)
            elif 110 < x < 190 and 130 < y < 170:  # Pause
                pygame.mixer.music.pause()
            elif 210 < x < 290 and 130 < y < 170:  # Next
                current_index = (current_index + 1) % len(tracks)
                play_track(current_index)
            elif 310 < x < 390 and 130 < y < 170:  # Previous
                current_index = (current_index - 1) % len(tracks)
                play_track(current_index)
            
            draw_buttons()

pygame.quit()
sys.exit()