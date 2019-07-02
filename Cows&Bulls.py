import random

print("Welcome to the Cows and Bulls Game!")
username = input("Please, enter your name: ")

comp_num = "".join(str(i) for i in random.sample(range(0, 10), k=4))

print(comp_num)

def checking(user_guess, comp_num, user):
    attempts = 1
    while True:
        if user_guess.lower() == "exit":
          if attempts == 2:
            print("\nLOOSER !!! Ha - Ha \n\n{}, you have made {} attempt.".format(user, attempts - 1))
            break
          elif attempts == 1:
              print("\nWoow!!! {}, you are such a quiter. SHAME! You have made {} attempts.".format(user, attempts - 1))
              break
          else:
              print("\nLOOSER !!! Ha - Ha \n\nYou have made", attempts - 1, "attempts.")
              break
        else:
            bulls = 0
            cows = 0
            if user_guess.isdigit() != True:
                print("\nHey, {}! Only digits!".format(user))
            elif len(user_guess) > 4:
                print("\nYour number must be exact 4 digits!")
            elif len(user_guess) < 4:
                print("\nYour number must be exact 4 digits!")
            elif len(set(user_guess)) < 4:
                print("\nA, a, aaa! Cheater!\nYour number must be with 4 different digits!")
            elif user_guess.isdigit():
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
                        print("\nYou have {} Cow and {} Bull".format(cows, bulls))
                    else:
                        print("You have {} Cow and {} Bulls".format(cows, bulls))
                elif cows > 1:
                    if bulls > 1:
                        print("You have {} Cows and {} Bulls.".format(cows, bulls))
                    else:
                        print("You have {} Cows and {} Bull.".format(cows, bulls))
                elif cows == 0:
                    if bulls == 1:
                        print("You have 0 Cows and 1 Bull.")
                    elif bulls == 4:
                        print("You have 4 Bulls!\nCongratulation!\nYOU WIN!\n\nYou have made {} attempts".format(attempts))
                        break
                    else:
                        print("You have 0 Cows and {} Bulls.".format(bulls))
                attempts += 1
            user_guess = input("Guess the number. Enter a four digit number or type Exit to quit: ")

if __name__ == "__main__":
    user_guess = input("Guess the number. Enter a four digit number or type Exit to quit the game: ")
print(checking(user_guess, comp_num, username))
