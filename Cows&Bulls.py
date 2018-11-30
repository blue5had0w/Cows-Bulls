import random

print("Welcome to the Cows and Bulls Game!")


comp_num = ""
while len(comp_num) <= 3:
    x = random.randint(0, 9)
    y = str(x)
    if y not in comp_num:
        comp_num += y
#print(comp_num)

def checking(user_guess, comp_num):
    attempts = 1
    while True:
        if user_guess.lower().startswith("e"):
            print("LOOSER !!!\n\nYou have made", attempts - 1, "attempts.")
            break
        else:
            bulls = 0
            cows = 0
            if len(user_guess) > 4:
                print("Your number must be exact 4 digits!")
            elif len(user_guess) < 4:
                print("Your number must be exact 4 digits!")
            else:

                if user_guess[0] == comp_num[0]:
                    bulls += 1
                if user_guess[1] == comp_num[1]:
                    bulls += 1
                if user_guess[2] == comp_num[2]:
                    bulls += 1
                if user_guess[3] == comp_num[3]:
                    bulls += 1

                if user_guess[0] in comp_num:
                    if user_guess[0] not in comp_num[0]:
                        cows += 1
                if user_guess[1] in comp_num:
                    if user_guess[1] not in comp_num[1]:
                        cows += 1
                if user_guess[2] in comp_num:
                    if user_guess[2] not in comp_num[2]:
                        cows += 1
                if user_guess[3] in comp_num:
                    if user_guess[3] not in comp_num[3]:
                        cows += 1
                if cows == 1:
                    if bulls == 1:
                        print("You have", cows, "Cow and", bulls, "Bull")
                    else:
                        print("You have", cows, "Cow and", bulls, "Bulls")
                elif cows > 1:
                    if bulls > 1:
                        print("You have", cows, "Cows and", bulls, "Bulls.")
                    else:
                        print("You have", cows, "Cows and", bulls, "Bull.")
                elif cows == 0:
                    if bulls == 1:
                        print("You have", cows, "Cows and", bulls, "Bull.")
                    elif bulls == 4:
                        print("You have", cows, "Cows and", bulls, "Bulls.\nCongratulation!\nYOU WIN!\n\nYou have made", attempts, "attempts")
                        break
                    else:
                        print("You have", cows, "Cows and", bulls, "Bulls.")
                attempts += 1
            user_guess = input("Guess the number. Enter a four digit number or type Exit to quit: ")


if __name__ == "__main__":
    user_guess = input("Guess the number. Enter a four digit number or type Exit to quit: ")
    print(checking(user_guess, comp_num))
