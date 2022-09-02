# Author:  Martin McBride
# Created: 2022-08-28
# Copyright (c) 2022, Martin McBride
# License: MIT

import pygame as pg

class Hud:

    def __init__(self, game):
        self.game = game

    def update(self, screen):
        font = pg.font.Font(None, 30)
        text = font.render("Score: " + str(self.game.score), 1, (255, 255, 0))
        screen.blit(text, (10, 10))
        font = pg.font.Font(None, 30)
        text = font.render("Lives: " + str(self.game.lives), 1, (255, 255, 0))
        screen.blit(text, (550, 10))
        if self.game.paused:
            font = pg.font.Font(None, 60)
            text = font.render("Press enter to continue " + str(self.game.score), 1, (255, 255, 255))
            screen.blit(text, (10, 10))

