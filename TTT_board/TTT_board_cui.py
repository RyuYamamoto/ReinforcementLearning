# -*- coding: utf-8 -*-

import random

PLAYER1 = 'Human'
PLAYER2 = 'AI'
DISP_EMPTY   = '-'
DISP_MARU    = "○"
DISP_BATU    = "×"
EMPTY   = 0
MARU    = 1
BATU    = -1

class TTT_board:
    def __init__(self, player1, player2):
        self.field          = []
        self.display_field  = []
        self.win            = None
        self.lose           = None
        self.player1        = player1
        self.player2        = player2

        print ('[' + DISP_MARU + ' ]' + self.player1 + ' vs ' + '[' + DISP_BATU + ']' + self.player2 + ']\n')

        for i in range(9):self.field.append(EMPTY)
        for i in range(9):self.display_field.append(DISP_EMPTY)

    def print_field(self):
        row = ' {} | {} | {} '
        hr = '\n-----------\n'

        print((row + hr + row + hr + row).format(*self.display_field))

    def check_field(self, place):
        if self.field[place-1] == MARU or self.field[place-1] == BATU:
            return False
        else:
            return True

    def set_place(self, place, turn_player):
        if turn_player == self.player1:
            self.field[place-1]           = MARU
            self.display_field[place-1]   = DISP_MARU
            return self.player2
        else:
            self.field[place-1]           = BATU
            self.display_field[place-1]   = DISP_BATU
            return self.player1

    def check_winner(self):
        maru_count = 0
        batu_count = 0
        win_condition = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

        for i in win_condition:
            for j in i:
                if self.field[j-1] == MARU:
                    maru_count = maru_count + 1
                elif self.field[j-1] == BATU:
                    batu_count = batu_count + 1
            if maru_count == 3:
                self.win    = self.player1
                self.lose   = self.player2
                return True
            elif batu_count == 3:
                self.win    = self.player2
                self.lose   = self.player1
                return True
            maru_count = batu_count = 0

        return False

class TTT_Agent(TTT_board):
    def __init__(self, player1, player2):
        TTT_board.__init__(self, player1, player2)

    def random_player_acition(self, turn_player): 
        return random.randint(1,9)

class TTT_Facilitator(TTT_Agent):
    def __init__(self, turn_player, player1, player2):
        TTT_Agent.__init__(self, player1, player2)
        self.turn_player    = turn_player
        self.place          = 0
        self.count          = 0
    
    def game_progress(self):
        self.print_field()
        while self.count < 9:
            if self.turn_player == "Human":
                while 1:
                    self.place = int(input("["+self.turn_player+"]: place > "))
                    if self.place<10 and 0<self.place:
                        if self.check_field(self.place) is True:
                            break
                        else:
                            print ("Already exist.")
                    else:
                        print ("Invalid input.")
                self.turn_player = self.set_place(self.place, self.turn_player)
                self.print_field()
                if self.check_winner() is True:
                    break
                self.count = self.count + 1
            elif self.turn_player == "AI":
                while 1:
                    print ("["+self.turn_player+"]")
                    self.place = self.random_player_acition(self.turn_player)
                    if self.check_field(self.place) is True:
                        break
                self.turn_player = self.set_place(self.place, self.turn_player)
                self.print_field()
                if self.check_winner() is True:
                    break
                self.count = self.count + 1

        if self.win == self.player1:
            print (self.player1 + " Win.")
        elif self.win == self.player2:
            print (self.player2 + " Win.")
        elif self.win == None and self.lose == None:
            print ("Draw.")

if __name__ == '__main__':
    ttt = TTT_Facilitator(PLAYER1, PLAYER1, PLAYER2)

    ttt.game_progress()
