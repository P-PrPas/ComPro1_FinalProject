import harmonic_ball
import turtle
import perfect_pitch
import random
import heapq
import event
import pygame.midi
import time
import main_menu

class GameLauncher:
    def __init__(self):
        self.game_menu = main_menu.Menu()
        self.game_start_status = False

    def run(self):
        self.game_menu.show_menu()
        turtle.done()


def main():
    my_Game = GameLauncher()
    my_Game.run()

if __name__ == "__main__":
    main()