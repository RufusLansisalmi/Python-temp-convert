# alien_turtle.py
# Rita en klassisk utomjording med turtle
import turtle
import math

# --- Inställningar ---
screen = turtle.Screen()
screen.setup(800, 700)
screen.title("Turtle: Alien")
screen.bgcolor("#0B3D91")  # mörk bakgrund för kontrast

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# Hjälpfunktion: rita fylld ellips (parametrisk)
def draw_ellipse(center, rx, ry, fillcolor, outline=True):
    cx, cy = center
    steps = 120
    t.penup()
    # första punkt
    x = cx + rx * math.cos(0)
    y = cy + ry * math.sin(0)
    t.goto(x, y)
    t.pendown()
    if outline:
        t.color("black", fillcolor)
    else:
        t.color(fillcolor, fillcolor)
    t.begin_fill()
    for i in range(1, steps + 1):
        ang = 2 * math.pi * i / steps
        x = cx + rx * math.cos(ang)
        y = cy + ry * math.sin(ang)
        t.goto(x, y)
    t.end_fill()
    t.penup()

# Hjälpfunktion: rita en cirkel (flera punkter för jämn fyllning)
def draw_circle(center, r, fillcolor):
    draw_ellipse(center, r, r, fillcolor)

# Rita kroppen (stor oval)
body_center = (0, -30)
body_rx, body_ry = 140, 180
draw_ellipse(body_center, body_rx, body_ry, "#26C281")  # grön kropp

# Rita huvudet (oval/cirkel)
head_center = (0, 140)
head_rx, head_ry = 100, 90
draw_ellipse(head_center, head_rx, head_ry, "#27AE60")

# Halskoppling (liten oval där huvud möter kropp)
draw_ellipse((0, 60), 40, 20, "#27AE60", outline=False)

# Ögon (stora, vita med svarta pupiller)
left_eye_center = (-35, 160)
right_eye_center = (35, 160)
draw_circle(left_eye_center, 25, "white")
draw_circle(right_eye_center, 25, "white")
draw_circle((-35, 165), 10, "black")
draw_circle((35, 165), 10, "black")

# Highlight i pupillerna (små vita cirklar)
draw_circle((-30, 170), 4, "white")
draw_circle((39, 170), 4, "white")

# Mun (en leende båge)
t.penup()
t.goto(-40, 135)
t.setheading(-60)
t.pendown()
t.color("black")
t.pensize(4)
# använd circle för båge: radius, extent
t.circle(45, 120)  # rita en båge => leende
t.pensize(2)
t.penup()

# Antenner
def draw_antenna(base_x, base_y, angle_deg):
    t.penup()
    t.goto(base_x, base_y)
    t.setheading(angle_deg)
    t.pendown()
    t.pensize(3)
    t.color("black")
    t.forward(45)
    # liten kula i slutet
    end = t.position()
    draw_circle((end[0], end[1]), 8, "#F4D03F")  # gul kula
    t.penup()
    t.pensize(2)

draw_antenna(-30, 195, 150)
draw_antenna(30, 195, 30)

# Armar (kurvor) och händer (små tre-prickiga fingrar)
def draw_arm(start_x, start_y, direction):
    # direction = 1 för höger arm, -1 för vänster
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(250 if direction == -1 else 290)
    t.pendown()
    t.pensize(6)
    t.color("#27AE60")
    t.forward(90)
    hand_x, hand_y = t.position()
    # rita små "fingrar"
    for a in (-20, 0, 20):
        t.penup()
        t.goto(hand_x, hand_y)
        t.setheading(t.heading() + a)
        t.pendown()
        t.forward(18)
    t.penup()
    t.pensize(2)

draw_arm(-120, 10, -1)  # vänster arm
draw_arm(120, 10, 1)    # höger arm

# Ben (två korta ben)
def draw_leg(start_x, start_y):
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(-90)
    t.pendown()
    t.pensize(10)
    t.color("#145A32")
    t.forward(60)
    # fot
    t.penup()
    t.forward(10)
    t.pendown()
    draw_ellipse((t.xcor(), t.ycor()-8), 18, 8, "#145A32")
    t.penup()
    t.pensize(2)

draw_leg(-50, -180)
draw_leg(50, -180)

# Dekoration: prickar på kroppen
t.pensize(1)
spots = [(-40, -20), (30, -10), (-10, -60), (50, -80), (-70, -100)]
for (sx, sy) in spots:
    draw_circle((sx, sy), 12, "#1E8449")

# Signatur / text
t.goto(0, -300)
t.color("white")
t.write("En liten utomjording 🛸", align="center", font=("Arial", 16, "bold"))

# Klarmeddelande
t.penup()
t.goto(0, -330)
t.color("lightgray")
t.write("Stäng fönstret för att avsluta.", align="center", font=("Arial", 10, "normal"))

# Avsluta: håll fönstret öppet tills användaren stänger det
t.hideturtle()
screen.mainloop()
