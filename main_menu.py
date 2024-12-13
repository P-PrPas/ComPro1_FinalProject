import harmonic_ball
import turtle
import perfect_pitch
import random
import heapq
import event
import pygame.midi
import time

class Menu:
    def __init__(self):
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.currency = 0
        self.stage_clear = 0
        self.button_list = []

    def get_currency(self):
        return self.currency

    def get_stage_clear(self):
        return self.stage_clear

    def get_currency(self, new_currency):
        self.currency = new_currency

    def get_stage_clear(self, new_stage_clear):
        self.stage_clear = new_stage_clear

    def update_currency_and_stage(self, result):
        if result:
            self.currency += 1
            self.stage_clear += 1

    def start_game(self):
        num_balls = 2
        my_Game = perfect_pitch.PerfectPitch(num_balls)
        game_result = my_Game.run()
        self.update_currency_and_stage(game_result)
        self.show_menu()

    def show_instructions(self):
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(0, 200)
        turtle.write("Instructions", align="center", font=("Arial", 24, "bold"))
        turtle.goto(0, 150)
        turtle.write("The main goal of this game is to practice ear training,", align="center",
                     font=("Arial", 18, "normal"))
        turtle.goto(0, 115)
        turtle.write("which is an essential ability for musicians.", align="center",
                     font=("Arial", 18, "normal"))
        turtle.goto(0, 65)
        turtle.write("By the way, to win our game, you must use your hearing talents.", align="center",
                     font=("Arial", 18, "normal"))
        turtle.goto(0, 30)
        turtle.write("To distinguish sounds based on the following questions.", align="center",
                     font=("Arial", 18, "normal"))
        turtle.goto(0, -20)
        turtle.write("Perfect Pitch: In this game mode, the ball is released and bounces within a specific frame.", align="center",
                     font=("Arial", 17, "normal"))
        turtle.goto(0, -55)
        turtle.write("The ball produces a sound if it strikes a wall or collides with another ball.", align="center",
                     font=("Arial", 18, "normal"))
        turtle.goto(0, -90)
        turtle.write("Your job is to figure out what note the sound is.", align="center",
                     font=("Arial", 18, "normal"))

        turtle.goto(0, -200)
        turtle.write("Press 'M' to return to the menu.", align="center", font=("Arial", 18, "normal"))
        turtle.onkey(self.show_menu, "m")
        turtle.listen()

    def show_menu(self):
        turtle.clear()
        turtle.tracer(0)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-350, 350)
        turtle.write(f"Stage Clear: {self.stage_clear}", align="center", font=("Arial", 16, "normal"))
        turtle.goto(350, 350)
        turtle.write(f"Coins: {self.currency}", align="center", font=("Arial", 16, "normal"))

        turtle.goto(0, 200)
        turtle.write("Main Menu", align="center", font=("Arial", 24, "bold"))
        turtle.goto(0, 150)
        turtle.write("1: Start Game", align="center", font=("Arial", 18, "normal"))
        turtle.goto(0, 100)
        turtle.write("2: Instructions", align="center", font=("Arial", 18, "normal"))
        turtle.goto(0, 50)
        turtle.write("Press the corresponding number.", align="center", font=("Arial", 18, "normal"))
        turtle.update()

        turtle.onkey(self.start_game, "1")
        turtle.onkey(self.show_instructions, "2")
        turtle.listen()

if __name__ == "__main__":
    main_game = Menu()
    main_game.show_menu()
    turtle.done()
