import turtle
import time
import random 

score = 0
high_score = 0
delay =0.1

#creating a windoe screen
wind = turtle.Screen()
wind.title("Snake Maze!!!")
wind.bgcolor("green")
wind.setup(width=600, height=600)
wind.tracer(0)
# После создадим змею.
# Метод penup() тут нужен для того, чтоб змейка не рисовала линию при движении,
#  а goto(x,y) задает координаты, которые перемещают змею в абсолютное положение.

#head
head = turtle.Turtle()
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

#food - boost
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

#counter
pen = turtle.Turtle()
pen.speed(0)
pen.shape = ("square")
pen.color = ("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align = "center",
font=("Arial", 24, "bold"))

# assigning key directions
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
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

wind.listen()
wind.onkeypress(goup, "Up")
wind.onkeypress(godown,"Down")
wind.onkeypress(goleft,"Left")
wind.onkeypress(goright,"Right")

segments = []

while True:
    wind.update()

    # Проверка столкновения со стенами
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Arial", 24, "bold"))

    # Проверка столкновения с едой
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)  # Перемещаем еду

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Arial", 24, "bold"))

    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()  

    # Проверка столкновения с телом
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("Arial", 24, "bold"))

    time.sleep(delay)



    




 






       

