import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Maze!!!")

# Цвета
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
COLORS = [RED, BLUE, ORANGE, PURPLE]

# Скорость и размер
BLOCK_SIZE = 20
speed = 10
clock = pygame.time.Clock()

# Шрифты
font = pygame.font.Font(None, 36)

# Координаты змейки и еды
snake = [(WIDTH//2, HEIGHT//2)]
direction = (0, 0)
food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
        random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
food_color = random.choice(COLORS)

score = 0
high_score = 0

running = True
while running:
    win.fill(GREEN)
    
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)
    
    # Двигаем змейку
    if direction != (0, 0):
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        
        # Проверка столкновений
        if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            time.sleep(1)
            snake = [(WIDTH//2, HEIGHT//2)]
            direction = (0, 0)
            score = 0
            speed = 10
        else:
            snake.insert(0, new_head)
            
            # Проверка на поедание еды
            if new_head == food:
                food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                        random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
                food_color = random.choice(COLORS)
                score += 10
                speed += 0.2
                if score > high_score:
                    high_score = score
            else:
                snake.pop()
    
    # Отрисовка змейки
    for i, segment in enumerate(snake):
        color = YELLOW if i == 0 else ORANGE
        pygame.draw.rect(win, color, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Отрисовка еды
    pygame.draw.rect(win, food_color, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Отображение счёта
    text = font.render(f"Score: {score}  High Score: {high_score}", True, WHITE)
    win.blit(text, (WIDTH//2 - text.get_width()//2, 10))
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
