from time import *


tasks = []


def addtask():
    task = input("Enter the task that you want to add in your tasks")
    tasks.append(task)
    print(f"{task} is added in your list of tasks")
    sleep(1)

def deletetask():
    print("Tasks : ")
    for Index, task in enumerate(tasks):
        print(f"Task #{Index} . {task}")
    task = input("Enter the no. of task that you want to delete from your tasks")
    if task.isdigit():
        task = int(task)
        if 0 >= task > len(tasks):
            print("Your Input is Wrong, Please Try Again")
        elif 0 < task <= len(tasks):
            tasks.pop(task)
            print(f"{task} is removed from your list of tasks")
    else:
        print("Please enter only number...!")

def showtask():
    print("Current Tasks : ")
    for Index,task in enumerate(tasks):
        print(f"Task #{Index} . {task}")


if __name__ == "__main__":
    print("Welcome to my to-do list :)")
    while True:
        print()
        print("\nPlease select one of the following options")
        print("===========================================")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Quit")
        print("============================================")
        choice = input("Enter the Options : ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                addtask()
                sleep(1)
            elif choice == 2:
                deletetask()
                sleep(1)
            elif choice == 3:
                showtask()
                sleep(1)
            elif choice == 4:
                print("Thankyou for Using My To-Do List")
                quit()
            else:
                print("Invalid Option")
                sleep(1)
        else:
            print("Please enter only number...!")
            sleep(1)


sleep(1)
print("Thankyou for Using My To-Do List")
