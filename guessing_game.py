import random

class player:


    def __init__(self, name):
        player.name = name

    def game(self):
        print(f'Hello, {self.name}! Guess any number between 0 and 50')
        n = random.randint(0,50)
        n_guess = int(input('your guess here:'))
        att = 2 #number of attempts
        while att >0:
            if n_guess == n:
                print('Win!')
                att = -1
            elif n_guess > n:
                att -= 1
                print(f'Thats not it! Try a smaller number! No of attempts left: {att}' )
                if att > 0 :n_guess = int(input('your new guess here:'))
            elif n_guess < n:
                att -= 1
                print(f'Thats not it! Try a bigger number! No of attempts left: {att}' )
                if att > 0 :n_guess = int(input('your new guess here:'))

        print(f'Game over! The number was {n}')


if __name__ == "__main__":
    name = input("Please Enter your name: ")
    m = player(name)
    m.game()