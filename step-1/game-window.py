# Author:  Martin McBride
# Created: 2022-08-28
# Copyright (c) 2022, Martin McBride
# License: MIT

import pygame as pg

class Game:
    pass

game = Game()

# Setup game

game.screen_width = 640
game.screen_height = 480

# Initialise pygame
pg.init()

# Set display size
pg.display.set_mode((game.screen_width, game.screen_height))

# Set window title
pg.display.set_caption('Pong')

# Game loop

running = True

while running:

    # Check all events in queue
    for event in pg.event.get():

        # If a quit event occurs, reset running flag
        if event.type == pg.QUIT:
            running = False
