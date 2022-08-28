# Author:  Martin McBride
# Created: 2022-08-28
# Copyright (c) 2022, Martin McBride
# License: MIT

import pygame as pg

class Ball(pg.sprite.Sprite):

    def __init__(self, pos, game):
        super(Ball, self).__init__()
        self.game = game
        self.image = pg.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 0.2
        self.direction = pg.Vector2(1, -1)

    def update(self, delta_time):
        self.rect.center += self.direction * self.speed * delta_time
        screen_size = pg.display.get_window_size()
        sprite_size = self.image.get_size()
        if self.rect.colliderect(self.game.left):
            self.direction[0] = 1
        if self.rect.colliderect(self.game.right):
            self.direction[0] = -1
        if self.rect.colliderect(self.game.top):
            self.direction[1] = 1
        if self.rect.colliderect(self.game.bottom):
            self.direction[1] = -1

class Bat(pg.sprite.Sprite):

    def __init__(self, pos, game):
        super(Bat, self).__init__()
        self.game = game
        self.image = pg.image.load('bat.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, delta_time):
        pass
