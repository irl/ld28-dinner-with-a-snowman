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

def step(screen):
    # Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Update Objects
    for asset in assets:
        screen.blit(asset[0], asset[0].get_rect().move(asset[1], asset[2]))
    pygame.display.flip()

    # Do Game Logic

    # Return New State
    return 0

