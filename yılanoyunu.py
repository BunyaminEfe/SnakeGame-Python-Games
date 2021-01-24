import turtle
import random

w = 500
h = 500
fs = 10
d = 100  

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def r():
    global yılan, yön, bejo, cam
    yılan = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    yön = "up"
    bejo = nun()
    food.goto(bejo)
    hall()

def hall():
    global yön

    new_head = yılan[-1].copy()
    new_head[0] = yılan[-1][0] + offsets[yön][0]
    new_head[1] = yılan[-1][1] + offsets[yön][1]

    if new_head in yılan[:-1]:  
        r()
    else:
        yılan.append(new_head)

        if not khana():
            yılan.pop(0)  

        if yılan[-1][0] > w / 2:
            yılan[-1][0] -= w
        elif yılan[-1][0] < - w / 2:
            yılan[-1][0] += w
        elif yılan[-1][1] > h / 2:
            yılan[-1][1] -= h
        elif yılan[-1][1] < -h / 2:
            yılan[-1][1] += h

        cam.clearstamps()

        for segment in yılan:
            cam.goto(segment[0], segment[1])
            cam.stamp()

        screen.update()
        turtle.ontimer(hall, d)

def khana():
    global bejo
    if dist(yılan[-1], bejo) < 20:
        bejo = nun()
        food.goto(bejo)
        return True
    return False

def nun():
    x = random.randint(- w / 2 + fs, w / 2 - fs)
    y = random.randint(- h / 2 + fs, h / 2 - fs)
    return (x, y)

def dist(poos1, poos2):
    x1, y1 = poos1
    x2, y2 = poos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def yukarı():
    global yön
    if yön != "down":
        yön = "up"

def sag_git():
    global yön
    if yön != "left":
        yön = "right"

def asagi():
    global yön
    if yön != "up":
        yön = "down"

def sol_git():
    global yön
    if yön != "right":
        yön = "left"

screen = turtle.Screen()
screen.setup(w, h)
screen.title("Yılan Oyunu")
screen.bgcolor("grey")
screen.setup(500, 500)
screen.tracer(0)






cam = turtle.Turtle("turtle")
cam.penup()



food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(fs / 20) 
food.penup()

screen.listen()
screen.onkey(yukarı, "Up")
screen.onkey(sag_git, "Right")
screen.onkey(asagi, "Down")
screen.onkey(sol_git, "Left")

r()
turtle.done()