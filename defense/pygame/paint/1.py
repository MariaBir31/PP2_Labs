import pygame

pygame.init()

# Создаём окно
screen = pygame.display.set_mode((600, 600))

# Определяем цвета
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

# Флаг нажатия ЛКМ
LMBpressed = False
THICKNESS = 5

# Фон очищаем в белый цвет
screen.fill(colorWHITE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обрабатываем нажатие ЛКМ
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True

        # Обрабатываем отпускание ЛКМ
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            LMBpressed = False

        # Обрабатываем нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print("Increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("Reduced thickness")
                THICKNESS = max(1, THICKNESS - 1)  # Не даём толщине стать меньше 1

    # Получаем текущие координаты мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Если ЛКМ нажата, рисуем точку
    if LMBpressed:
        pygame.draw.rect(screen, colorRED, (mouse_x, mouse_y, THICKNESS, THICKNESS))

    # Обновляем экран
    pygame.display.flip()

pygame.quit()
