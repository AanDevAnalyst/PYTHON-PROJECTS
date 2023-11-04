class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")



point1 = Point(10,20,30)
print(point1.x)
print(point1.y)
print(point1.z)

class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi My Name is {self.name}")

User = Person("ABDULJABBAR NUHU")
User.talk()
