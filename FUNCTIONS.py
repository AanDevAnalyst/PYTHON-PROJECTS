
def getAnswer(answer_Number):
    while True:
        try:
            if answer_Number == 1:
                print('It is certain')
                break

            elif answer_Number == 2:
                print('It is decidedly so')
                break

            elif answer_Number == 3:
                print('Yes')
                break

            elif answer_Number == 4:
                print('Reply hazy try again')
                break

            elif answer_Number == 5:
                print('Ask again later')
                break

            elif answer_Number == 6:
                print('Concentrate and ask again')
                break

            elif answer_Number == 7:
                print('My reply is no')
                break

            elif answer_Number == 8:
                print('Outlook not so good')
                break

            elif answer_Number == 9:
                print('Very doubtful')
                break

            else:
                print("Wrong User Input")

        except KeyboardInterrupt:
            print("PROGRAM IS COMPLETED")


answer_Number = int(input("INPUT: "))
getAnswer(answer_Number)

