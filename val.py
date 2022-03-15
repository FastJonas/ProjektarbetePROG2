

def choice(location, ryggsäck):
    global val

    while True:
        val_lista = ['1','2','3','4']
        print('\nYou have the following options:')
        if location.get_wname() != '':
            print(f'({val_lista.pop(0)}) Go to the {location.get_wname()}')
        
        if location.get_nname() != '':    
            print(f'({val_lista.pop(0)}) Go to the {location.get_nname()}') 
        
        if location.get_ename() !='':
            print(f'({val_lista.pop(0)}) Go to the {location.get_ename()}')
        
        if location.get_sname() !='':
            print(f'({val_lista.pop(0)}) Go to the {location.get_sname()}')


        val=input("\nEnter your choice: ")
        
        if val==str(1):
            if location.get_wname() != '':
                new_location=location.get_w()
                return new_location

            elif location.get_wname() == '' and location.get_nname() != '':
                new_location=location.get_n()
                return new_location

            elif location.get_wname() == '' and location.get_nname() == '' and location.get_ename() != '':
                new_location=location.get_e()
                return new_location

            elif location.get_wname() == '' and location.get_nname() == '' and location.get_ename() == '' and location.get_sname() != '':
                new_location=location.get_s()
                return new_location

            else:
                print('There is no room in that direction! Try again:')
        
        elif val==str(2):
            if location.get_wname() != '' and location.get_nname() != '':
                new_location=location.get_n()
                return new_location


            elif location.get_wname() != '' and location.get_nname() == '' and location.get_ename() != '':
                new_location=location.get_e()
                return new_location


            elif location.get_wname() == '' and location.get_nname() != '' and location.get_ename() != '':
                new_location=location.get_e()
                return new_location
            
            elif location.get_wname() != '' and location.get_nname() == '' and location.get_ename() == '' and location.get_sname() != '':
                new_location=location.get_s()
                return new_location
                
            elif location.get_wname() == '' and location.get_nname() != '' and location.get_ename() == '' and location.get_sname() !='':

                new_location=location.get_s()
                return new_location

            elif location.get_wname() == '' and location.get_nname() == '' and location.get_ename() != '' and location.get_sname() !='':
                new_location=location.get_s()
                return new_location


            else:
                print('There is no room in that direction! Try again:')       


        elif val==str(3):
            if location.get_wname() != '' and location.get_nname() != '' and location.get_ename() != '' and location.get_ename() != 'second floor':
                new_location = location.get_e()
                return new_location
                
            if location.get_wname() != '' and location.get_nname() != '' and location.get_ename() == 'second floor':   
                
                if 'Staircasekey' in ryggsäck:
                    new_location=location.get_e()
                    return new_location
                    
                    
                else:
                    print(('The door to the stairs is locked! You need a key to get go uppstairs!').center(170))
    
                

            elif location.get_wname() == '' and location.get_nname() != '' and location.get_ename() != '' and location.get_sname() != '':
                new_location=location.get_s()
                return new_location

            elif location.get_wname() != '' and location.get_nname() == '' and location.get_ename() != '' and location.get_sname() != '':
                new_location=location.get_s()
                return new_location
            
            elif location.get_wname() != '' and location.get_nname() != '' and location.get_ename() == '' and location.get_sname() != '':
                new_location=location.get_s()
                return new_location
                
            
            else:
                print('There is no room in that direction! Try again:')


        elif val ==str(4):
            if location.get_wname() != '' and location.get_nname() != '' and location.get_ename() != '' and location.get_sname() != '':
                new_location=location.get_s()
                return new_location

            else:
                print('There is no room in that direction! Try again:')

        else:
            print('You dit not enter any of the options! Try again:')
