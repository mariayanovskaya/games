## naughts and crosses
class nnc:
    def __init__( self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.possible_inp =  {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}

    def game(self):
        ## refreshing the board
        self.possible_inp = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
        ## setting the turn queue - the game automatically finishes after 9 turns
        turn_q = 0
        game_on = True
        ## printing the board
        self.positions()
        while game_on == True:
            ## conditions for player 1 is for the turn que to be divisible by 2
            if turn_q%2 ==0:
                turn_x = True
                ## player 1 is always x's and always goes first
                value = 'x'
                print(f'{self.player1} turn')
                ## collecting dtring input for the position of the cross
                turn = input('your x goes to:')
                ## checking that the position entered is on the board - if not, the palyer has to re-enter
                if turn in self.possible_inp:
                    ## checking if the cell is occupied
                    turn_x = self.check_occupancy(turn)
                    ## if it isn't - put a cross there
                    if turn_x == True:
                        self.possible_inp[turn] = value
                    #print the board
                    self.positions()
                    ## check if that move won the game
                    if self.check_win(value) == True:
                        print(f'{self.player1} won!')
                        game_on = False
                else:
                    print('not a valid postion!')
                    turn_x = False
                ##checking that all conditions for a turn have been satisfied
                if turn_x == True:
                    turn_q +=1
            ## checking that the max number of turns have not been exceeded
            elif turn_q == 9:
                print('game over')
                game_on = False
            ## player 2 turn -- same as above
            else:
                turn_o = True
                value = 'o'
                print(f'{self.player2} turn')
                turn = input('your o goes to:')
                if turn in self.possible_inp:
                    turn_o = self.check_occupancy(turn)
                    if turn_o == True:
                        self.possible_inp[turn] = value
                    self.positions()
                    if self.check_win(value) == True:
                        print(f'{self.player2} won!')
                        game_on = False
                else:
                    print('not a valid postion!')
                    turn_o = False
                if turn_o == True:
                    turn_q +=1

    ## prints the positions of x's and o's
    def positions(self):
        print(f'''The board layout is:  
        
 {self.possible_inp['1']} | {self.possible_inp['2']} | {self.possible_inp['3']}      1 | 2 | 3  
-----------    -----------
 {self.possible_inp['4']} | {self.possible_inp['5']} | {self.possible_inp['6']}      4 | 5 | 6
-----------    -----------
 {self.possible_inp['7']} | {self.possible_inp['8']} | {self.possible_inp['9']}      7 | 8 | 9

enter a number for desired postion\n''')

    ## win conditions
    def check_win(self, value):
        win = False
        if value in self.possible_inp['1'] and value in self.possible_inp['2'] and value in self.possible_inp['3']:
            win = True
        elif value in self.possible_inp['4'] and value in self.possible_inp['5'] and value in self.possible_inp['6']:
            win = True
        elif value in self.possible_inp['7'] and value in self.possible_inp['8'] and value in self.possible_inp['9']:
            win = True
        elif value in self.possible_inp['1'] and value in self.possible_inp['5'] and value in self.possible_inp['9']:
            win = True
        elif value in self.possible_inp['1'] and value in self.possible_inp['4'] and value in self.possible_inp['7']:
            win = True
        elif value in self.possible_inp['2'] and value in self.possible_inp['5'] and value in self.possible_inp['8']:
            win = True
        elif value in self.possible_inp['3'] and value in self.possible_inp['6'] and value in self.possible_inp['9']:
            win = True
        elif value in self.possible_inp['3'] and value in self.possible_inp['5'] and value in self.possible_inp['7']:
            win = True
        return win

    #checkinf occupancy
    def check_occupancy(self, imp):
        if self.possible_inp[imp] != ' ':
            print("Can't do that - the cell is occupied!\n")
            return False
        else:
            return True

if __name__ == '__main__':
    p1 = input("Crosses player: ")
    p2 = input("Noughts player: ")
    n = nnc(p1, p2)
    n.game()