import random
import time
import sys
from rum import Room
from funktioner import nytt_rum
from funktioner import try_again
def hittad(location, pocket):
    
    rum=["bedroom upstairs","bathroom upstairs","room with the stairs,","tv room","office room","guest room","hallway","bathroom","room with a staircase","kitchen","liviningroom","bedroom","front door"]
    if location.get_platsname()=="hallway" or location.get_platsname()=="bathroom" or location.get_platsname()=="room with a staircase" or location.get_platsname()=="kitchen" or location.get_platsname()=="liviningroom" or location.get_platsname()=="bedroom" or location.get_platsname()=="front door":
        man=rum[random.randint(6,12)]
    elif location.get_platsname()=="bedroom upstairs" or location.get_platsname()=="bathroom upstairs" or location.get_platsname()=="room with the stairs" or location.get_platsname()=="tv room" or location.get_platsname()=="office room" or location.get_platsname()=="guest room":
        man=rum[random.randint(0,5)]
    

    if man==location.get_platsname():
        print('\n'*4)
        time.sleep(3)
        print(('All of a sudden, you hear that someone is on their way into the room...').center(170))
        print('\n'*4)

        while True:
            time.sleep(2)
            svar=input("You have the following options: \n(1) Hide in the room \n(2) Stand still and be quiet \n \nEnter your choice: ")
            if svar=="1":
                print(('You are hiding...').center(170))
                time.sleep(5)
                val=random.randint(1,3)
                if val==1:
                    print(('The man sees you and manages to catch you...').center(170))
                    print('\n'*5)
                    print(('GAME OVER').center(170))
                    slut=try_again()
                    return slut

                elif val==2 or val==3:
                    print(('A man walks right next to you...').center(170))
                    print(('But the man does not see you and moves on to another room!').center(170))
                    time.sleep(4)
                    break
                else:
                    print("You did not enter any of the options... Try again:")
            if svar=="2":
                print(('You stand still without making a sound').center(170))
                time.sleep(5)
                val=random.randint(1,3)

                if val==1:
                    print(('The man comes in and finds you').center(170))
                    print(('GAME OVER').center(170))
                    slut=try_again()
                    return slut

                elif val==2 or val==3:
                    print(('The man walk past and into another room').center(170))
                    time.sleep(4)
                    break
                else:
                    print("You did not enter any of the options... Try again:")
            else:
                print("You did not enter any of the options... Try again:")
