import random

class RockPaperScissors:
    def _init_(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def play_round(self):
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in self.choices:
                break
            else:
                print("Invalid choice. Please choose again.")

        computer_choice = random.choice(self.choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            self.user_score += 1
        else:
            print("Computer wins!")
            self.computer_score += 1

    def display_score(self):
        print(f"\nYour score: {self.user_score}")
        print(f"Computer's score: {self.computer_score}")

def main():
    game = RockPaperScissors()
    while True:
        game.play_round()
        game.display_score()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if _name_ == "_main_":
    main()
