# Author:  Martin McBride
# Created: 2022-08-28
# Copyright (c) 2022, Martin McBride
# License: MIT

from dataclasses import dataclass

import pygame as pg
from sprites import Ball, Bat

@dataclass
class Game:
    screen_width = None
    screen_height = None
    left = None
    right = None
    top = None
    bottom = None
    ball_sprite = None
    bat_sprite = None
    all_sprites = None
    running = None

game = Game()

# Setup game

game.screen_width = 640
game.screen_height = 480

# Initialise pygame
pg.init()

# Set display size
screen = pg.display.set_mode((game.screen_width, game.screen_height))

# Create rectangles at boundaries of the screen

game.left = pg.Rect(-100, 0, 100, game.screen_height)
game.right = pg.Rect(game.screen_width, 0, 100, game.screen_height)
game.top = pg.Rect(0, -100, game.screen_width, 100)
game.bottom = pg.Rect(0, game.screen_height, game.screen_width, 100)

# Set window title
pg.display.set_caption('Pong')

# Create sprites

game.ball_sprite = Ball((100, 200), game)
game.bat_sprite = Bat((200, 400), game)
game.all_sprites = pg.sprite.RenderPlain()
game.all_sprites.add(game.ball_sprite)
game.all_sprites.add(game.bat_sprite)

# Game loop

game.running = True

# Start the clock
clock = pg.time.Clock()

while game.running:

    # Check all events in queue
    for event in pg.event.get():

        # If a quit event occurs, reset running flag
        if event.type == pg.QUIT:
            game.running = False

    delta_time = clock.tick(60)
    screen.fill((0, 0, 0))
    game.all_sprites.update(delta_time)
    game.all_sprites.draw(screen)
    pg.display.flip()
