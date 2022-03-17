import sys
import time
def nytt_rum(room):
    print('\n' * 100)
    if room.get_plats !=13:
        print((f'You enter the {room.get_platsname()} and look around.').center(170))
    else:
        print("You stand in front of the front door")
    print('\n' * 1)
    print((room.get_info()).center(170))
    

    #time.sleep(3)
    #time.sleep(1.5)
    if room.get_wname() !='':
        print((f'the room to your left is the {room.get_wname()}').center(170))

    #time.sleep(1.5)
    if room.get_nname() !='':
        print((f'the room infront of you is the {room.get_nname()}').center(170))

    #time.sleep(1.5)
    if room.get_ename() !='':
        print((f'the room to your right is the {room.get_ename()}').center(170))

    #time.sleep(1.5)
    if room.get_sname() !='':
        print((f'the room behind you is the {room.get_sname()}').center(170))
    #time.sleep(1.5)
    print('\n' * 1)


def pick_up_object(location, pocket):
    if location.get_object() != 'No objects':
        while True:
            if location.get_object() not in pocket:
                print((f'You find a {location.get_object()}.').center(170))
                choice_object = input(f'You have the following options:\n(1) Pick up \n(2) Do not pick up\n\nEnter your choice: ')

                if choice_object == str(1):
                    föremål_ryggsäck = pocket.append(location.get_object())
                    print('\n' * 50)
                    print((f'You pick up the {location.get_object()} and put it in your pocket.').center(170))
                    print((f'You are still in the {location.get_platsname()}.').center(170))
                    return föremål_ryggsäck
                    
                elif choice_object == str(2):
                    break
            
                else:
                    print("You did not enter any of the options... Try again:\n")
            else:
                break

def door(room,pocket):
    if room.get_platsname()=='front door':
        print("\n"*50)
        print(("The door has a padlock, you need to enter the correct sequence of numbers to GET OUT OF THE HOUSE").center(170))
        print("\n"*3)
        while True:
            doorchoice=input("You have the following options:\n(1) Enter the code\n(2) Stop trying\n\nEnter your choice: ")
            print("\n"*3)
            if doorchoice=="1":
                
                print('\n' * 50)
                print("In your pockets there is")
                for elem in pocket:
                    if pocket != []:
                        print ("- a",elem)
                        
                print(('You now have this padlock infront of you.\n').center(170))
                print(('|1|2|3|').center(170))
                print(('|4|5|6|').center(170))
                print(('|7|8|9|').center(170))
                print(('|0|').center(170))
                print('\n')
                print(('The correct code consists of 4 digits.').center(170))
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
    print(("You wake up in a scary house at night").center(170))
    print(("You hear something moving around upstairs").center(170))
    print(("Your objective is to get out without being caught").center(170))
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

