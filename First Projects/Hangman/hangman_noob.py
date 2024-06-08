import random

def game():
    words = ['tomek' ,'robak' , 'marchewka' , 'lato' ]
    word = random.choice(words)
    letters = ['_'] * len(word)
    lives = 10
    
    while lives > 0:
        quess = input('Podaj literke: ')
        print(word)
        print(letters)
        if quess in  letters:
            for i in  letters:
                if quess == letters[i]:
                    letters[i] = quess
                
        else:
            lives -=1
            print('Pudło')    
            
                  
    print('Przegrałes')
    exit()
game()