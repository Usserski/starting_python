user_type = ""
started = False
while True:
    user_type = input('>').lower()
   
         
    if user_type == 'start':
        if started == True:
            print('Car is already started')
        else:
            print('Car started.. ready to go')
            started = True
    elif user_type == 'stop':
        if started == False:
            print('Car is already stopped')
        else:    
            print('Car stopped')
            started = False
    elif user_type =='help':
        
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
      
    elif user_type == 'quit':
        break
    else:
        print("Sorry I don't understand that..")
    