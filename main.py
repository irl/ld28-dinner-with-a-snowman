#!/usr/bin/env python3
#
# Dinner with a Snowman
#
# Copyright (c) 2013, Iain R. Learmonth <irl@sdf.org>
# All rights reserved.
#
# For redistribution and use terms, see the LICENSE file.
#

import sys, pygame
from step import step

pygame.init()

width, height = size = (640, 480)

screen = pygame.display.set_mode(size)

try:
    # Start Screen
    start = pygame.image.load("assets/start.png")
    screen.blit(start, start.get_rect())
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

    state = 0

    while state == 0:
        state = step(screen)
        pygame.time.delay(50)

    pygame.time.delay(1000)

    winImage = None

    if state == 1:
        winImage = pygame.image.load("assets/welldone.png")
    if state > 1 and state < 4:
        winImage = pygame.image.load("assets/tryharder.png")
    if state >= 4:
        winImage = pygame.image.load("assets/toodirty.png")

    screen.blit(winImage, winImage.get_rect())

    pygame.display.flip()

    pygame.time.delay(10000)


except KeyboardInterrupt:
    print()
    print("You told me to die so I'm dying now.")

