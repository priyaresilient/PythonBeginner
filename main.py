import random

if __name__ == '__main__':



    def game():
        user = input(f'r for Rock s for Scissors p for paper')
        computer = random.choice(['r', 's', 'p'])

        if user == computer:
            return 'Tie'

        if is_win(user, computer):
            return 'You WON!'

        return 'You Lost!'

    def is_win(user, computer):
        if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
            return True

print(game())