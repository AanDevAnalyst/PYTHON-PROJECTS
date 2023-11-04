pin=1234
Account_balance=10000
print("enter your pin")
x=int(input())
if x == pin:
    print("1 trnasfer fund")
    print("2 change pin")
    print("3 withdrawal")
    print("4 balance")
option = int(input())
if option == 1:
    print("choose your Bank")
    print("1 Access Bank")
    print("2 First Bank")
if bank = int(input()):
    print("enter account balance")
if option == 2:
    new_pin=int(input())
    change_pin=int(input())
if new_pin == change_pin:
    pin = new_pin
    print("pin change successfully")
if option == 3:
    print("show account type")
    print("1 current account")
    print("2 savings account")
    print("3 frequent account")
account_type = int(input()):
    print("1 for 500")
    print("2 for 10000")
    print("3 for others")
account_withdrawal = int(input())
if account_withdrawal <= Account_balance:
    print("withdraw 5000")
pin = input("pin: ")
if len(pin) > 4:
    print("sorry incorrect pin".upper())
else:
    print("1 for amount withdrawal")
    print("2 for transaction")
    print("3 for balance enquirery")
    print("4 for changeing pin")
    
