def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def choice(choice):
    choice = 0
    while choice < 4:
        x = int(input("ENTER: "))
        x = int(input("Value1: "))
        y= int(input("Value2: "))
        choice+=1
        if choice == 1:
            print(addition(x,y))

        elif choice == 2:
            print(subtraction(x,y))

        elif choice == 3:
            print(multiplication(x,y))

        elif choice == 4:
            print(division(x,y))

        else:
            choice >=5
            print("your choice is out of range".upper())
            break


            


