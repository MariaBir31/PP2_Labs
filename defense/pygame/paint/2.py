import pygame

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Шрифт для таблицы клавиш
font = pygame.font.Font(None, 24)  

# Переменные состояния
drawing = False
tool = "line"  # "line", "rect", "circle", "eraser"
color = BLACK
thickness = 5
start_pos = (0, 0)

# Фоновый слой
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)

running = True
while running:
    screen.blit(background, (0, 0))

    # Отрисовка таблицы горячих клавиш
    keys_info = [
        "1 - Линия", "2 - Прямоугольник", "3 - Круг",
        "E - Ластик", "R - Красный", "B - Синий", "K - Черный",
        "+ - Увеличить толщину", "- - Уменьшить толщину"
    ]
    for i, text in enumerate(keys_info):
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (10, 10 + i * 20))  # Смещаем строки вниз

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка выбора инструмента и цвета
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "line"
            elif event.key == pygame.K_2:
                tool = "rect"
            elif event.key == pygame.K_3:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
            elif event.key == pygame.K_EQUALS:
                thickness += 1
            elif event.key == pygame.K_MINUS and thickness > 1:
                thickness -= 1

        # Обработка рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                if tool == "line":
                    pygame.draw.line(background, color, start_pos, end_pos, thickness)
                elif tool == "rect":
                    pygame.draw.rect(background, color, pygame.Rect(
                        min(start_pos[0], end_pos[0]), 
                        min(start_pos[1], end_pos[1]), 
                        abs(start_pos[0] - end_pos[0]), 
                        abs(start_pos[1] - end_pos[1])
                    ), thickness)
                elif tool == "circle":
                    radius = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5
                    pygame.draw.circle(background, color, start_pos, int(radius), thickness)
                elif tool == "eraser":
                    pygame.draw.circle(background, WHITE, start_pos, thickness)
                drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "eraser":
                pygame.draw.circle(background, WHITE, event.pos, thickness)

    pygame.display.flip()

pygame.quit()
