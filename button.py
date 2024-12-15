import time
import turtle

class Button:
    def __init__(self, x, y, width, height, label, note_color, callback):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.note_color = note_color
        self.callback = callback
        self.pressed = False

    @property
    def color(self):
        return self.note_color

    def is_clicked(self, x, y):
        return self.x - self.width / 2 <= x <= self.x + self.width / 2 and \
               self.y - self.height / 2 <= y <= self.y + self.height / 2

    def draw(self):
        turtle.penup()
        turtle.goto(self.x - self.width / 2, self.y - self.height / 2)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color("white")
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
        turtle.end_fill()

        # Write the label
        turtle.penup()
        turtle.goto(self.x, self.y - 10)
        turtle.color("black")
        turtle.write(self.label, align="center", font=("Arial", 12, "bold"))

    def onclick(self, func):
        turtle.goto(self.x, self.y)  # Reset turtle position
        turtle.onclick(func)