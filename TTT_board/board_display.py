#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import copy
import pygame
from pygame.locals import *

MASU = 70

class BoardDisplay:
    def __init__(self):
        pygame.init()
        
        self.board_x            = MASU * 3
        self.board_y            = MASU * 3
        self.board_size         = Rect(0,0,self.board_x,self.board_y)
        self.screen             = pygame.display.set_mode(self.board_size.size)
        self.font               = pygame.font.SysFont("timesnewroman",22)
        pygame.display.set_caption("TTT Board")

    def draw(self, mouse):
        for j in range(3):
	    for i in range(3):
                pygame.draw.rect(self.screen, (250,250,250), Rect(i*MASU,j*MASU,MASU,MASU))
		pygame.draw.rect(self.screen, (50,50,50), Rect(i*MASU,j*MASU,MASU,MASU),1)
        #return self.check_place(mouse)
				
    def check_place(self, mouse):
        x, y = mouse
	place = 0
        if 0<y and y<MASU:
	    if 0<x and x<MASU:
		place = 1
	    elif MASU<x and x<MASU*2:
		place = 2
	    elif MASU*2<x and x<MASU*3:
		place = 3
	elif MASU<y and y<MASU*2:
	    if 0<x and x<MASU:
		place = 4
	    elif MASU<x and x<MASU*2:
		place = 5
	    elif MASU*2<x and x<MASU*3:
		place = 6
	elif MASU*2<y and y<MASU*3:
	    if 0<x and x<MASU:
		place = 7
	    elif MASU<x and x<MASU*2:
		place = 8
	    elif MASU*2<x and x<MASU*3:
		place = 9
	return place
'''
  def show_policy(self, q_table):
			for x in range(self.row):
        for y in range(self.colmun):
          action = np.array(q_table[:,x,y])
          max_q_action = action.argmax()
          direction = ""
          if max_q_action == 0:
            direction = u"←"
          elif max_q_action == 1:
            direction = u"↓"
          elif max_q_action == 2:
            direction = u"→"
          elif max_q_action == 3:
            direction = u"↑"
					color = (q_table[:,x,y].max()/3.0)*255.0
          pygame.draw.rect(self.screen, (255,255-color,255-color), Rect(y*MASU,x*MASU, MASU,MASU))
          self.screen.blit(self.font.render(direction, True, (125,125,125)), (y*MASU+MASU/3,x*MASU+MASU/4))
'''
