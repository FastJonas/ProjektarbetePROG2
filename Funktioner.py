import sys
import time
from notes import *
from nyckel import *
def nytt_rum(room):
    print('\n' * 100)
    if room.get_plats !=13:
        print((f'You enter the {room.get_platsname()} and look around.').center(170))
    else:
        print(("You stand in front of the front door").center(170))
    print('\n' * 1)
    print((room.get_info()).center(170))
    print("\n")
    print(("After looking around you see that").center(170))
    if room.get_wname() !='':
        print((f'the {room.get_wname()} is to your left').center(170))

    
    if room.get_nname() !='':
        print((f'the {room.get_nname()} is in front of you').center(170))

    
    if room.get_ename() !='':
        print((f'the {room.get_ename()} is to your right').center(170))

    
    if room.get_sname() !='':
        print((f'the {room.get_sname()} is behind you').center(170))
    
    print('\n' * 1)


def door(room,pocket):
    if room.get_platsname()=='front door':
        print("\n"*50)
        print(("The door has a codelock, you need to enter the correct sequence of numbers to GET OUT OF THE HOUSE").center(170))
        print("\n"*3)
        while True:
            doorchoice=input("You have the following options:\n(1) Try to enter the code\n(2) Step away from the door\n\nEnter your choice: ")
            print("\n"*3)
            if doorchoice=="1":
                
                print('\n' * 50)
                print("In your pockets there is")
                for elem in pocket:
                    if pocket != []:
                        print ("- a",elem)
                        
                print(('You now have this codelock infront of you.\n').center(170))
                print(('|1|2|3|').center(170))
                print(('|4|5|6|').center(170))
                print(('|7|8|9|').center(170))
                print(('|0|').center(170))
                print('\n')
                print(('The code consists of 4 digits.').center(170))
                print('\n'*3)
                code=input("Enter the correct code: ")
                if code=="7241":
                    print(("You entered the correct code").center(170))
                    print(("and GOT OUT OF THE HOUSE").center(170))
                    print(("Congratulations and thanks for playing <3").center(170))
                    sys.exit()
                else: 
                    print(("You entered the wrong code").center(170))
                    time.sleep(2)
                    print('\n'*50)
            elif doorchoice=="2":
                break
            else:
                print("You did not enter any of the options... Try again:")

                
               
def intro():
    print("\n"*15)
    print(("Welcome to:").center(170))
    print(("GET OUT OF THE HOUSE").center(170))
    print(("THE GAME").center(170))
    print("\n"*5)
    print(("you wake up in a scary house at night").center(170))
    print(("you hear something moving around upstairs").center(170))
    print(("your objective is to get out without being caught").center(170))
    print("\n"*3)
    time.sleep(6)
    
    
def try_again():
    while True:
        answer=input("press (1) to try again\npress (2) to exit the game\n\nenter your choice: ")
        if answer=="1":
            print(("Good luck").center(170))
            return 1
        elif answer=="2":
            print(("Thank you for playing, welcome back.").center(170))
            return 0
        else:
            print("You did not enter any of the options... Try again:")

