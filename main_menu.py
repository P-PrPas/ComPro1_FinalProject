import harmonic_ball
import turtle
from turtle import Screen
import perfect_pitch
import intervals
import random
import heapq
import event
import pygame.midi
import time

class Menu:
    def __init__(self):
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.screen = Screen()
        self.currency = 0
        self.stage_clear = 0
        self.intervals_stage_clear = 0
        self.level = 1
        self.num_balls = 1
        self.button_list = []

    def get_currency(self):
        return self.currency

    def get_stage_clear(self):
        return self.stage_clear

    def set_currency(self, new_currency):
        self.currency = new_currency

    def set_stage_clear(self, new_stage_clear):
        self.stage_clear = new_stage_clear

    def update_currency_and_stage(self, result, mode):
        if result:
            if mode == "Perfect Pitch":
                self.currency += 1
                self.stage_clear += 1
            else:
                self.currency += 1
                self.intervals_stage_clear += 1


    def random_num_balls(self):
        if self.stage_clear+1 <= 2:
            self.num_balls = random.randint(1, 3)
        elif self.stage_clear > 2 and self.stage_clear <= 5:
            self.num_balls = random.randint(2, 5)
        else:
            self.num_balls = random.randint(3, 10)

    def consider_level(self, mode):
        if mode == "Perfect Pitch":
            if self.stage_clear + 1 <= 2:
                self.level = 1
            elif self.stage_clear + 1 > 2 and self.stage_clear + 1 <= 5:
                self.level = 2
            elif self.stage_clear + 1 > 5 and self.stage_clear + 1 <= 7:
                self.level = 3
            elif self.stage_clear + 1 > 7 and self.stage_clear + 1 <= 10:
                self.level = 4
            elif self.stage_clear + 1 > 10 and self.stage_clear + 1 <= 13:
                self.level = 5
            else:
                self.level = 6
        else:
            if self.intervals_stage_clear + 1 <= 2:
                self.level = 1
            elif self.intervals_stage_clear + 1 > 2 and self.intervals_stage_clear + 1 <= 5:
                self.level = 2
            elif self.intervals_stage_clear + 1 > 5 and self.intervals_stage_clear + 1 <= 7:
                self.level = 3
            elif self.intervals_stage_clear + 1 > 7 and self.intervals_stage_clear + 1 <= 10:
                self.level = 4
            elif self.intervals_stage_clear + 1 > 10 and self.intervals_stage_clear + 1 <= 13:
                self.level = 5
            else:
                self.level = 6

    def clear_binding(self):
        turtle.onkey(None, "1")
        turtle.onkey(None, "2")
        turtle.onkey(None, "3")
        turtle.onkey(None, "m")
        turtle.onkey(None, "n")
        turtle.onkey(None, "a")
        turtle.onkey(None, "b")

    def start_game(self):
        pygame.mixer.stop()
        self.clear_binding()
        self.consider_level("Perfect Pitch")
        self.random_num_balls()
        my_Game = perfect_pitch.PerfectPitch(self.num_balls, self.level, self.stage_clear)
        game_result = my_Game.run()
        self.update_currency_and_stage(game_result, "Perfect Pitch")
        self.show_menu()

    def start_intervals_game(self):
        pygame.mixer.stop()
        self.clear_binding()
        self.consider_level("Intervals")
        self.random_num_balls()
        my_Game = intervals.Intervals(self.level, self.intervals_stage_clear)
        game_result = my_Game.run()
        self.update_currency_and_stage(game_result, "Intervals")
        self.show_menu()

    def show_perfect_pitch_instructions(self):
        self.clear_binding()
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(0, 325)
        turtle.write("Perfect Pitch Instructions", align="center", font=("Arial", 24, "bold"))
        turtle.goto(-300, 275)
        turtle.write("Objective", align="center",
                     font=("Arial", 20, "bold"))
        turtle.goto(25, 235)
        turtle.write("Identify the musical notes produced by the bouncing balls within the box.", align="center",
                     font=("Arial", 16, "normal"))
        turtle.goto(-300, 185)
        turtle.write("How to Play", align="center",
                     font=("Arial", 20, "bold"))
        turtle.goto(25, 100)
        turtle.write("- Watch the screen as balls bounce inside the box.\n"
                     "- Each time a ball hits a wall or another ball, it will produce a musical note.\n"
                     "- Listen carefully to identify the notes being played.", align="center",
                     font=("Arial", 16, "normal"))
        turtle.goto(-240, 50)
        turtle.write("Answering the Notes",
                     align="center",
                     font=("Arial", 20, "bold"))
        turtle.goto(-90, -15)
        turtle.write("Click on the button below with the English letters \n"
                     "representing the following notes.", align="center",
                     font=("Arial", 16, "normal"))
        turtle.goto(280, -50)
        turtle.write("C: Do, C#: Do+, D: Re, \nEb: Me-, E: Me, F: Fa,\n"
                     "F#: F+, G: Sol, Ab: La-, \nA: La, Bb: Te-, B: T", align="center",
                     font=("Arial", 16, "normal"))
        turtle.goto(50, -225)
        turtle.write("The symbols #/b or +/- are written for understanding. \n"
                     "Denotes a higher or lower sound. Normally every sound is separated by 2 semi tones,\n"
                     "for example the sounds C and D are separated by 2 semi tones.\n"
                     "The #/b symbol increases or decreases the pitch of the sound by one semi tone.\n "
                     "The # symbol means that the sound is a half a tone higher.\n"
                     "Conversely, the symbol b means that the sound is a half tone lower.", align="center",
                     font=("Arial", 16, "normal"))

        turtle.goto(0, -280)
        turtle.write("Press 'M' to return to the menu.", align="center", font=("Arial", 18, "normal"))
        turtle.goto(0, -330)
        turtle.write("Press 'N' to return to the all instruction page.", align="center", font=("Arial", 18, "normal"))
        turtle.onkey(self.show_menu, "m")
        turtle.onkey(self.show_instructions, "n")
        turtle.listen()

    def show_intervals_instruction(self):
        self.clear_binding()
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(0, 325)
        turtle.write("Intervals Instructions", align="center", font=("Arial", 24, "bold"))
        turtle.goto(-300, 275)
        turtle.write("What are Intervals?", align="center",
                     font=("Arial", 20, "bold"))
        turtle.goto(25, 120)
        turtle.write("- An interval is the distance between two musical notes.\n"
                     "- In simple terms, it describes how far apart the pitches of two notes are.\n"
                     "- The game focuses on these three intervals:\n"
                     "   - Major 3rd: A happy and bright sound. Example: C to E (Do to Mi).\n"
                     "   - Perfect 5th: A strong and balanced sound. Example: C to G (Do to Sol).\n"
                     "   - Octave: The same note, but one higher or lower in pitch. Example: C to C (Do to Do).", align="center",
                     font=("Arial", 16, "normal"))
        turtle.goto(-345, 80)
        turtle.write(" How to Play", align="center",
                     font=("Arial", 20, "bold"))
        turtle.goto(0, -200)
        turtle.write("1.Listen to the Notes:\n"
                     "   - Two balls will be released in the box.\n"
                     "   - When the balls collide or bounce against walls, they will play two notes.\n"
                     "2.Identify the Interval:\n"
                     "   - Pay attention to the relationship between the two notes.\n"
                     "   - Decide whether the interval is: Major 3rd, Perfect 5th, Octave\n"
                     "3.Submit Your Answer:\n"
                     "   - After the notes are played, choose the correct interval using the options provided.\n"
                     "4.Scoring System:\n"
                     "   - You earn points for each correct answer.\n", align="center",
                     font=("Arial", 16, "normal"))

        turtle.goto(0, -250)
        turtle.write("Press 'M' to return to the menu.", align="center", font=("Arial", 18, "normal"))
        turtle.goto(0, -300)
        turtle.write("Press 'N' to return to the all instruction page.", align="center", font=("Arial", 18, "normal"))
        turtle.onkey(self.show_menu, "m")
        turtle.onkey(self.show_instructions, "n")
        turtle.listen()

    def show_level_detail(self):
        self.clear_binding()
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(0, 325)
        turtle.write("Level Detail", align="center", font=("Arial", 24, "bold"))
        turtle.goto(-200, 275)
        turtle.write("In this game we will have 6 levels.", align="center", font=("Arial", 20, "normal"))
        turtle.goto(15, -50)
        turtle.write("   Level 1 (Stage 1 - 2): At this level, there are only 8 notes you will hear\n"
                     "starting from Do - Te according to the C Major scale.\n\n"
                     "   Level 2 (Stage 3 - 5): In this scale, there are 12 notes you will hear,\n"
                     "with #/b added according to the Chromatics scale.\n\n"
                     "   Level 3 (Stage 5 - 7): At this level, the notes you hear will have the same 12 notes,\n"
                     "but with the addition of the next octave of that sound. \n"
                     "If counted together, there would be 24 notes at this level.\n\n"
                     "   Level 4 (Stage 7 - 10): This level has the same number of sounds as the first level,\n"
                     "but the color of the ball will be covered. \n",
                     align="center",
                     font=("Arial", 16, "normal"))
        turtle.goto(15, -120)
        turtle.color("red")
        turtle.write("*Anyone who has gotten to this point by memorizing colors must have used their ears*\n\n",align="center",
                     font=("Arial", 16, "normal"))
        turtle.goto(30, -260)
        turtle.color("white")
        turtle.write("   Level 5 (Stage 10 - 13): The number of notes in this level is the same as in level 2,\n"
                     "but the colors of the balls are muted.\n\n"
                     "   Level 6 (Stage 13 and up): The number of notes in this level is the same as in level 3,\n"
                     "but the colors of the balls are muted.\n\n",align="center",
                     font=("Arial", 16, "normal"))
        turtle.goto(250, -250)
        turtle.color("red")
        turtle.write("    ***If you can make it to Level 6,\n"
                     "your ears might be turning golden.***",
                     align="center",
                     font=("Arial", 14, "normal"))
        turtle.goto(0, -300)
        turtle.color("white")
        turtle.write("Press 'M' to return to the menu.", align="center", font=("Arial", 18, "normal"))
        turtle.goto(0, -350)
        turtle.write("Press 'N' to return to the all instruction page.", align="center", font=("Arial", 18, "normal"))
        turtle.onkey(self.show_menu, "m")
        turtle.onkey(self.show_instructions, "n")
        turtle.listen()


    def show_instructions(self):
        self.clear_binding()
        self.on_menu = False
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()

        self.draw_shadow_text(0, 300, "Instructions", 46, "white", "purple")

        self.animate_text(0, 210, "What game mode do you want to learn?", "white")
        self.animate_text(0, 120, "A) Perfect Pitch", "white")
        self.animate_text(-28, 30, "B) Intervals", "white")
        self.animate_text(-5, -60, "C) Level Detail", "white")
        self.animate_text(0, -160, "Press A, B or C button on your keyboard.", "white")

        turtle.tracer(0)
        turtle.onkey(self.show_menu, "m")
        turtle.onkey(self.show_perfect_pitch_instructions, "a")
        turtle.onkey(self.show_intervals_instruction, "b")
        turtle.onkey(self.show_level_detail, "c")
        turtle.listen()

    def animate_text(self, x, y, text, color):
        ani_text = turtle.Turtle()
        ani_text.hideturtle()
        ani_text.penup()
        turtle.penup()
        for i in range(0, 10):
            ani_text._tracer(1)
            ani_text.goto(x, y + i)
            ani_text.color(color)
            ani_text.write(text, align="center", font=("Arial", 24, "bold"))
            ani_text.clear()
        turtle.goto(x, y)
        turtle.write(text, align="center", font=("Arial", 24, "bold"))

    def draw_shadow_text(self,x, y, text, size, text_color, shadow_color):
        # Draw Shadow
        turtle.penup()
        turtle.goto(x + 3, y - 3)
        turtle.pendown()
        turtle.color(shadow_color)
        turtle.write(text, align="center", font=("Arial", 46, "bold"))

        # Draw Text
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(text_color)
        turtle.write(text, align="center", font=("Arial", 46, "bold"))

    def show_menu(self):
        pygame.mixer.stop()
        bg_sound = pygame.mixer.Sound("Sound/bg.wav")
        bg_sound.set_volume(0.5)
        bg_sound.play(-1)
        turtle.bgpic("Image/bg.gif")
        self.clear_binding()
        turtle.clear()
        turtle.bgcolor("lightblue")
        turtle.tracer(0)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-350, 350)
        turtle.color("white")
        turtle.write(f"Stage Clear: {self.stage_clear}", align="center", font=("Arial", 16, "normal"))
        turtle.goto(-340, 315)
        turtle.write(f"Intervals Stage Clear: {self.intervals_stage_clear}", align="center", font=("Arial", 16, "normal"))
        turtle.goto(350, 350)
        turtle.write(f"Coins: {self.currency}", align="center", font=("Arial", 16, "normal"))

        self.draw_shadow_text(0, 180, "Harmonic Bounce", 46, "white", "purple")
        turtle.penup()
        turtle.goto(300, 260)
        turtle.write("( っ'-')╮ =͟͟͞͞🏀", align="center", font=("Arial", 24, "bold"))

        # Draw Option

        self.animate_text(0, 90, "1: Start Perfect Pitch Game 🦻", "white")
        self.animate_text(-30, 0, "2: Start Intervals Game 🎵", "white")
        self.animate_text(-70, -90, "3: Instructions 🗒️", "white")

        self.animate_text(0, -200, "Press the corresponding number.", "white")

        turtle.tracer(0)
        turtle.onkey(self.start_game, "1")
        turtle.onkey(self.start_intervals_game, "2")
        turtle.onkey(self.show_instructions, "3")
        turtle.listen()

if __name__ == "__main__":
    main_game = Menu()
    main_game.show_menu()
    turtle.done()
