#-- just a heads up this is how you do comments
#-- always do comments and when doing comments alwasy remember
#-- they are there to guide people that have never seen your code 
#-- and they are there to guide yourself when you haven't looked at your 
#-- code in a long time. Keep that in mind when creating comments to
#-- help you in the long run



current_room = ''                                               #-- current room is a variable to hold the current variable 



rooms = {                                                       #-- This is the rooms avaiable to you during the game
    'Great Hall': {'South': 'Bedroom'},                             
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom', 'North': 'Upper Level'},
    'Upper Level': {'South':  'Great Hall', 'East': 'Attic'},
    'Attic': {'North': 'Great Hall', 'West': 'Cellar'}
    
    }

collected_rooms = {}                                            #-- this is an empty dictionary, this will show you 
                                                                #-- all the rooms you have been in, I used this instead
                                                                #-- of an array because arrays can have duplcates   
                                                                #-- while a dictionary (sometimes called a map)
                                                                #-- only hold unique values and you'll notice its purpose is 
                                                                #-- to only tell you when you have vistied a room not how many times



#-- this is where the game starts
def dragonGame(_direction):                                     
    #-- This is just in case the user inputs a lower case letter
    _direction = _direction.upper()             

    #-- check if letter is E is entered
    #-- introduction of game
    if( _direction == 'E'):
        current_room = 'Great Hall'
        collected_rooms[current_room] = True
        print("You did it!")
    elif(_direction != 'E'):
        print('Theres a wall here')





    #-- we will enter while loop/ actual game
    while(len(collected_rooms) != 4):

        #-- print is a useful technique for debugging code and seeing how variables after changing
        #-- in this case watch as you play the game the variables change as you go along. 
        print("These are the current rooms: ", collected_rooms)
        print('These are the amount of items you have collected: ', len(collected_rooms))

        #-- This is part of the games it shows the current room and the options available in each room
        print("Select direction from room: ", current_room, " your option(s) are ", rooms[current_room])
      
 

        #-- This while loop uses a flag to check the next input and only continues with the game
        #-- when a direction that is valid is selected so for ex: if south is selected but it doesn't exist
        #-- as an option for the current, the game will ask you to input another direction
        flag = False
        while(flag == False):
            next_input = input("")
            next_input = next_input.upper()

            #-- check if user inputted S, N, W, E or something else 
            #-- pay attention to what is happening here
            if(next_input == 'S'):
                if('South' in rooms[current_room]):
                    current_room = rooms[current_room]['South']
                    print("You are now in ", current_room)
                    flag = True
                else:
                    print("That option is not available try again:")

            elif(next_input == 'N'):
                if('North' in rooms[current_room]):
                    current_room = rooms[current_room]['North']
                    print("You are now in ", current_room)               
                    flag = True
                else:
                    print("That option is not available try again:")


            
            elif(next_input == 'W'):
                if('West' in rooms[current_room]):
                    current_room = rooms[current_room]['West']
                    print("You are now in ", current_room)     
                    flag = True
                else:
                    print("That option is not available try again:")


            elif(next_input == 'E'):
                if('East' in rooms[current_room]):
                    current_room = rooms[current_room]['East']
                    print("You are now in ", current_room)     
                    flag = True
                else:
                    print("That option is not available try again:")
                
            
            else:
                print("Wrong selection, select again")

        #-- this checks every loop if current room has already been visited and gives feedback    
        if current_room in collected_rooms:
            print("You have already been here!")
        else:
            collected_rooms[current_room] = True
            print("You collect a new room item")

    #-- This is the end of the game and outputting that you have made it out
    print()
    print()
    print("--------------------------------")
    print("--------------------------------")
    print("Congratulations you made it out of the castle and collected all the necessary Items")

            
        



    




   


def main():


 
    
   
    print(rooms)




    print('Welcome to the game. You are at Start.\n')
    print("Controls East => E North => N South => S West => W")
    user_direction = 'E'
    # user_direction = input('Press E (East) to move to the Great Hall.\n')
    dragonGame( user_direction)

 



    
# Using the special variable
# __name__
if __name__=="__main__":
    main()