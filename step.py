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
        (pygame.image.load("assets/penguin-0.png"), 0, 160),
        (pygame.image.load("assets/snowman.png"), 6400, 160),
]

puddles = [ x for x in range(300, 6400 - 640, 600) ]

pudimg = [
        pygame.image.load("assets/puddle.png"),
        pygame.image.load("assets/splash.png"),
]

xv = 0
yv = 0

def step(screen):
    global assets
    global puddles
    global xv, yv
    global pudimg

    dirtiness = 0

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
            if event.key == pygame.K_d:
                for puddle in puddles:
                    print(f"Puddle {puddle}: {puddle + assets[0][1]}")

    # Do Game Logic
    if assets[1][2] < 160:
        if yv <= 0:
            yv -= 1
    else:
        if yv <= 0:
            yv = 0
    if yv > 0:
        yv = 10 - ((160 - assets[1][2]) // 10)

    image, x, y = assets[0]
    x -= xv
    assets[0] = (image, x, y)
    image, x, y = assets[1]
    y -= yv
    if y > 160:
        y = 160
    assets[1] = (image, x, y)
    assets[2] = (assets[2][0], 6220 + assets[0][1], 160)

    for i in range(0, len(puddles)):
        puddle = puddles[i]
        dirtiness += puddle % 10
        if puddle % 10 == 0:
            if puddle + assets[0][1] <= 165 and puddle + assets[0][1] >= -165:
                if assets[1][2] > 150:
                    print("You got splashed")
                    puddles[i] += 1

    image, x, y = assets[1]
    if dirtiness > 5:
        dirtiness = 5
    image = pygame.image.load("assets/penguin-%d.png" % dirtiness)
    assets[1] = (image, x, y)

    # Update Objects
    for asset in assets:
        screen.blit(asset[0], asset[0].get_rect().move(asset[1], asset[2]))
    for puddle in puddles:
        screen.blit(pudimg[puddle % 10], pudimg[0].get_rect().move(puddle + assets[0][1], 0))
    pygame.display.flip()

    # Return New State
    if assets[0][1] == -(6400 - 400):
        return dirtiness + 1
    else:
        return 0

