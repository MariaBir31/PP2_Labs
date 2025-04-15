#ускоряющая еда (буст)
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

# Размер блока и скорость
BLOCK_SIZE = 20
speed = 8
clock = pygame.time.Clock()

# Шрифты
font = pygame.font.Font(None, 36)

# Инициализация змейки
snake = [(WIDTH//2, HEIGHT//2)]
direction = (0, 0)

# Счёт и уровни
score = 0
high_score = 0
level = 1
boost_timer = 0 ######
boost_lifetime = 40 ######
food_timer = 0
food_lifetime = 100  # Время жизни еды в кадрах

# Генерация еды с разным весом
def generate_food():
    while True:
        pos = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
               random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
        if pos not in snake:  # Проверка, чтобы еда не попала на змейку
            return pos, random.choice(COLORS), random.choice([5, 10, 15])  # Разный вес еды

food, food_color, food_value = generate_food()
food_boost, boost_color, boost_value = generate_food() ######

running = True
while running:
    win.fill(GREEN)
    
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)#запрещает двигаться вверх, если змейка движется вниз (чтобы не развернуться в себя).
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)
    
    # Двигаем змейку
    if direction != (0, 0):
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        
        # Проверка столкновений со стенами и самой собой
        if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            time.sleep(1)
            snake = [(WIDTH//2, HEIGHT//2)]
            direction = (0, 0)
            score = 0
            speed = 10
            level = 1
        else:
            snake.insert(0, new_head)
            
            # Проверяем, съела ли змейка еду
            if new_head == food:
                score += food_value
                food, food_color, food_value = generate_food()
                food_timer = 0
            if new_head == food_boost: ######
                speed += 3 ######
                food_boost, boost_color, boost_value = generate_food() ######
                boost_timer = 0 ######

                
                # Повышение уровня каждые 30 очков
                if score // 30 + 1 > level:
                    level += 1
                    speed += 2  # Увеличиваем скорость
                
                if score > high_score:
                    high_score = score
            else:
                snake.pop()
    
    # Таймер исчезновения еды
    food_timer += 1
    if food_timer > food_lifetime:
        food, food_color, food_value = generate_food()
        food_timer = 0
    boost_timer += 1 ######
    if boost_timer > boost_lifetime: ######
        food_boost, boost_color, boost_value = generate_food() ######
        boost_timer = 0 ######

    
    # Отрисовка змейки
    for i, segment in enumerate(snake):
        color = YELLOW if i == 0 else ORANGE
        pygame.draw.rect(win, color, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Отрисовка еды
    pygame.draw.rect(win, (255, 255, 255), (food_boost[0], food_boost[1], BLOCK_SIZE, BLOCK_SIZE))  # ######
    pygame.draw.rect(win, food_color, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Отображение счёта и уровня
    text = font.render(f"Score: {score}  High Score: {high_score}  Level: {level}", True, WHITE)
    win.blit(text, (WIDTH//2 - text.get_width()//2, 10))
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
