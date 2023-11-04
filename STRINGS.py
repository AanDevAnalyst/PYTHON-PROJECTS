import re
from time import *



def Phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print(Phone_number('123-456-7899'))




phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
find = phone_num_regex.search('my number is 123-345-6789')
print('phone number found is: ' + find.group())

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

phone = re.compile(r'''(
 (\d{3}|\(\d{3}\))?         
 (\s|-|\.)?                 
 (\d{3})                    
 (\s|-|\.)                  
 (\d{4})                    
 (\s*(ext|x|ext.)\s*(\d{2,5}))? 
 )''', re.VERBOSE)

Email = re.compile(r'''(
 [a-zA-Z0-9._%+-]+ 
 @ 
 [a-zA-Z0-9.-]+ 
 (\.[a-zA-Z]{2,4}) 
 )''', re.VERBOSE)

print('%s, %s, %.2f' % (42, 'spam', 1 / 3.0))
print('\t Musa Haruna')
print('\n Musa Haruna')
print('The Dad who said %s!' % 'No')

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting.replace('H','J'))

# The Format Method For String
s1 = "His name is {0}!".format("Arthur")
print(s1)
name = "Alice"
age = 10
s2 = "I am {0} and I am {1} years old.".format(name, age)
print(s2)

letter = '''
Dear {0} {2}.
 {0}, I have an interesting money-making proposition for you!
 If you deposit $10 million into my bank account, I can
 double your money ...
'''
print(letter.format("Paris", "Whitney", "Hilton"))
print(letter.format("Bill", "Henry", "Gates"))

ix = 0
fruit = 'Banana'
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

for letter in fruit:
    print(letter)

Number_identifier = +234

Amount = int(input('AMOUNT: '))
print(f'${Amount}')

Health_Status = input('HEALTH STATUS: ')
Blood_Group = input('BLOOD GROUP: ').upper()
Disability = input('DISABILITY: ')
Medication = input('MEDICATION: ')
print(f'''
HEALTH STATUS: {Health_Status}
Disability: {Disability}
Medication: {Medication}
''')
while True:
    print('COURSES REGISTRATION & UPDATE OF COURSES')
    n = 1
    while n < 2:
        sleep(2)
        n += 1
    print('''
Please Choose Any Option To Proceed
1.Courses Registration 
2.Update of Courses Registered
    ''')
    try:
        option = int(input('OPTION: '))
    except ValueError:
        print('User is Expected To Key In Integer Only')
    if option == 1:
        print('''
\t\t\t\t\tWELCOME TO COURSES REGISTRATION GATEWAY
    ''')
        course = input('Enter Courses: ').upper()
        if course == 'Mathematics' 'maths' or 'math':
            print('You have select your first course')

        elif course == 'English Language' 'English' or 'Eng':
            print('You have select Your second course')

        elif course == 'Physcis' or 'Phy':
            print('You have select Your Third course')

        elif course == 'Chemistry' 'Chm':
            print('You have select Your Fourth course')

        elif course == 'Computer Science' or 'Computer':
            print('You have select Your Fifth course')

        elif course == 'Agricultural Science' or 'Agric':
            print('You have select Your Sixth course')

        elif course == 'Biology' or 'Bio':
            print('You have select Your Seventh course')

        elif course == 'Civic Education' or 'Civic':
            print('You have select Your Eight course')

        elif course == 'Islamic Studies' or 'IRS':
            print('You have select Your Ninth course')

        elif course == '':
            print("User didn't Key In Any Course")

        else:
            print('Sorry You Have Entered Wrong Input').upper()

    if option == 2:
        print('''
\t\t\t\t\tWELCOME TO COURSE UPDATE         
    ''')



name = input('Enter name: ')
age = 28
sentence = "My name is {0} and I am {1} years old".format(name,age)
print(sentence)