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

width, height = size = (320, 240)

screen = pygame.display.set_mode(size)

try:
    while True:
        step()

except KeyboardInterrupt:
    print
    print "You told me to die so I'm dying now."

