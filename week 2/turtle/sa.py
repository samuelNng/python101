import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Three-Petal Shape Rotated 90 Degrees")

# Create the turtle object
t = turtle.Turtle()
t.speed(5)
turtle.colormode(255)

# Function to draw a filled curved petal
def draw_filled_petal(radius, angle, fill_color):
    t.fillcolor(fill_color)
    t.begin_fill()
    # Draw arc
    
    # Draw line to center
    t.forward(radius)
    t.left(90)
    
    t.circle(radius, 80)
    # Reorient to close the petal
    t.left(90 + 80)
    t.end_fill()

# Function to draw the shape with three curved petals + center circle
def draw_three_slice_circle(radius, center_circle_radius):
    angle_per_slice = 120    # Each petal covers 120 degrees
    petal_color = (153, 0, 0)  # Dark red color for petals

    # Draw three petals, each rotated 120° from the previous,
    # but start heading at 90° for the first petal to rotate the whole shape left by 90.
    for i in range(3):
        t.penup()
        t.goto(0, 0)
        # 90° for the first petal, then add 120° per iteration
        t.setheading(90 + i * 120+75)
        t.pendown()
        draw_filled_petal(radius, angle_per_slice, petal_color)

    # Draw the central circle (white cutout)
    t.penup()
    t.goto(0, -center_circle_radius)
    t.setheading(0)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(center_circle_radius)
    t.end_fill()

# Parameters
outer_radius = 200        # Radius of the large arc for the petals
center_circle_radius = 60 # Radius of the center cutout circle

# Draw the full shape
draw_three_slice_circle(outer_radius, center_circle_radius)

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
