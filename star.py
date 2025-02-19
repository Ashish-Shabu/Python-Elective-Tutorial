import turtle


def draw_star(t, length):
    t.begin_fill()
    for _ in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()


def draw_stars_in_circle(t, num, star_length, radius):
    for i in range(num):

        t.penup()
        t.goto(0, 0)

        angle = 360 / num * i

        t.setheading(angle)

        t.forward(radius)

        t.right(36)
        t.pendown()
        draw_star(t, star_length)
        t.penup()


num_stars = int(input("Enter the number of stars: "))

drawer = turtle.Turtle()
#drawer.shape("turtle")  
drawer.speed(2)
drawer.fillcolor("blue")

draw_stars_in_circle(drawer, num_stars, 100, 200)

drawer.hideturtle()
turtle.done()