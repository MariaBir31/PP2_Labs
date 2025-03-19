#Starrrrrr
import turtle
import time
import random 

# Инициализация счёта
score = 0
high_score = 0
delay = 0.1

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
food.shape("star")  # Устанавливаем форму звезды
food.color("gold")
food.penup()
food.goto(0, 100)

# Счётчик
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "bold"))

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

    # Проверка столкновения со стенами
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)  # Убираем змейку с экрана
        segments.clear()
        
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    # Проверка столкновения головы с едой
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Меняем цвет еды при каждом появлении
        food.color(random.choice(["red", "blue", "gold", "purple", "orange"]))

        # Добавляем новый сегмент змейки
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        # Ускоряем игру
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        
        # Обновляем счёт
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

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
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    time.sleep(delay)

wind.mainloop()
