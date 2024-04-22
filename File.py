
collected_rooms = []
current_room = ''


def dragonGame(dictionary_rooms, _direction):

    _direction = _direction.upper()

    #-- check if letter is E is entered
    if( _direction == 'E'):
        current_room = 'Great  Hall'
        collected_rooms.append('Great Hall')
        print("You did it!")
    elif(_direction != 'E'):
        print('Theres a wall here')

    print("Here is thye collected_room: ", collected_rooms)

    # while(collected_rooms != 2):



    




   


def main():
    rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'},
    'Upper Level': {'South':  'Great Hall', 'East': 'Attic'},
    
    }

 
    
   
    print(rooms)




    print('Welcome to the game. You are at Start.\n')
    user_direction = input('Press E (East) to move to the Great Hall.\n')
    dragonGame(rooms, user_direction)

 



    
# Using the special variable
# __name__
if __name__=="__main__":
    main()