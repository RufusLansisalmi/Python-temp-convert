import turtle

# --- FUNKTIONER FÖR ATT RITA DE OLIKA DELARNA ---

def draw_head(t, x, y, radius):
    """Ritar utomjordingens huvud."""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color("#4CAF50")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_body(t, x, y, head_radius):
    """Ritar en enkel, centrerad kropp under huvudet."""
    t.penup()
    # Startpunkt: Nackens vänstra sida
    t.goto(x - 40, y - head_radius + 5)
    t.pendown()
    t.color("#388E3C") # En mörkare grön
    t.begin_fill()
    
    # Rita en symmetrisk trapets med direkta koordinater
    t.goto(x - 60, y - head_radius - 100)  # Nedre vänstra hörnet
    t.goto(x + 60, y - head_radius - 100)  # Nedre högra hörnet
    t.goto(x + 40, y - head_radius + 5)   # Nackens högra sida
    t.goto(x - 40, y - head_radius + 5)   # Tillbaka till start

    t.end_fill()

def draw_eyes(t, x, y):
    """Ritar de stora, klassiska alien-ögonen."""
    original_shape = t.shape()
    original_tilt = t.tiltangle()

    t.shape("circle")
    t.color("black")
    t.penup()
    
    # Vänster öga
    t.goto(x - 35, y + 25)
    t.shapesize(stretch_wid=3, stretch_len=1.5)
    t.tilt(30)
    t.stamp()

    # Höger öga
    t.goto(x + 35, y + 25)
    t.tilt(-30)
    t.stamp()

    # Återställ
    t.shape(original_shape)
    t.tilt(original_tilt)
    t.shapesize(stretch_wid=1, stretch_len=1)

def draw_antenna(t, x, y, head_radius):
    """Ritar en antenn på toppen av huvudet."""
    t.penup()
    t.goto(x, y + head_radius)
    t.pendown()
    t.color("#4CAF50")
    t.pensize(5)
    t.setheading(90)
    t.forward(50)
    t.dot(18, "red")
    t.pensize(3)

def draw_mouth(t, x, y):
    """Ritar en liten, enkel mun."""
    t.penup()
    t.goto(x - 20, y - 30)
    t.pendown()
    t.color("black")
    t.setheading(-60)
    t.circle(25, 120)

# --- HUVUDPROGRAM ---

screen = turtle.Screen()
screen.bgcolor("#000033")
screen.title("Alien ritad med Python Turtle")

alien_turtle = turtle.Turtle()
alien_turtle.speed(0)
alien_turtle.pensize(3)
alien_turtle.hideturtle()

HEAD_RADIUS = 100
CENTER_X = 0
CENTER_Y = 0

draw_head(alien_turtle, CENTER_X, CENTER_Y, HEAD_RADIUS)
draw_body(alien_turtle, CENTER_X, CENTER_Y, HEAD_RADIUS)
draw_eyes(alien_turtle, CENTER_X, CENTER_Y)
draw_antenna(alien_turtle, CENTER_X, CENTER_Y, HEAD_RADIUS)
draw_mouth(alien_turtle, CENTER_X, CENTER_Y)

screen.mainloop()