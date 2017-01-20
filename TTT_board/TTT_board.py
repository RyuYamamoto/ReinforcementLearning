# coding: utf-8

PLAYER1 = 'Human'
PLAYER2 = 'Human'
EMPTY   = '-'
MARU    = "○"
BATU    = "×"

class TTT_board:
    def __init__(self, player1='Human', player2='AI'):
        self.field      = []
        self.win        = None
        self.lose       = None
        self.player1    = player1
        self.player2    = player2

        print ('[' + self.player1 + ' vs ' + self.player2 + ']\n')

        for i in range(9):self.field.append(EMPTY)

    def print_field(self):
        row = ' {} | {} | {} '
        hr = '\n-----------\n'

        print((row + hr + row + hr + row).format(*self.field))

class TTT_Agent:
    def __init__(self, mode='RANDOM'):
        self.mode = mode

if __name__ == '__main__':
    ttt = TTT_board(PLAYER1, PLAYER2)

    ttt.print_field()
