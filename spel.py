from rum import Room
from val import choice
from funktioner import pick_up_object
from funktioner import nytt_rum
from funktioner import door
from Man import hittad
from funktioner import intro
import sys
def make_temp_dict(file):                  
    temp_dict = {}                   
    for line in file:
        new_line = line.strip('\n')
        lista = new_line.split(';')
        room = Room(lista)
        temp_dict[room.get_plats()] = room
    return temp_dict

def create_graph(temp_dict):               
    for v in temp_dict.values():           
        if v.get_n() != 0:
            v.set_n(temp_dict[v.get_n()])
        else:
            v.set_n(None)
        if v.get_s() != 0:
            v.set_s(temp_dict[v.get_s()])
        else:
            v.set_s(None)
        if v.get_e() != 0:
            v.set_e(temp_dict[v.get_e()])
        else:
            v.set_e(None)
        if v.get_w() != 0:
            v.set_w(temp_dict[v.get_w()])
        else:
            v.set_w(None)    
file = open('speltext.txt','r')
temp_dict = make_temp_dict(file)            
create_graph (temp_dict)
while True:
                        
    location = temp_dict[1]
    pocket = []
    intro()
    while True:
        door(location,pocket)
        nytt_rum(location)
        pick_up_object(location, pocket)
        slut=hittad(location, pocket)
        if slut==1:
            break
        elif slut==0:
            sys.exit()
        location=choice(location, pocket)
