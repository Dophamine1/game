import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def intro():
    print_slow("Welcome to the Adventure Game!")
    print_slow("You find yourself in a mysterious old house.")
    print_slow("Your goal is to find the hidden treasure!")
    print_slow("Let the adventure begin!\n")

def choose_path():
    print_slow("Choose your path:")
    print_slow("1. Go left")
    print_slow("2. Go right")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print_slow("Invalid choice! Please try again.")
        choose_path()

def left_path():
    print_slow("You chose the left path.")
    print_slow("You encounter a locked door.")
    print_slow("To open the door, you need a key.")
    has_key = 'key' in inventory
    if has_key:
        print_slow("You use the key to unlock the door.")
        print_slow("Congratulations! You found a chest with a precious gem inside!")
        print_slow("You win!")
    else:
        print_slow("You need a key to open the door.")
        choose_path()

def right_path():
    print_slow("You chose the right path.")
    print_slow("You enter a dark room.")
    print_slow("There's a suspicious-looking pedestal in the center.")
    print_slow("On the pedestal, there are three different colored orbs.")
    orb_choice = input("Which color orb do you take? (red/blue/green): ").lower()

    if orb_choice in ['red', 'blue', 'green']:
        inventory.append(orb_choice + ' orb')
        print_slow(f"You take the {orb_choice} orb and put it in your inventory.")
    else:
        print_slow("Invalid choice! You must choose one of the orbs.")
        right_path()

def main():
    intro()
    choose_path()

inventory = []
main()
