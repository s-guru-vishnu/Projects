import random

user_wins = 0
ai_wins = 0

options = ["rock", "rock", "paper", "paper", "scissors", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Try Again")
        continue

    random_number = random.randint(0, 5)
    # rock : 0, paper : 1, scissor : 2, rock : 3, paper : 4, scissor : 5
    ai_pick = options[random_number]
    print("AI picked", ai_pick)


    if user_input == "rock" and ai_pick == "scissors":
        print()
        print("                        YOU WIN!")
        print()
        user_wins += 1

    elif user_input == "scissors" and ai_pick == "paper":
        print()
        print("                        YOU WIN!")
        print()
        user_wins += 1

    elif user_input == "paper" and ai_pick == "rock":
        print()
        print("                        YOU WIN!")
        print()
        user_wins += 1

    elif user_input == "paper" and ai_pick == "paper":
        print()
        print("                        MATCH TIED!")
        print()
        
    elif user_input == "rock" and ai_pick == "rock":
        print()
        print("                        MATCH TIED!")
        print()
        
    elif user_input == "scissors" and ai_pick == "scissors":
        print()
        print("                        MATCH TIED!")
        print()
        
    elif user_input == "rock" and ai_pick == "paper":
        print()
        print("                        AI WINS!")
        print()
        ai_wins += 1
        
    elif user_input == "paper" and ai_pick == "scissors":
        print()
        print("                        AI WINS!")
        print()
        ai_wins += 1

    elif user_input == "scissors" and ai_pick == "rock":
        print()
        print("                        AI WINS!")
        print()
        ai_wins += 1

    if user_wins == 3 or ai_wins == 3:
        break

if user_wins == 3:
    print("Congralutions!,You win")

if ai_wins == 3:
    print("Sorry,You lost")

print("Good Bye!")
