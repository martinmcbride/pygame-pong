# Author:  Martin McBride
# Created: 2022-08-28
# Copyright (c) 2022, Martin McBride
# License: MIT

import pygame as pg
from sprites import Ball, Bat
from hud import Hud

class Game:
    pass

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

# Create score/lives display

hud = Hud(game)

# Game loop

game.score = 0
game.lives = 3
game.running = True
game.paused = True

# Start the clock
clock = pg.time.Clock()

while game.running:

    # Check all events in queue
    for event in pg.event.get():

        # If a quit event occurs, reset running flag
        if event.type == pg.QUIT:
            game.running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                game.paused = False

    delta_time = clock.tick(60)
    screen.fill((0, 0, 0))
    if not game.paused:
        game.all_sprites.update(delta_time)
        game.all_sprites.draw(screen)
    hud.update(screen)
    pg.display.flip()
