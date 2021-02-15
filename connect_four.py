#from IPython.display import clear_output
import os

class connect4:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.board = [[' ']*6+[0],
                      [' ']*6+[1],
                      [' ']*6+[2],
                      [' ']*6+[3],
                      [' ']*6+[4],
                      [' ']*6+[5],
                      [' ']*6+[6]]
        self.marker = 'X'
        self.winner = None

    # this is horrifying - implement pygame IMMEDIATELY
    @staticmethod
    def display_board(l):
        print(f'''
Current board layout is:
|{l[0][6]} {l[1][6]} {l[2][6]} {l[3][6]} {l[4][6]} {l[5][6]} {l[6][6]}|
---------------
|{l[0][5]} {l[1][5]} {l[2][5]} {l[3][5]} {l[4][5]} {l[5][5]} {l[6][5]}|
|{l[0][4]} {l[1][4]} {l[2][4]} {l[3][4]} {l[4][4]} {l[5][4]} {l[6][4]}|
|{l[0][3]} {l[1][3]} {l[2][3]} {l[3][3]} {l[4][3]} {l[5][3]} {l[6][3]}|
|{l[0][2]} {l[1][2]} {l[2][2]} {l[3][2]} {l[4][2]} {l[5][2]} {l[6][2]}|
|{l[0][1]} {l[1][1]} {l[2][1]} {l[3][1]} {l[4][1]} {l[5][1]} {l[6][1]}|
|{l[0][0]} {l[1][0]} {l[2][0]} {l[3][0]} {l[4][0]} {l[5][0]} {l[6][0]}|
---------------
''')

    def turn(self):
        print(f'''It's {self.marker}'s turn! ''' )
        inp = int(input('Your disc goes into:'))
        self.check_occupancy_n_fill(inp, self.marker)



    def check_occupancy_n_fill(self, inp, turn):
        for n, column in enumerate(self.board):
            if inp == column[6]:
                if ' ' not in column[0:6]:
                    print('column occupied, choose another')
                    self.turn()
                for m, place in enumerate(column):
                    if place != ' ':
                        continue
                    elif place == ' ':
                        self.board[n][m] = turn
                        break





    def next_turn(self):
        if self.marker == 'X':
            self.marker = 'O'
            self.winner = self.player2
        else:
            self.marker = 'X'
            self.winner = self.player1

    def win_conditions(self, winner, l):
        win = False
        #marker conditions
        marker = None
        if winner == self.player1:
            marker = 'X'
        else:
            marker = 'O'
        # horizontals
        for i in range(4):
            for r in range(6):
                #print('marker',marker)
                #print(l[i][r], l[i+1][r], l[i+2][r], l[i+3][r])
                if marker in l[i][r] and marker in l[i+1][r] and marker in l[i+2][r] and marker in l[i+3][r]:
                    #print('THIS WORKS')
                    win = True
        #verticals
        for c in range(7):
            for p in range(3):
                if marker in l[c][p] and marker in l[c][p+1] and marker in l[c][p+2] and marker in l[c][p+3]:
                    win = True


        #diagonals - left up
        for c in range(4):
            for p in range(3):
                if marker in l[c][p+3] and marker in l[c+1][p+2] and marker in l[c+2][p+1] and marker in l[c+3][p]:
                    win = True
                elif marker in l[c][p] and marker in l[c+1][p+1] and marker in l[c+2][p+2] and marker in l[c+3][p+3]:
                    win = True



        return win




    def game(self):
        self.board = [[' ']*6+[0],
                      [' ']*6+[1],
                      [' ']*6+[2],
                      [' ']*6+[3],
                      [' ']*6+[4],
                      [' ']*6+[5],
                      [' ']*6+[6]]
        turn_no = 1
        game_on = True
        win = False
        while game_on == True:


            if turn_no < 19:
                self.display_board(self.board)
                self.turn()
                win = self.win_conditions(self.winner, self.board)
                print(win)
                if win == True:
                    self.display_board(self.board)
                    print(f'{self.winner} won!')
                    break
                self.next_turn()
                turn_no += 1
                # clear_output() # this doesn't work in terminal
            elif turn_no == 19:
                self.display_board(self.board)
                print('''It's a tie!''')
                break

if __name__ == '__main__':
    p1 = input("Player 1: ")
    p2 = input("Player 2: ")
    c = connect4(p1, p2)
    c.game()