import random

# Function to simulate rolling a die
def roll_die():
    return random.randint(1, 6)

# Function to play a single game of dice
def play():
    # Roll two dice
    roll = roll_die() + roll_die()

    # Check the outcome of the first roll
    if roll in [2, 3, 12]:
        return "lose"
    elif roll in [7, 11]:
        return "win"
    else:
        point = roll
        while True:
            roll = roll_die() + roll_die()
            if roll == 7:
                return "lose"
            elif roll == point:
                return "win"

# Function to play multiple games of dice
def playMultipleGames(num_games, bet):
    total_winnings = 0

    for _ in range(num_games):
        result = play()
        if result == "win":
            total_winnings += 2 * bet
        else:
            total_winnings -= bet

    print(f"Total Winnings: ${total_winnings}")

# Main function to run the program
def main():
    bet_amount = -1
    while bet_amount < 0:
        bet = input("Enter your bet amount: ")
        try:
            bet_amount = int(bet)
            if bet_amount < 0:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    number_of_games = int(input("Enter the number of games to play: "))
    playMultipleGames(number_of_games, bet_amount)

if __name__ == "__main__":
    main()
    
