# Dinner with a Snowman
#
# Copyright (c) 2013, Iain R. Learmonth <irl@sdf.org>
# All rights reserved.
#
# For redistribution and use terms, see the LICENSE file.
#

import pygame

from world import *

def step():
    # Process Events
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()

    # Update Objects

    # Do Game Logic

    # Return New State
    return 0

