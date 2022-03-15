
def nytt_rum(room):
    print('\n' * 100)
    print((f'You enter the {room.get_platsname()} and look around.').center(170))
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
        if location.get_object() not in pocket:
            print((f'You see a {location.get_object()}.').center(170))
            choice_object = input(f'You have the following options:\n(1) Pick up {location.get_object()}\n(2) Do not pick up the {location.get_object()}.\nEnter your choice: ')

            if choice_object == str(1):
                föremål_ryggsäck = pocket.append(location.get_object())
                return föremål_ryggsäck

        else:
            return
