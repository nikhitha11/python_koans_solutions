while True:
    try:
        x=int(input("enter number:"))
        if x%2 == 0:
            print('Its even')
        elif x%2 != 0 :
            print ('odd')
        
    except ValueError: 
        print ("Not a number")
    except KeyboardInterrupt:
        
        print("exited the loop")
        break



