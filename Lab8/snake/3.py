import turtle
import time
import random 

# Инициализация счёта и уровня
score = 0
high_score = 0
level = 1
foods_eaten = 0  # Количество съеденных звёзд на текущем уровне
delay = 0.1  # Начальная задержка

# Создание окна
wind = turtle.Screen()
wind.title("Snake Maze!!!")
wind.bgcolor("green")
wind.setup(width=600, height=600)
wind.tracer(0)

# Создание формы звезды
star_shape = ((0, 10), (3, 3), (10, 3), (4, -1), (6, -8), 
              (0, -4), (-6, -8), (-4, -1), (-10, 3), (-3, 3))
wind.register_shape("star", star_shape)

# Создание головы змеи
head = turtle.Turtle()
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Создание еды в виде звезды
food = turtle.Turtle()
food.shape("star")
food.color("gold")
food.penup()
food.goto(0, 100)

# Таймер для еды
last_food_time = time.time()  # Время появления еды
food_timer = 5  # Через сколько секунд еда исчезает

# Счётчик
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0  Level: 1", align="center", font=("Arial", 24, "bold"))

# Управление змейкой
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goright():
    if head.direction != "left":
        head.direction = "right"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Привязываем клавиши к движениям
wind.listen()
wind.onkeypress(goup, "Up")
wind.onkeypress(godown, "Down")
wind.onkeypress(goleft, "Left")
wind.onkeypress(goright, "Right")

segments = []

# Основной игровой цикл
while True:
    wind.update()

    # Проверяем, прошло ли время, чтобы еда исчезла
    if time.time() - last_food_time >= food_timer:
        x, y = random.randint(-270, 270), random.randint(-270, 270)
        food.goto(x, y)
        food.color(random.choice(["red", "blue", "gold", "purple", "orange"]))  # Меняем цвет
        last_food_time = time.time()  # Обновляем таймер

    # Проверка столкновения со стенами
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)  # Убираем змейку с экрана
        segments.clear()
        
        score = 0
        level = 1
        foods_eaten = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}  Level: {level}", align="center", font=("Arial", 24, "bold"))

    # Проверка столкновения головы с едой
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        food.color(random.choice(["red", "blue", "gold", "purple", "orange"]))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        foods_eaten += 1

        # Ускорение и переход на следующий уровень
        if foods_eaten >= 4:  # Меняем уровень каждые 4 еды
            level += 1
            foods_eaten = 0
            delay = max(0.05, delay - 0.01)  # Уменьшаем задержку (увеличиваем скорость)

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}  Level: {level}", align="center", font=("Arial", 24, "bold"))

        last_food_time = time.time()  # Сбрасываем таймер еды

    # Двигаем тело змейки за головой
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Проверяем столкновение головы с телом
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            level = 1
            foods_eaten = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}  Level: {level}", align="center", font=("Arial", 24, "bold"))

    time.sleep(delay)

wind.mainloop()
