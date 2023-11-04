import random
secrete_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secrete_number:
        print("YOU WON THE GAME")
        break
    else:
        print("SORRY YOU FAIL")


class Dice:
    def roll(self):
        first= random.randint(1,6)
        second = random.randint(1,6)
        return first, seccond

dice = Dice
print(dice.roll)

try:
    path = Path("ecommerce")
    print(path.exists())
except ImportError:
    print("Mistake during importation")

