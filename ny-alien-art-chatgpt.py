import turtle
import math

# --- Inställningar ---
screen = turtle.Screen()
screen.setup(800, 700)
screen.title("Turtle: Alien")
screen.bgcolor("#0B3D91")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# --- Hjälpfunktioner ---
def draw_ellipse(center, rx, ry, fillcolor, outline=True):
    """Rita en fylld ellips med given mittpunkt och radier."""
    cx, cy = center
    steps = 120
    t.penup()
    x = cx + rx * math.cos(0)
    y = cy + ry * math.sin(0)
    t.goto(x, y)
    t.pendown()
    t.color("black" if outline else fillcolor, fillcolor)
    t.begin_fill()
    for i in range(steps + 1):
        ang = 2 * math.pi * i / steps
        x = cx + rx * math.cos(ang)
        y = cy + ry * math.sin(ang)
        t.goto(x, y)
    t.end_fill()
    t.penup()

def draw_circle(center, r, fillcolor, outline=True):
    draw_ellipse(center, r, r, fillcolor, outline)

# --- Alien-delar ---
def draw_body():
    draw_ellipse((0, -30), 140, 180, "#26C281")
    draw_ellipse((0, 60), 40, 20, "#27AE60", outline=False)

def draw_head():
    draw_ellipse((0, 140), 100, 90, "#27AE60")

def draw_eyes():
    for dx in (-35, 35):
        draw_circle((dx, 160), 25, "white")
        draw_circle((dx, 165), 10, "black")
        draw_circle((dx + (5 if dx > 0 else 5), 170), 4, "white")

def draw_mouth():
    t.penup()
    t.goto(-40, 135)
    t.setheading(-60)
    t.pendown()
    t.color("black")
    t.pensize(4)
    t.circle(45, 120)
    t.pensize(2)
    t.penup()

def draw_antenna(base_x, base_y, angle_deg):
    t.penup()
    t.goto(base_x, base_y)
    t.setheading(angle_deg)
    t.pendown()
    t.pensize(3)
    t.color("black")
    t.forward(45)
    end = t.position()
    draw_circle(end, 8, "#F4D03F")
    t.penup()
    t.pensize(2)

def draw_antennas():
    draw_antenna(-30, 195, 150)
    draw_antenna(30, 195, 30)

def draw_arm(start_x, start_y, heading):
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(heading)
    t.pendown()
    t.pensize(6)
    t.color("#27AE60")
    t.forward(90)
    hand_x, hand_y = t.position()
    for a in (-20, 0, 20):
        t.penup()
        t.goto(hand_x, hand_y)
        t.setheading(heading + a)
        t.pendown()
        t.forward(18)
    t.penup()
    t.pensize(2)

def draw_arms():
    draw_arm(-120, 10, 250)  # vänster
    draw_arm(120, 10, 290)   # höger

def draw_leg(start_x, start_y):
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(-90)
    t.pendown()
    t.pensize(10)
    t.color("#145A32")
    t.forward(60)
    t.penup()
    t.forward(10)
    draw_ellipse((t.xcor(), t.ycor() - 8), 18, 8, "#145A32")
    t.pensize(2)

def draw_legs():
    draw_leg(-50, -180)
    draw_leg(50, -180)

def draw_spots():
    spots = [(-40, -20), (30, -10), (-10, -60), (50, -80), (-70, -100)]
    for pos in spots:
        draw_circle(pos, 12, "#1E8449")

def draw_signature():
    t.goto(0, -300)
    t.color("white")
    t.write("En liten utomjording 🛸", align="center", font=("Arial", 16, "bold"))
    t.goto(0, -330)
    t.color("lightgray")
    t.write("Stäng fönstret för att avsluta.", align="center", font=("Arial", 10, "normal"))

# --- Main ---
def draw_alien():
    draw_body()
    draw_head()
    draw_eyes()
    draw_mouth()
    draw_antennas()
    draw_arms()
    draw_legs()
    draw_spots()
    draw_signature()

# Kör programmet
draw_alien()
t.hideturtle()
screen.mainloop()
