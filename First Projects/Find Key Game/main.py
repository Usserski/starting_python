from random import randint
import math

HEIGHT = 10
WIDTH = 10

key_x = randint(0, WIDTH)
key_y = randint(0 , HEIGHT)
steps = 0
player_x = 0 
player_y = 0
player_found_key =  False
distance = 0
old_distance = 0

while not player_found_key:
    print()
    old_distance = distance
    print('Mozesz udac sie w kierunkach jako [W/A/S/D]: ')
    move = input('Dokąd idziesz? ')
    match move.lower():

        case 'w':
            if  player_y >= HEIGHT:
                print('nie mozesz wyjsc poza pole')
            else:    
                player_y += 1
                steps =+ 1
            
        case 's':
            if player_y <= 0:
               print('nie mozesz wyjsc poza pole')
            else:   
               player_y -= 1
               steps =+ 1
        case 'a':
            if player_x <= 0:
               print('nie mozesz wyjsc poza pole')
            else:
               player_x -= 1
               steps =+ 1
        case 'd':
            if player_x >= WIDTH:
               print('nie mozesz wyjsc poza pole')
            else:
               player_x += 1
               steps =+ 1
    distance = math.sqrt((key_x - player_x)**2 + (key_y - player_y)**2)
    
    print()
    print(f'Twoja pozycja : {player_x} , {player_y}')
    
    if distance == old_distance:
        print('dalej tak samo')
    elif distance > old_distance:
        print('zimno')
    elif distance < old_distance:
        print('cieplo')


    if player_x == key_x and player_y == key_y:
        print('Gratulcje znalazles klucz')
        player_found_key = True
    

    
        