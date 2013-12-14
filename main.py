#!/usr/bin/env python2
#
# Dinner with a Snowman
#
# Copyright (c) 2013, Iain R. Learmonth <irl@sdf.org>
# All rights reserved.
#
# For redistribution and use terms, see the LICENSE file.
#

import sys,pygame
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
                waiting = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

    while True:
        step(screen)

except KeyboardInterrupt:
    print
    print "You told me to die so I'm dying now."

