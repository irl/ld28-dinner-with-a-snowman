# Dinner with a Snowman
#
# Copyright (c) 2013, Iain R. Learmonth <irl@sdf.org>
# All rights reserved.
#
# For redistribution and use terms, see the LICENSE file.
#

import sys, pygame

assets = [
        (pygame.image.load("assets/bg.png"), 0, 0),
        (pygame.image.load("assets/penguin.png"), 0, 160),
]

xv = 0
yv = 0

def step(screen):
    global xv, yv

    # Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xv = 10
            if event.key == pygame.K_UP and assets[1][2] >= 160:
                yv = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                xv = 0
            if event.key == pygame.K_UP:
                yv = 0

    # Do Game Logic
    if assets[1][2] < 160:
        if yv <= 0:
            yv -= 1
    else:
        if yv <= 0:
            yv = 0
    if yv > 0:
        yv = 10 - ((160 - assets[1][2]) / 10)

    image, x, y = assets[0]
    x -= xv
    assets[0] = (image, x, y)
    image, x, y = assets[1]
    y -= yv
    if y > 160:
        y = 160
    assets[1] = (image, x, y)

    # Update Objects
    for asset in assets:
        screen.blit(asset[0], asset[0].get_rect().move(asset[1], asset[2]))
    pygame.display.flip()

    # Return New State
    return 0

