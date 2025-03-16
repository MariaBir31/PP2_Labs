import pygame
import os

pygame.init()
pygame.mixer.init()

# Полные пути к трекам
tracks = [
    os.path.abspath("music/track1.mp3"),
    os.path.abspath("music/track2.mp3"),
    os.path.abspath("music/track3.mp3")
]
current_index = 0

# Проверяем, существуют ли файлы
for track in tracks:
    if not os.path.exists(track):
        print(f"Ошибка: Файл {track} не найден!")
        exit()

# Создаём окно
pygame.display.set_mode((300, 100))
pygame.display.set_caption("Super Simple Music Player")

# Функция для воспроизведения трека
def play_track(index):
    pygame.mixer.music.load(tracks[index])
    pygame.mixer.music.play()
    print(f"Сейчас играет: {tracks[index]}")  # Вывод текущего трека

# Запускаем первый трек
play_track(current_index)

running = True
while running:
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
