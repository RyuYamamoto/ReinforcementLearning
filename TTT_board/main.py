#!/usr/bin/env python
# -*- coding: utf-8 -*-

from board_display import *
import numpy as np
import sys
import time

if __name__ == "__main__":
    board = BoardDisplay()

    place = 0
    mouse = 0,0
    while True:
        place = board.draw(mouse)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse = event.pos
                place = board.check_place(mouse)
                print place
