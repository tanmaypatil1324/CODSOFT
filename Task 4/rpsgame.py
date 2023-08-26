import random

def get_userchoice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_compchoice():
    return random.choice(['rock', 'paper', 'scissors'])

def det_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def gameplay():
    print("Welcome to Rock-Paper-Scissors Game!")
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_userchoice()
        computer_choice = get_compchoice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result, score = det_winner(user_choice, computer_choice)
        print(result)
        user_score += score
        computer_score -= score
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    gameplay()
