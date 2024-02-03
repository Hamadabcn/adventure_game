import time

def intro():
    print("Welcome to the Intelligent Adventure Game!")
    time.sleep(2)
    print("You find yourself in a mysterious room.")
    time.sleep(2)
    print("Your goal is to find the hidden treasure chest.")
    time.sleep(2)
    print("Let's begin!")

def room1():
    print("\n== Room 1 ==\n")
    print("You enter a dark room with two doors.")
    time.sleep(2)
    print("Which door do you choose? (1 or 2)")
    choice = input("> ")

    if choice == "1":
        print("You chose door 1 and see a glowing orb.")
        time.sleep(2)
        print("Do you take the orb? (yes or no)")
        choice = input("> ")

        if choice == "yes":
            print("You grab the orb and it illuminates the room.")
            time.sleep(2)
            print("You win!")
        else:
            print("You ignore the orb and the room remains dark.")
            time.sleep(2)
            print("You lose!")

    elif choice == "2":
        print("You chose door 2 and find yourself outside the room.")
        time.sleep(2)
        print("You lose!")

def room2():
    print("\n== Room 2 ==\n")
    print("You enter a room with a riddle.")
    time.sleep(2)
    print("What has keys but can't open locks?")
    time.sleep(1)
    print("Hint: It's often found on a computer.")
    time.sleep(1)
    answer = input("> ")

    if answer.lower() == "keyboard":
        print("That's correct!")
        time.sleep(2)
        print("The door opens and you proceed to the next room.")
        time.sleep(2)
        room3()
    else:
        print("That's incorrect. You lose!")

def room3():
    print("\n== Room 3 ==\n")
    print("You enter a room with a scale balance.")
    time.sleep(2)
    print("On one side, there are three heavy stones and on the other, four light stones.")
    time.sleep(2)
    print("You can only weigh the stones twice.")
    time.sleep(2)
    print("How will you determine which side has the heavier stones?")
    time.sleep(1)
    print("A) Place three stones on each side, leaving one stone aside.")
    print("B) Place four stones on each side, leaving one stone aside.")
    print("C) Place three stones on one side and four stones on the other.")
    choice = input("> ")

    if choice.lower() == "a":
        print("Incorrect choice. You lose!")
    elif choice.lower() == "b":
        print("Incorrect choice. You lose!")
    elif choice.lower() == "c":
        print("That's the correct choice!")
        time.sleep(2)
        print("The balance tips towards the side with three stones.")
        time.sleep(2)
        print("Congratulations, you found the hidden treasure chest!")
        time.sleep(2)
        print("You win!")

def main():
    intro()
    time.sleep(2)
    room1()

if __name__ == '__main__':
    main()
    