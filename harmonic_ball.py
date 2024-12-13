import pygame
import pygame.midi
import threading
import turtle
import math
import time


pygame.init()
pygame.midi.init()


class Ball:
    def __init__(self, size, x, y, vx, vy, color, note, name):
        self.name = name
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = 100 * size ** 2
        self.count = 0
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.sound_file = note
        self.is_answer = False

        # Load the sound file to the mixer
        self.sound = pygame.mixer.Sound(self.sound_file)
        # We use the channel to solve the problem of the ball hitting the wall in rapid succession,
        # it does not make a sound.
        self.channel = pygame.mixer.find_channel()

    def get_color(self):
        return self.color

    def play_sound(self):
        if self.channel and self.is_answer == False:
            self.channel.play(self.sound)

    def stop_sound(self):
        if self.is_answer == False:
            self.channel.stop()

    def delete_sound(self):
        self.stop_sound()
        self.is_answer = True

    # Code from AJ.Paruj
    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def bounce_off_vertical_wall(self):
        self.vx = -self.vx
        self.count += 1
        self.play_sound()

    def bounce_off_horizontal_wall(self):
        self.vy = -self.vy
        self.count += 1
        self.play_sound()

    def bounce_off(self, that):
        dx = that.x - self.x
        dy = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dv_dr = dx * dvx + dy * dvy  # dv dot dr
        dist = self.size + that.size  # distance between particle centers at collison

        # magnitude of normal force
        magnitude = 2 * self.mass * that.mass * dv_dr / ((self.mass + that.mass) * dist)

        # normal force, and in x and y directions
        fx = magnitude * dx / dist
        fy = magnitude * dy / dist

        # update velocities according to normal force
        self.vx += fx / self.mass
        self.vy += fy / self.mass
        that.vx -= fx / that.mass
        that.vy -= fy / that.mass

        # update collision counts
        self.count += 1
        that.count += 1

        # play sound
        self.play_sound()
        that.play_sound()

    def distance(self, that):
        x1 = self.x
        y1 = self.y
        x2 = that.x
        y2 = that.y
        d = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return d

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def time_to_hit(self, that):
        if self is that:
            return math.inf
        dx = that.x - self.x
        dy = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dv_dr = dx*dvx + dy*dvy
        if dv_dr > 0:
            return math.inf
        dv_dv = dvx*dvx + dvy*dvy
        if dv_dv == 0:
            return math.inf
        dr_dr = dx*dx + dy*dy
        sigma = self.size + that.size
        d = (dv_dr*dv_dr) - dv_dv * (dr_dr - sigma*sigma)
        '''if dr_dr < sigma*sigma:
            print("overlapping particles")'''
        if d < 0:
            return math.inf
        t = -(dv_dr + math.sqrt(d)) / dv_dv

        # should't happen, but seems to be needed for some extreme inputs
        # (floating-point precision when dvdv is close to 0, I think)
        if t <= 0:
            return math.inf

        return t

    def time_to_hit_vertical_wall(self):
        if self.vx > 0:
            return (self.canvas_width - self.x - self.size) / self.vx
        elif self.vx < 0:
            return (self.canvas_width + self.x - self.size) / (-self.vx)
        else:
            return math.inf

    def time_to_hit_horizontal_wall(self):
        if self.vy > 0:
            return (self.canvas_height - self.y - self.size) / self.vy
        elif self.vy < 0:
            return (self.canvas_height + self.y - self.size) / (-self.vy)
        else:
            return math.inf

    def __repr__(self):
        return (f"|--------------------------------|\n"
                f"Name : {self.name} \n"
                f"Position : ({self.x}, {self.y}) \n"
                f"Color : {self.color} \n"
                f"Note : {self.sound_file}\n"
                f"Size : {self.size}\n"
                f"Velocity : ({self.vx}, {self.vy})")
