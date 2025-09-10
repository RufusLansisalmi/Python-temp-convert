import turtle

# --- HJÄLPFUNKTIONER ---

def _draw_one_eye(t, x_pos, y_pos, tilt_angle):
    """Hjälpfunktion för att rita ett enda ovalt öga."""
    t.penup()
    t.goto(x_pos, y_pos)
    t.tilt(tilt_angle)
    t.stamp()

# --- FUNKTIONER FÖR KROPPSDELAR ---

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
    """Ritar en centrerad kropp under huvudet."""
    t.penup()
    t.goto(x - 40, y - head_radius + 5)
    t.pendown()
    t.color("#388E3C")
    t.begin_fill()
    t.goto(x - 60, y - head_radius - 100)
    t.goto(x + 60, y - head_radius - 100)
    t.goto(x + 40, y - head_radius + 5)
    t.goto(x - 40, y - head_radius + 5)
    t.end_fill()

def draw_eyes(t, x, y):
    """Ritar båda ögonen genom att återanvända kod."""
    original_shape = t.shape()
    
    # Förbered pennan för att stämpla ögon
    t.shape("circle")
    t.color("black")
    t.shapesize(stretch_wid=3, stretch_len=1.5)

    # Använd hjälpfunktionen för att rita varje öga
    _draw_one_eye(t, x - 35, y + 25, 30)   # Vänster öga
    _draw_one_eye(t, x + 35, y + 25, -30)  # Höger öga

    # Återställ pennans ursprungliga form
    t.shape(original_shape)
    t.shapesize(stretch_wid=1, stretch_len=1)
    t.tilt(0) # Nollställ vinkeln

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

# --- HUVUDFUNKTIONER FÖR KONTROLL ---

def draw_alien(t, center_x, center_y):
    """Huvudfunktion som anropar alla rit-funktioner i ordning."""
    HEAD_RADIUS = 100
    
    draw_head(t, center_x, center_y, HEAD_RADIUS)
    draw_body(t, center_x, center_y, HEAD_RADIUS)
    draw_eyes(t, center_x, center_y)
    draw_antenna(t, center_x, center_y, HEAD_RADIUS)
    draw_mouth(t, center_x, center_y)

def setup_environment():
    """Skapar och konfigurerar skärmen och turtle-pennan."""
    screen = turtle.Screen()
    screen.bgcolor("#000033")
    screen.title("Alien ritad med Python Turtle (Refaktorerad)")

    alien_turtle = turtle.Turtle()
    alien_turtle.speed(0)
    alien_turtle.pensize(3)
    alien_turtle.hideturtle()
    
    return screen, alien_turtle

def main():
    """Huvudfunktion som startar programmet."""
    screen, alien_turtle = setup_environment()
    draw_alien(alien_turtle, 0, 0)
    screen.mainloop()

# --- STARTA PROGRAMMET ---
if __name__ == "__main__":
    main()