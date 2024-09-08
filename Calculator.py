def Intial_calc():
    m = 1
    n = 2
    o = 3
    x = []
    y = []
    total = []

    user_input1 = float(input(f"Enter the Number {m} : "))
    Operator = input("Enter the Operator Here (+, -, *, /) : ")
    m += 1
    x.append(user_input1)
    user_input2 = float(input(f"Enter the Number {m} : "))
    n += 1
    x.append(user_input2)

    if Operator == "+":
        num1 = x[m - 2]
        num2 = x[n - 2]
        result = num1 + num2
        print(f"Answer of the Addition : {result:.2f}")
        total.append(result)

    elif Operator == "-":
        num1 = x[m - 2]
        num2 = x[n - 2]
        result = num1 - num2
        print(f"Answer of the Subtraction : {num1 - num2:.2f}")
        total.append(result)

    elif Operator == "*":
        num1 = x[m - 2]
        num2 = x[n - 2]
        result = num1 * num2
        print(f"Answer of the Multiplication: {num1 * num2:.2f}")
        total.append(result)

    elif Operator == "/":
        num1 = x[m - 2]
        num2 = x[n - 2]
        result = num1 / num2
        print(f"Answer of the Division : {num1 / num2:.2f}")
        total.append(result)

    else:
        print("Please Enter Only Operator, Try Again")
        quit()

    while True:
        Operator = input("Enter the Operator Here (+, -, *, /) (q == Quit)  : ")
        user_input = float(input(f"Enter the Number {o} : "))
        o += 1
        y.append(user_input)

        if Operator == "+":
            num1 = total[0]
            num2 = y[o - 4]
            result = num1 + num2
            print(f"Answer of the Addition : {result:.2f}")
            total.pop(0)
            total.append(result)

        elif Operator == "-":
            num1 = x[m - 2]
            num2 = x[n - 2]
            result = num1 - num2
            print(f"Answer of the Subtraction : {num1 - num2:.2f}")
            total.pop(0)
            total.append(result)

        elif Operator == "*":
            num1 = x[m - 2]
            num2 = x[n - 2]
            result = num1 * num2
            print(f"Answer of the Multiplication: {num1 * num2:.2f}")
            total.pop(0)
            total.append(result)

        elif Operator == "/":
            num1 = x[m - 2]
            num2 = x[n - 2]
            result = num1 / num2
            print(f"Answer of the Division : {num1 / num2:.2f}")
            total.pop(0)
            total.append(result)


        elif Operator == "q" or Operator == "Q":
            quit()

        else:
            print("Please Enter Only Operator, Try Again")
            quit()


if __name__ == "__main__":
    print("Welcome to Calc World!")
    print("What is the Calculation, I Want to solve for you!")
    call = Intial_calc()
