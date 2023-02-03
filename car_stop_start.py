user_type = ""
while user_type != 'quit':
    user_type = input('>').lower()
   
         
    if user_type == 'Start':
        print('Car started.. ready to go')
    elif user_type == 'stop':
        print('Car stopped')
    elif user_type =='help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    else:
        print("Sorry I don't understand that..")
    