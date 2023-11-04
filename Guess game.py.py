guess_count = 0
def GAME(guess_count):
    secrete_number = 9
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count +=1
        if guess == secrete_number: 
            print("YOU WON THE GAME")
            break
        else:
            print("SORRY YOU FAIL")


