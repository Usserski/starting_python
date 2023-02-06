#solution 1
#secret_name = 9

#for i in range(3):
#   shot = input('Guess: ')
#   if secret_name == int(shot):
#    print('You win!')
#    break
#   elif secret_name != int(shot):
#    i += 1
#if i >= 3:
#    print('You lose!')

# solution 2
secret_number = 9
guessing_number = 0 
guessing_limit = 3
while guessing_number < guessing_limit:
   guess =  int(input('Guess: '))
   guessing_number += 1
   if guess == secret_number:
    print('you won!')
    
    break
else:
  print("you have faild!")