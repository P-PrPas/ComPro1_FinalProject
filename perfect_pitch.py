import harmonic_ball
import turtle
import random
import heapq
import event
from button import Button
import pygame.midi
import time


class PerfectPitch:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.ball_list = []
        self.status_message = ""
        self.status_message_time = 0
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.answer = 0
        self.score = 0
        self.lives = 3
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.game_end = False
        self.game_result = False

        self.note_data = [{"label": "C",
                           "color": (255, 0, 0),
                           "note": "Sound/4C.wav"},
                          {"label": "C#",
                           "color": (255, 0, 255),
                           "note": "Sound/4C#.wav"},
                          {"label": "D",
                           "color": (255, 165, 0),
                           "note": "Sound/4D.wav"},
                          {"label": "Eb",
                           "color": (150, 75, 0),
                           "note": "Sound/4Eb.wav"},
                          {"label": "E",
                           "color": (255, 255, 0),
                           "note": "Sound/4E.wav"},
                          {"label": "F",
                           "color": (0, 128, 0),
                           "note": "Sound/4F.wav"},
                          {"label": "F#",
                           "color": (0, 128, 128),
                           "note": "Sound/4F#.wav"},
                          {"label": "G",
                           "color": (0, 0, 255),
                           "note": "Sound/4G.wav"},
                          {"label": "Ab",
                           "color": (75, 0, 130),
                           "note": "Sound/4Ab.wav"},
                          {"label": "A",
                           "color": (128, 0, 128),
                           "note": "Sound/4A.wav"},
                          {"label": "Bb",
                           "color": (255, 192, 203),
                           "note": "Sound/4Bb.wav"},
                          {"label": "B",
                           "color": (255, 215, 0),
                           "note": "Sound/4B.wav"},
                          {"label": "High-C",
                           "color": (255, 0, 0),
                           "note": "Sound/5C.wav"},
                          {"label": "High-C#",
                           "color": (255, 0, 255),
                           "note": "Sound/5C#.wav"},
                          {"label": "High-D",
                           "color": (255, 165, 0),
                           "note": "Sound/5D.wav"},
                          {"label": "High-Eb",
                           "color": (150, 75, 0),
                           "note": "Sound/5Eb.wav"},
                          {"label": "High-E",
                           "color": (255, 255, 0),
                           "note": "Sound/5E.wav"},
                          {"label": "High-F",
                           "color": (0, 128, 0),
                           "note": "Sound/5F.wav"},
                          {"label": "High-F#",
                           "color": (0, 128, 128),
                           "note": "Sound/5F#.wav"},
                          {"label": "High-G",
                           "color": (0, 0, 255),
                           "note": "Sound/5G.wav"},
                          {"label": "High-Ab",
                           "color": (75, 0, 130),
                           "note": "Sound/5Ab.wav"},
                          {"label": "High-A",
                           "color": (128, 0, 128),
                           "note": "Sound/5A.wav"},
                          {"label": "High-Bb",
                           "color": (255, 192, 203),
                           "note": "Sound/5Bb.wav"},
                          {"label": "High-B",
                           "color": (255, 215, 0),
                           "note": "Sound/5B.wav"}
                          ]

        self.button_list = []

        self.create_balls(num_balls)
        self.create_buttons()
        # Check all the balls
        '''for a in self.ball_list:
            print(a)'''

    def checking_game_ending(self):
        if self.game_end:
            return self.game_end

    def checking_game_status(self):
        return self.game_result

    def create_balls(self, num_balls):
        for i in range(num_balls):
            ball_data = random.choice(self.note_data)
            radius = 0.05 * self.canvas_width
            x = -self.canvas_width + (i + 1) * (2 * self.canvas_width / (self.num_balls + 1))
            y = 0.0
            vx = 10 * random.uniform(-1.0, 1.0)
            vy = 10 * random.uniform(-1.0, 1.0)
            ball = harmonic_ball.Ball(radius, x, y, vx, vy, ball_data["color"], ball_data["note"], ball_data["label"])
            self.ball_list.append(ball)
        self.answer = len(self.ball_list) + 1

    def create_buttons(self):
        button_width = 50
        button_height = 30
        gap = 25
        start_x = -self.canvas_width - gap/2
        start_y = -self.canvas_height - 2*gap

        for i, note in enumerate(self.note_data[:12]):
            x = start_x + i * (button_width + gap)
            button = Button(x, start_y, button_width, button_height, note["label"], note["color"],
                            self.handle_button_click)
            button.onclick(lambda x, y, note: self.handle_button_click(note))
            self.button_list.append(button)

    def handle_button_click(self, color):
        if color in [ball.get_color() for ball in self.ball_list]:
            self.score += 1
            self.answer -= 1
            self.status_message = "Correct!"
            balls_to_remove = [ball for ball in self.ball_list if color == ball.get_color()]
            button_to_remove = [button for button in self.button_list if button.color == color]
            for ball in balls_to_remove:
                ball.delete_sound()
                self.ball_list.remove(ball)
            for button in button_to_remove:
                self.button_list.remove(button)
            self.__redraw()
        else:
            a = [ball.get_color() for ball in self.ball_list]
            print(color, a)
            self.lives -= 1
            self.status_message = "Wrong!"
            if self.lives <= 0:
                self.game_result = False
                self.game_end = True
                turtle.clear()
                turtle.penup()
                turtle.goto(0, self.canvas_height // 3)
                turtle.color("black")
                turtle.write("Game Over!!", align="center", font=("Arial", 14, "bold"))
                turtle.update()
                time.sleep(2)
        self.status_message_time = time.time()

    def check_click(self, x, y):
        for button in self.button_list:
            if button.is_clicked(x, y):
                self.handle_button_click(button.note_color)

    def __predict(self, a_ball):
        if a_ball is None:
            return

        # particle-particle collisions
        for i in range(len(self.ball_list)):
            dt = a_ball.time_to_hit(self.ball_list[i])
            # insert this event into pq
            heapq.heappush(self.pq, event.Event(self.t + dt, a_ball, self.ball_list[i]))

        # particle-wall collisions
        dtX = a_ball.time_to_hit_vertical_wall()
        dtY = a_ball.time_to_hit_horizontal_wall()
        heapq.heappush(self.pq, event.Event(self.t + dtX, a_ball, None))
        heapq.heappush(self.pq, event.Event(self.t + dtY, None, a_ball))

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def __draw_ui(self):
        # Game Status (Score and Live)
        turtle.penup()
        turtle.goto(-self.canvas_width, self.canvas_height + 40)
        turtle.color("black")
        turtle.write(f"Score: {self.score}   Lives: {self.lives}", font=("Arial", 16, "bold"))

        # Status of Answer (Correct or Wrong)
        if self.status_message and time.time() - self.status_message_time < 1:  # Show for 1 second
            turtle.penup()
            turtle.goto(0, self.canvas_height // 2 - 60)
            turtle.color("red" if self.status_message == "Wrong!" else "green")
            turtle.write(self.status_message, align="center", font=("Arial", 14, "bold"))


    def __redraw(self):
        turtle.clear()
        self.__draw_border()
        self.__draw_ui()
        for i in range(len(self.ball_list)):
            self.ball_list[i].draw()
        for i in range(len(self.button_list)):
            self.button_list[i].draw()
        turtle.update()
        heapq.heappush(self.pq, event.Event(self.t + 1.0/self.HZ, None, None))

    def run(self):
        def on_click(x, y):
            self.check_click(x, y)

        turtle.onscreenclick(on_click)

        # initialize pq with collision events and redraw event
        for i in range(len(self.ball_list)):
            self.__predict(self.ball_list[i])
        heapq.heappush(self.pq, event.Event(0, None, None))
        while (True):
            e = heapq.heappop(self.pq)
            if not e.is_valid():
                continue

            ball_a = e.a
            ball_b = e.b

            # update positions, and then simulation clock
            for i in range(len(self.ball_list)):
                self.ball_list[i].move(e.time - self.t)
            self.t = e.time

            if (ball_a is not None) and (ball_b is not None):
                ball_a.bounce_off(ball_b)
            elif (ball_a is not None) and (ball_b is None):
                ball_a.bounce_off_vertical_wall()
            elif (ball_a is None) and (ball_b is not None):
                ball_b.bounce_off_horizontal_wall()
            else:
                self.__redraw()

            self.__predict(ball_a)
            self.__predict(ball_b)
            if self.answer < self.score:
                self.game_result = True
                self.game_end = True
                turtle.clear()
                turtle.penup()
                turtle.goto(0, 0)
                turtle.color("black")
                turtle.write("You Win!!", align="center", font=("Arial", 14, "bold"))
                turtle.update()
                time.sleep(2)


        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()

if __name__ == "__main__":
    num_balls = 2
    my_Game = PerfectPitch(num_balls)
    my_Game.run()