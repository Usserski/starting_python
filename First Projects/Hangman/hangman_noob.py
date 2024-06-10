import random

def game():
    words = ['thomas' ,'bug' , 'carrot' , 'summer' ]
    word = random.choice(words)
    letters = ['_'] * len(word)
    lives = 10
    
    while lives > 0:
        print(word)
        print(letters)
        quess = input('Type letter: ')
        if quess in  word:
            index_to_change = [i for i , character in enumerate(word) if character == quess]
            for i in index_to_change:
                letters[i]=quess
        else: 
            lives -=1
            print("Miss! Try one more time ")
            print( "lives count:  " + str(lives))
            
        if '_'  not in letters :
            print('You WON!')
            return
            
        if lives == 0:
            print('You LOSE !')
                
                
                
           
            
                  
 
  
game()