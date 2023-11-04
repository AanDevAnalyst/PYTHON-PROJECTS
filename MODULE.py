from time import*card_number = 0
card_number_limit = 5
while card_number <= card_number_limit:
    print("please present your card number".upper())
    card_number +=1
    card_number = int(input("Hospital number: "))
    if card_number < card_number_limit:
        n=1
        while n<3:
            sleep(1)
            print("please wait searching file...",end='')
            n+=1
        print("\nsorry hospital number must be less than of 5 characters")
        continue
        
    elif card_number > card_number_limit:
        n=1
        while n<3:
            sleep(1)
            print("please wait searching file...",end='')
            n+=1
        print("\nhospital number must be more than 5 characters")
        continue
       
    elif card_number == 5:
        n=1
        while n<3:
            sleep(1)
            print("\nplease wait searching file...",end='')
            n+=1
        print("you may jion the queue to see you doctor".upper())
        break
hospital_number=1
while hospital_number <=5:
    print("please show you hospital verification".upper())
    hospital_number +=1
    hospital_id = str(input("CARD NUMBER: "))
    if len(hospital_id) <5:
        n=1
        while n<2:
            sleep(1)
            n+=1
            print("please wait...")
        print("\nhospital id must be atleast 5 characters")
        continue
    
    elif len(hospital_id) >5:
        n=1
        while n<2:
            sleep(1)
            n+=1
            print("please wait...")
        print("\nhospital id must be a maximum of 5 characters")
    
    elif len(hospital_id) == 5:
        n=1
        while n<2:
            sleep(1)
            n+=1
            print("searching file...")
        print("\nYOU MAY PROCEED FOR YOUR MEDICATIONS!")
        break

    else:
        print("sorry you don't have a file in this hospital".upper())
        break
