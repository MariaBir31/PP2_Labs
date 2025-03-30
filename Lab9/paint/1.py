import pygame
import math

pygame.init()

'''
Горячие клавиши:
1 – Линия
2 – Прямоугольник
3 – Круг
4 – Квадрат
5 – Прямоугольный треугольник
6 – Равносторонний треугольник
7 – Ромб
E – Ластик
R – Красный цвет
B – Синий цвет
K – Черный цвет
+ – Увеличить толщину
- – Уменьшить толщину
'''

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Переменные состояния
drawing = False
tool = "line"  # "line", "rect", "circle", "eraser", "square", "triangle", "equilateral", "rhombus"
color = BLACK
thickness = 5
start_pos = (0, 0)

# Фоновый слой
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)

running = True
while running:
    screen.blit(background, (0, 0))

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
            elif event.key == pygame.K_4:
                tool = "square"
            elif event.key == pygame.K_5:
                tool = "triangle"
            elif event.key == pygame.K_6:
                tool = "equilateral"
            elif event.key == pygame.K_7:
                tool = "rhombus"
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
                x1, y1 = start_pos
                x2, y2 = end_pos

                if tool == "line":
                    pygame.draw.line(background, color, start_pos, end_pos, thickness)
                elif tool == "rect":
                    pygame.draw.rect(background, color, pygame.Rect(
                        min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), thickness)
                elif tool == "circle":
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(background, color, start_pos, radius, thickness)
                elif tool == "square":
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(background, color, (x1, y1, side, side), thickness)
                elif tool == "triangle":
                    points = [(x1, y2), (x2, y2), (x1, y1)]
                    pygame.draw.polygon(background, color, points, thickness)
                elif tool == "equilateral":
                    height = abs(y2 - y1)
                    base_half = height / math.sqrt(3)
                    points = [(x1, y2), (x1 - base_half, y1), (x1 + base_half, y1)]
                    pygame.draw.polygon(background, color, points, thickness)
                elif tool == "rhombus":
                    width = abs(x2 - x1)
                    height = abs(y2 - y1)
                    points = [(x1, y1 - height // 2), (x1 + width // 2, y1),
                              (x1, y1 + height // 2), (x1 - width // 2, y1)]
                    pygame.draw.polygon(background, color, points, thickness)
                elif tool == "eraser":
                    pygame.draw.circle(background, WHITE, start_pos, thickness)

                drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "eraser":
                pygame.draw.circle(background, WHITE, event.pos, thickness)

    pygame.display.flip()

pygame.quit()

