from rum import Room
from val import choice
from object import pick_up_object
from funktioner import nytt_rum
from funktioner import door
from Man import hittad
from funktioner import intro
import sys
def create_dict(file):                  
    dict = {}                   
    for line in file:
        new_line = line.strip('\n')
        lista = new_line.split(';')
        room = Room(lista)
        dict[room.get_plats()] = room
    return dict

def graph(dict):               
    for x in dict.values():           
        if x.get_n() != 0:
            x.set_n(dict[x.get_n()])
        else:
            x.set_n(None)
        if x.get_s() != 0:
            x.set_s(dict[x.get_s()])
        else:
            x.set_s(None)
        if x.get_e() != 0:
            x.set_e(dict[x.get_e()])
        else:
            x.set_e(None)
        if x.get_w() != 0:
            x.set_w(dict[x.get_w()])
        else:
            x.set_w(None)    
file = open('speltext.txt','r')
dict = create_dict(file)            
graph (dict)
while True:
                        
    location = dict[1]
    pocket = []
    intro()
    while True:
        door(location,pocket)
        nytt_rum(location)
        pick_up_object(location, pocket)
        slut=hittad(location)
        if slut==1:
            break
        elif slut==0:
            sys.exit()
        location=choice(location, pocket)
