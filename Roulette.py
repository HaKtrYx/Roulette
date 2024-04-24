import random  # Import the random module to generate random numbers
import time  # Import the time module to add delays

# Define the initial balance and lists for different betting options
balance = 1000
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
row1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
row2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
row3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
low = list(range(1, 13))
mid = list(range(13, 25))
high = list(range(25, 37))
lower = list(range(1, 19))
upper = list(range(19, 37))


def placeBet():
    """
    Function to prompt the user to place their bets on different options.
    It updates the global variables for each bet amount.
    """
    global bet_red, bet_black, bet_even, bet_odd, bet_row1, bet_row2, bet_row3, bet_low, bet_mid, bet_high, bet_lower, bet_upper, bet
    print("Your current Balance is\t\t\t: ", balance, "\n")
    bet_red = int(input("Amount on Red\t\t\t\t: "))
    bet_black = int(input("Amount on Black\t\t\t\t: "))
    bet_even = int(input("Amount on Even\t\t\t\t: "))
    bet_odd = int(input("Amount on Odd\t\t\t\t: "))
    bet_row1 = int(input("Amount on Row 1 (3,6,...)\t\t\t: "))
    bet_row2 = int(input("Amount on Row 2 (2,5,...)\t\t\t: "))
    bet_row3 = int(input("Amount on Row 3 (1,4,...)\t\t\t: "))
    bet_low = int(input("Amount on 1-12\t\t\t\t: "))
    bet_mid = int(input("Amount on 13-24\t\t\t\t: "))
    bet_high = int(input("Amount on 25-36\t\t\t\t: "))
    bet_lower = int(input("Amount on 1-18\t\t\t\t: "))
    bet_upper = int(input("Amount on 19-36\t\t\t\t: "))
    bet = bet_red + bet_black + bet_even + bet_odd + bet_row1 + bet_row2 + bet_row3 + bet_low + bet_mid + bet_high + bet_upper + bet_lower

def LuckyWheel():
    """
    Function to generate a random lucky number between 0 and 36.
    It prints the lucky number with a red color if it's a red number.
    """
    global lucky_number
    lucky_number = random.randint(0, 36)
    if lucky_number in red:
        print("__________________________________ \n The lucky number is: \033[31m", lucky_number, "\033[0m \n__________________________________")
    else:
        print("__________________________________ \n The lucky number is: ", lucky_number, "\n__________________________________")

def Payout():
    """
    Function to calculate the payout based on the lucky number and the user's bets.
    It updates the global variables for the result and balance.
    """
    global result, balance
    result = 0
    if lucky_number in red:
        result += bet_red * 2
    if lucky_number in black:
        result += bet_black * 2
    if lucky_number in even:
        result += bet_even * 2
    if lucky_number in odd:
        result += bet_odd * 2
    if lucky_number in upper:
        result += bet_upper * 2
    if lucky_number in lower:
        result += bet_lower * 2
    if lucky_number in row1:
        result += bet_row1 * 3
    if lucky_number in row2:
        result += bet_row2 * 3
    if lucky_number in row3:
        result += bet_row3 * 3
    if lucky_number in high:
        result += bet_high * 3
    if lucky_number in mid:
        result += bet_mid * 3
    if lucky_number in low:
        result += bet_low * 3

def game():
    """
    Main function to run the game loop.
    It calls the other functions, updates the balance, and handles the game over condition.
    """
    global balance, bet, result
    while True:
        print('\n' * 100)  # Clear the console
        placeBet()
        LuckyWheel()
        if balance < bet:
            print("*********************************\n\033[31m Error: Your Balance is too small \033[0m\n*********************************")
            time.sleep(3)
            print('\n' * 100)
        else:
            balance -= bet
            Payout()
            balance += result
            if balance == 0:
                print("You have no balance left. \033[1mGame over.\033[0m")
                print("""'   .----------------.  .----------------.  .----------------.  .----------------. 
'  | .--------------. || .--------------. || .--------------. || .--------------. |
'  | |    ______    | || |      __      | || | ____    ____ | || |  _________   | |
'  | |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |
'  | | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |
'  | | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |
'  | | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |
'  | |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |
'  | |              | || |              | || |              | || |              | |
'  | '--------------' || '--------------' || '--------------' || '--------------' |
'   '----------------'  '----------------'  '----------------'  '----------------' 
'   .----------------.  .----------------.  .----------------.  .----------------. 
'  | .--------------. || .--------------. || .--------------. || .--------------. |
'  | |     ____     | || | ____   ____  | || |  _________   | || |  _______     | |
'  | |   .'    `.   | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | |
'  | |  /  .--.  \  | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | |
'  | |  | |    | |  | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | |
'  | |  \  `--'  /  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | |
'  | |   `.____.'   | || |     \_/      | || | |_________|  | || | |____| |___| | |
'  | |              | || |              | || |              | || |              | |
'  | '--------------' || '--------------' || '--------------' || '--------------' |
'   '----------------'  '----------------'  '----------------'  '----------------' """)
                break
            elif result > 0:
                print("You won:\t\t\t\t ", result)
            else:
                print("\033[31m You lose \033[0m")
            time.sleep(3)
            print('\n' * 100)

# Call the game function to start the game
game()
