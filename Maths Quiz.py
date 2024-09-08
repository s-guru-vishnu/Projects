import random
from time import *
import time


OPERATOR = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator =  random.choice(OPERATOR)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

correct = 0
input("PLEASE CLICK ENTER TO START! : ")
print("Starts in 3...")
sleep(1)
print("2...")
sleep(1)
print("1...")
sleep(1)
print("GO...")
print("_______________________________")
print()

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem No." + str(i+1) + " : " + expr + " = ")
        if guess == str(answer):
            break
        correct += 1

end_time = time.time()
total_time = end_time - start_time

mark = []

if total_time <= 20:
    mark.append("Good")
elif 21 <= total_time <= 30:
    mark.append("Average")
elif 31 <= total_time <= 40:
    mark.append("Bad")
else:
    mark.append("Very Bad")

print("_______________________________")
print(f"Your Cracked this course in {total_time}seconds! with {mark} Score")
print("Thank you for play my Maths game!")


