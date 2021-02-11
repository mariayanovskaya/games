import getpass
import string

class hangman:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.guesser = None
        self.setter = None
        self.word = None
        self.alphabet_d = {letter:0 for letter in string.ascii_lowercase}
        self.display_word = None

    def set_word(self):
        #resetting the alphabet tracker for the game
        self.alphabet_d = {letter:0 for letter in string.ascii_lowercase}
        players = [self.player1 , self.player2]
        # inputting the word to be guessed
        setter = input('Which player wants to set the word?') # TODO: make this game access random words (scrape a dictionary?) so it can be a one player game

        if setter in players:
            word = getpass.getpass('Enter your word:')
            self.word = word
            self.display_word = ['#']*len(self.word)
            self.setter = setter
        else:
            print('not a valid player')
            self.set_word()


        if setter == self.player1:
            print(f'{self.player2} is guessing')
            self.guesser = self.player2
        elif setter == self.player2:
            print(f'{self.player1} is guessing')
            self.guesser = self.player1


    def hangman_stage(self, stage = 0):
        zero = '''            \n             \n            \n           \n              \n            \n____________'''
        dead = '''    _____   \n   |     |    \n   |     o   \n   |    /|\ \n   |    / \    \n   |         \n____________'''
        one = '''            \n   |          \n   |         \n   |        \n   |           \n   |         \n____________'''
        two = '''    _____   \n   |          \n   |         \n   |        \n   |           \n   |         \n____________'''
        three = '''    _____   \n   |     |    \n   |        \n   |     \n   |        \n   |         \n____________'''
        four = '''    _____   \n   |     |    \n   |     o   \n   |     \n   |        \n   |         \n____________'''
        five = '''    _____   \n   |     |    \n   |     o   \n   |     | \n   |        \n   |         \n____________'''
        six = '''    _____   \n   |     |    \n   |     o   \n   |    /| \n   |        \n   |         \n____________'''
        seven = '''    _____   \n   |     |    \n   |     o   \n   |    /|\ \n   |        \n   |         \n____________'''
        eight = '''    _____   \n   |     |    \n   |     o   \n   |    /|\ \n   |    /     \n   |         \n____________'''
        comment = '''You lost!'''
        list_stage = [zero, one, two, three, four, five, six, seven, eight, dead, comment]
        alive = True
        while alive == True:
            yield list_stage[stage]
            stage +=1
            if stage == len(list_stage):
                alive = False


    def alphabet(self, letter = ''):
        '''has a '''
        alpbt = self.alphabet_d
        used = False
        if letter in alpbt and alpbt[letter] == 0:
            alpbt[letter] = 1
            used = False
        elif letter in alpbt and alpbt[letter] == 1:
            print(f'Letter {letter} has already been used, choose another!')
            used = True
        return alpbt, used

    def guessing_word(self, letter, death_condition):
        word_list = list(self.word)
        result = True
        for n, l in enumerate(word_list):
            if letter == l:
                print(f'Letter {letter} is in the word!')
                self.display_word[n] = letter
                result = True

        if letter not in word_list:
            print(f'Letter {letter} is not in the word!')
            print(death_condition.__next__())
            result = False
        #print(result)
        return result



    def attempt(self, death_condition ):
        result = True

        print(f'{self.display_word}')
        guess = input('your letter:')
        alpbt, used = self.alphabet(guess)
        if used == True:
            self.attempt(death_condition)
        else:
            result = self.guessing_word(guess, death_condition)
        #print(result)
        return result

    def game(self):
        self.set_word()
        death_condition = self.hangman_stage()
        death_countdown = 0
        game_on = True
        alive = True
        win = False
        while game_on == True:
            result = self.attempt(death_condition)
            if '#' not in self.display_word:
                win = True
                print(f'{self.guesser} won!')
                print(f'The word was {(self.word).upper()}')
            elif result == False:
                death_countdown += 1
                if death_countdown== 10:
                    print(f'{self.setter} won!')
                    print(f'The word was {(self.word).upper()}')
                    alive = False
            elif '#' in self.display_word:
                continue
            if alive ==False or win == True:
                game_on = False


if __name__ == '__main__':
    p1 = input("Player 1: ")
    p2 = input("Player 2: ")
    h = hangman(p1, p2)
    h.game()