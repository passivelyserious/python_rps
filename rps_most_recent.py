import random
from random import randint
import math
import sys
import csv

stats = {}
stats['name']   = ''
stats['wins']   = 0
stats['losses'] = 0
stats['ties']   = 0

rounds = 1

finished = False

def confirm_new_game():
    print('*** Warning! You have saved game statistics. Starting a new game will')
    print('    erase your old statistics.')
    while True:
        try:
            print()
            response = input('Continue with a new game (Y/N)? ')
        except KeyboardInterrupt:
            print("\n")
            print("You pressed Ctrl-C")
        except EOFError:
            print()
            print("You pressed Ctrl-Z")
        else:
            print()
            if response in {'Y', 'y'}:
                stats['wins']   = 0
                stats['losses'] = 0
                stats['ties']   = 0
                return True
            elif response in {'N', 'n'}:
                return False

def finish():
    save_game()
    global finished
    finished = True
    return

def get_name():
    print('')
    while True:
        try:
            stats['name'] = input("What is your name? ")
        except IOError:
            return False
        else:
            print()
            break
    print('')
    print('Hello ' + stats['name'] + '. Lets play!')
    gameplay()

def save_game():
    filename = stats['name'] + '.rps'
    try:
        fn = open(filename, 'w', newline='')
    except:
        return False
    else:
        writer = csv.writer(fn, quoting=csv.QUOTE_NONNUMERIC)
        field = ['']*4
        field[0] = stats['name']
        field[1] = int(stats['wins'])
        field[2] = int(stats['losses'])
        field[3] = int(stats['ties'])
        writer.writerow(field)
        fn.close()
        return True
    pass
    sys.exit()
    quit()

def load_game():
    get_name()
    load_file = stats['name'] + '.rps'
    try:
        open_load_file = open(load_file, 'r')
    except:
        return False
    else:
        reader = csv.reader(open_load_file, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            stats['name'] = row[0]
            stats['wins'] = row[1]
            stats['losses'] = row[2]
            stats['ties'] = row[3]
            rounds = row[4]
        open_load_file.close()
        return True
    print('')
    print('Welcome back', load_file,'. Lets play!')
    gameplay()

def end_of_gameplay_menu():
    while True:
        print("What would you like to do?")
        print("\n1. Play Again")
        print("2. View Statistics")
        print("3. Quit")
        print('')
        end_menu = input("Enter choice: ")
        if end_menu == ("1"):
            gameplay()
        elif end_menu == ("2"):
            view_statistics()
        elif end_menu == ("3"):
            save_game()
        else:
            print("An error occured. Oh noes!")
            return
        

def gameplay():

    global rounds

    computer = [randint(0,2)]

    player = False
    while player == False:
        print('')
        print("Round", rounds)
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player_choice = input("\n What will it be? ")
        print('')
        if player_choice == computer:
            stats['ties'] += 1
            rounds += 1
            print("It's a tie!")
            end_of_gameplay_menu()
        elif player_choice == ("1"):
            if computer == (3):
                print("You chose Rock. The computer chose Paper. You lose!")
                stats['losses'] += 1
                rounds += 1
            else:
                print("You chose Rock. The computer chose Scissors. You win!")
                stats['wins'] += 1
                rounds += 1
        elif player_choice == ("2"):
            if computer == (2):
                print("You chose Paper. The computer chose Scissors. You lose!")
                stats['losses'] += 1
                rounds += 1
            else:
                print("You chose Paper. The computer chose Rock. You win!")
                stats['wins'] += 1
                rounds += 1
        elif player_choice == ("3"):
            if computer == (1):
                print("You chose Scissors. The computer chose Rock. You lose!")
                stats['losses'] += 1
                rounds += 1
            else:
                print("You chose Scissors. The computer chose Paper. You win!")
                stats['wins'] += 1
                rounds += 1
        else:
            print("That's not a valid entry!")
        player = True
    print('')
    end_of_gameplay_menu()
        
def user_input():
    while True:
        print('Welcome to Rock, Paper, Scissors!')
        print('')
        print('1. Start New Game')
        print('2. Load Game')
        print('3. Quit')
        print('')
        choice = input('Enter choice: ')
        if choice == '1':
            get_name()
        elif choice == '2':
            load_game()
        elif choice == '3':
            save_game()
        else:
            print('I did not recognize your command')
            return

def view_statistics():
    message = stats['name'] + ', here are your game play statistics...'
    if stats['losses'] == 0:
        ratio = 0.0
    else:
        ratio = float(stats['wins'] / stats['losses'])
    print()
    print(message)
    print('Wins:', str(stats['wins']))
    print('Losses:', str(stats['losses']))
    print('Ties:', str(stats['ties']))
    print('Win/Loss Ratio:{:>5.2}'.format(ratio))

def main():
    # main loop
    while not finished:
        user_input()
    return

if __name__ == "__main__":
    main()
