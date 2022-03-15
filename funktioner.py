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
    objektval=input("Do you want to search the room for any objects?")
    if objektval=="1":
        if location.get_object() != 'No objects':
            if location.get_object() not in pocket:
                print((f'You see a {location.get_object()}.').center(170))
                choice_object = input(f'You have the following options:\n(1) Pick up {location.get_object()}\n(2) Do not pick up the {location.get_object()}.\nEnter your choice: ')

                if choice_object == str(1):
                    föremål_ryggsäck = pocket.append(location.get_object())
                    return föremål_ryggsäck
                    
            else:
                return
            
        else:
            print("No objects were found.")
           
    elif objektval=="2":
        return
    else:
        print("You did not enter any of the options... Try again:")


def door(room,pocket):
    if room.get_plats()==13:
        print("\n"*15)
        print(("The door has a padlock, you need to enter the correct sequence of numbers to GET OUT?").center(170))
        print("\n"*3)
        while True:
            doorchoice=input("You have the following options:\n(1) Enter the code\n(2) Stop trying\n\nEnter your choice: ")
            print("\n"*3)
            if doorchoice=="1":
                print("In your pockets there is")
                for elem in pocket:
                    print ("a",elem)
                    print("\n")
                code=input("Write the correct code(4 numbers):")
                if code=="7241":
                    print(("The door opened and you got out of the house!").center(170))
                    sys.exit()
                else: 
                    print(("You entered the wrong code").center(170))
                    time.sleep(2)
            elif doorchoice=="2":
                break
            else:
                print("You did not enter any of the options... Try again:")
