# Author:  Martin McBride
# Created: 2022-08-28
# Copyright (c) 2022, Martin McBride
# License: MIT

import pygame as pg
from sprites import Ball, Bat

# Setup game

class Game:
    pass

# Setup game

screen_width = 640
screen_height = 480

# Initialise pygame
pg.init()

# Set display size
screen = pg.display.set_mode((screen_width, screen_height))

# Set window title
pg.display.set_caption('Pong')

# Create sprites

ball_sprite = Ball((100, 200))
bat_sprite = Bat((200, 400))
all_sprites = pg.sprite.RenderPlain()
all_sprites.add(ball_sprite)
all_sprites.add(bat_sprite)

# Game loop

running = True

while running:

    # Check all events in queue
    for event in pg.event.get():

        # If a quit event occurs, reset running flag
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pg.display.flip()
