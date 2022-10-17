import random


class RockPaperScissors:

    moves = ['rock', 'paper', 'scissors']

    with open('rating.txt', 'r') as f:
        players = {item[0]: int(item[1]) for item in [line.strip().split() for line in f]}

    def main(self):
        rating = self.check_rating()
        set_of_moves = input()
        self.moves = self.moves if set_of_moves == '' else [item for item in set_of_moves.split(',')]
        print('''Okay, let's start''')
        while True:
            user_choice = input()
            computer_choice = random.choice(self.moves)
            if user_choice == '!exit':
                print('Bye!')
                exit()
            elif user_choice == '!rating':
                print('Your rating: {}'.format(rating))
            elif user_choice in self.moves:
                rating = self.game(user_choice, computer_choice, rating)
            else:
                print('Invalid input')

    def check_rating(self):
        name = input('Enter your name:')
        rating = self.players[name] if name in self.players else 0
        print('Hello, {}'.format(name))
        return rating

    def game(self, user_choice, computer_choice, rating):
        picked = self.moves.index(user_choice)
        new_moves = (self.moves * 2)[picked + 1:picked + len(self.moves)]
        if computer_choice == user_choice:
            print('There is a draw ({})'.format(computer_choice))
            rating += 50
        elif computer_choice in new_moves[:len(new_moves) // 2]:
            print('Sorry, but the computer chose {}'.format(computer_choice))
        else:
            print('Well done. The computer chose {} and failed'.format(computer_choice))
            rating += 100
        return rating


if __name__ == '__main__':
    RockPaperScissors().main()
