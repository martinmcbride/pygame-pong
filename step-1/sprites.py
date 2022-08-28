# Author:  Martin McBride
# Created: 2022-08-28
# Copyright (c) 2022, Martin McBride
# License: MIT

import pygame as pg

class Ball(pg.sprite.Sprite):

    def __init__(self, pos):
        super(Ball, self).__init__()
        self.image = pg.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass

class Bat(pg.sprite.Sprite):

    def __init__(self, pos):
        super(Bat, self).__init__()
        self.image = pg.image.load('bat.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass
