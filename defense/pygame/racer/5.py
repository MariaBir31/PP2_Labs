import pygame
import random
import time

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка изображений
image_background = pygame.image.load('Lab8/resources/AnimatedStreet.png')
image_background = pygame.transform.scale(image_background, (WIDTH, HEIGHT))
image_player = pygame.image.load('Lab8/resources/Player.png')
image_player = pygame.transform.scale(image_player, (50, 100))
image_enemy = pygame.image.load('Lab8/resources/Enemy.png')
image_enemy = pygame.transform.scale(image_enemy, (50, 100))
image_coin = pygame.image.load('Lab8/resources/Coin.png')
image_coin = pygame.transform.scale(image_coin, (30, 30))

# Звуки
pygame.mixer.music.load('Lab8/resources/background.wav')
pygame.mixer.music.play(-1)  # Фоновая музыка, будет играть бесконечно
sound_crash = pygame.mixer.Sound('Lab8/resources/crash.wav')  # Звук при столкновении

# Шрифт для отображения очков
font = pygame.font.SysFont("Verdana", 30)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player  # Загружаем изображение игрока
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 70))  # Размещаем игрока внизу экрана
        self.speed = 5  # Скорость движения игрока
        self.coins_collected = 0  # Количество собранных монет

    # Метод для сброса позиции игрока
    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT - 70)  # Сброс позиции игрока в центр экрана снизу
        self.coins_collected = 0  # Сброс количества монет

    # Метод для движения игрока
    def move(self):
        keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
        if keys[pygame.K_RIGHT]:  # Если нажата клавиша вправо
            self.rect.move_ip(self.speed, 0)  # Двигаем игрока вправо
        if keys[pygame.K_LEFT]:  # Если нажата клавиша влево
            self.rect.move_ip(-self.speed, 0)  # Двигаем игрока влево
        self.rect.clamp_ip(screen.get_rect())  # Ограничиваем движение игрока границами экрана

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy  # Загружаем изображение врага
        self.rect = self.image.get_rect()  # Получаем прямоугольник вокруг изображения
        self.base_speed = 5  # Базовая скорость врага
        self.speed = self.base_speed  # Текущая скорость врага
        self.generate_random_rect()  # Устанавливаем случайное начальное положение

    # Метод для генерации случайной позиции врага
    def generate_random_rect(self):
        self.rect.left = random.randint(0, max(0, WIDTH - self.rect.w))  # Размещаем врага в случайной горизонтальной позиции
        self.rect.bottom = 0  # Начальное положение сверху экрана

    # Метод для движения врага
    def move(self):
        self.rect.move_ip(0, self.speed)  # Двигаем врага вниз по экрану
        if self.rect.top > HEIGHT:  # Если враг вышел за нижнюю границу экрана
            self.generate_random_rect()  # Перемещаем его обратно наверх

    # Метод для увеличения скорости врага в зависимости от собранных монет
    def increase_speed(self, coins):
        self.speed = self.base_speed + (coins // 10)  # Увеличиваем скорость каждые 10 собранных монет

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin  # Загружаем изображение монеты
        self.rect = self.image.get_rect()  # Получаем прямоугольник вокруг изображения
        self.speed = 3  # Скорость падения монеты
        self.value = random.choice([1, 2, 5])  # Случайная стоимость монеты (1, 2 или 5 очков)
        self.generate_random_rect()  # Устанавливаем случайное начальное положение

    # Метод для генерации случайной позиции монеты
    def generate_random_rect(self):
        self.rect.left = random.randint(0, max(0, WIDTH - self.rect.w))  # Размещаем монету в случайной горизонтальной позиции
        self.rect.bottom = 0  # Начальное положение сверху экрана
        self.value = random.choice([1, 2, 5])  # Перегенерируем стоимость монеты при создании

    # Метод для движения монеты
    def move(self):
        self.rect.move_ip(0, self.speed)  # Двигаем монету вниз по экрану
        if self.rect.top > HEIGHT:  # Если монета вышла за нижнюю границу экрана
            self.generate_random_rect()  # Перемещаем её обратно наверх

# Функция для сброса игры
def reset_game():
    player.reset()  # Сбрасываем игрока
    enemy.generate_random_rect()  # Генерируем новую случайную позицию для врага
    for coin in coin_sprites:  # Для каждой монеты на экране
        coin.generate_random_rect()  # Перегенерируем её позицию

running = True
clock = pygame.time.Clock()
FPS = 60  # Частота обновления экрана

# Создаем объекты
player = Player()
enemy = Enemy()
all_sprites = pygame.sprite.Group(player, enemy)  # Группа всех спрайтов (игрок + враг)
enemy_sprites = pygame.sprite.Group(enemy)  # Группа врагов
coin_sprites = pygame.sprite.Group()  # Группа монет

# Генерация монет на экране
for _ in range(2):  # Три монеты на экране одновременно
    coin = Coin()
    coin_sprites.add(coin)
    all_sprites.add(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь закрыл окно
            running = False

    player.move()  # Двигаем игрока
    enemy.move()  # Двигаем врага
    for coin in coin_sprites:  # Двигаем каждую монету
        coin.move()

    screen.blit(image_background, (0, 0))  # Отображаем фоновое изображение
    for entity in all_sprites:  # Отображаем все спрайты (игрока, врагов, монеты)
        screen.blit(entity.image, entity.rect)

    # Проверяем столкновение с врагом
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()  # Воспроизводим звук столкновения
        time.sleep(1)  # Небольшая задержка, чтобы игрок успел заметить
        reset_game()  # Сбрасываем игру после столкновения

    # Проверяем сбор монет
    for coin in coin_sprites:
        if player.rect.colliderect(coin.rect):  # Если игрок коснулся монеты
            player.coins_collected += coin.value  # Добавляем очки за монету
            coin.generate_random_rect()  # Генерируем новую монету
            enemy.increase_speed(player.coins_collected)  # Увеличиваем скорость врага

    # Отображаем количество собранных монет
    coin_text = font.render(f"Coins: {player.coins_collected}", True, "blue")
    screen.blit(coin_text, (WIDTH - 150, 10))

    pygame.display.flip()  # Обновляем экран
    clock.tick(FPS)  # Устанавливаем частоту обновлений

pygame.quit()  # Закрытие Pygame
