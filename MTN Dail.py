from time import *
print('Welcome To MTN Network Services')
print('Dear Valued Customer Dail in Your Code')
SMS = '''
Activation of 40MB Daily Plan Was Successful.Bundle 
Renews Tomorrow 12:38:21 To opt out of Auto-renewal,
Text NO114 To 131.Text 2 To 131 For Balance.To Link
Your NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.
'''
SMS_2 = '''
Activation of 1GB Weekly Plan For IG & TIK TOK Was  
Successful.Bundle Renews Tomorrow 12:38:21To opt 
out of Auto-renewal, Text NO114 To 131. Text 2 
To 131 For Balance. To Link Your NIN With Your 
Phone Number Click On The Link:https://bit.ly/3DVytHu.
'''
SMS_3 = '''
Activation of 1.5GB Monthly Plan Was Successful.Bundle 
Renews Next Month 12:38:21. To opt out of Auto-renewal,
Text NO114 To 131.Text 2 To 131 For Balance. To Link
Your NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.
'''
SMS_4 = '''
Activation of 30GB 2-Months Plan Was Successful.Bundle 
Renews Next Two Months 12:38:21. To opt out of Auto-renewal,
Text NO114 To 131.Text 2 To 131 For Balance. To Link Your
NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.
'''
SMS_41 = '''
Activation of 100GB 2-Months Plan Was Successful.Bundle 
Renews Next Two Months 12:38:21. To opt out of Auto-renewal,
Text NO114 To 131.Text 2 To 131 For Balance. To Link Your
NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.
'''
SMS_42 = '''
Activation of 160GB 2-Months Plan Was Successful.Bundle 
Renews Next Two Months 12:38:21. To opt out of Auto-renewal,
Text NO114 To 131.Text 2 To 131 For Balance. To Link Your
NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.
'''
SMS_43 = '''
Activation of 400GB 3-Months Plan Was Successful.Bundle 
Renews Next Two Months 12:38:21. To opt out of Auto-renewal,
Text NO114 To 131.Text 2 To 131 For Balance. To Link Your
NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.
'''
SMS_44 = '''
Activation of 600GB 3-Months Plan Was Successful.Bundle 
Renews Next Two Months 12:38:21. To opt out of Auto-renewal,
Text NO114 To 131.Text 2 To 131 For Balance. To Link Your
NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.
'''
DAIL = ''' 
1.Data Plans
2.Social Bundles
3.Balance Check
4.Roaming/int'i
5.Borrow Credit/Recharge
6.Gift Data
7.Video Packs
8.Hot Deals
9.Chat Zigi
'''
Dial_code = 131
Dial_mini = 1
Dial_max = 3
while Dial_mini <= Dial_max:
    Dial = int(input("Code: "))
    if Dial == Dial_code:
        print('Please wait')
        n = 1
        while n < 2:
            sleep(1)
            n += 1
        print(DAIL)
        Option = int(input('Please Select Any Option: '))
        if Option == 1:
            print('Loading!!!')
            n = 1
            while n < 2:
                sleep(1)
                n += 1
            print('''
1.Daily
2.Weekly
3.Monthly
4.2-3Month
5.Always ON Plans
6.Mi-fi Plans 
7.Family Packs
8.Hot Deals
9.Free Youtube
10.Manage Data
99.Next
0.Back
    ''')
            select = int(input('Select: '))
            if select == 1:
                print('Please wait!!!')
                n = 1
                while n < 2:
                    sleep(1)
                    n += 1
                print('''
1.N50 for 40MB 
2.N100 for 100MB
3.N100 for 350MB (IG & TIK TOK ONLY)
4.N200 for 3200MB (3 days)
5.N300 for 1GB
6.N500 for 2GB (2 days)
99.Next
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('Please wait!!!')
                    n = 1
                    while n < 2:
                        sleep(1)
                        n += 1
                    print('''You Will Be Charged N50
For The Purchase of 40MB
Daily Plan To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For a friend
4.Redeem promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Loading!!!')
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('Please wait')
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''Activation of 40MB Daily Plan Was
Successful and Will Be Renew Tomorrow 12:38:21.You Will Receive 
An SMS Shortly With More Details
    ''')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(SMS)
                            break
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 40MB Daily Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank OR *606# To Borrow                    
Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 40MB Daily Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, IG/Tik Tok Bundles or Music Time and Exchange Your Points For 
Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 40MB Daily Plan Was
Successful and Renew on Tomorrow 12:38:21.You Will Receive An 
SMS Shortly With More Details
    ''')
                            print(SMS)
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 40MB Daily Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank OR *606# To Borrow                    
Airtime Thank You.                    
    ''')
                            break
                        elif proceed == 3:
                            print('''For 40MB Daily Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                            break
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, IG/Tik Tok Bundles or Music Time and Exchange Your Points For 
Free.Thank You
    ''')
                            break
                        else:
                            print('Sorry Input Is Invalid/Incorrect')
                            break
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                        break
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                        break
                    elif pick == 0:
                        print('''
1.N50 for 40MB
2.N100 for 100MB
3.N100 for 350MB (IG & TIK TOK ONLY)
4.N200 for 3200MB (3 days)
5.N300 for 1GB
6.N500 for 2GB (2 days)
99.Next
0.Back
    ''')
                        break
                elif chose == 2:
                    print(''' You Will Be Charged N100 For
The Purchase of 100MB Daily Plan.To Proceed 
Please Select Any,
1.Auto-Renew    
2.One-Off
3.Buy For A Friend
4.Redeem Promo code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        break
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        break
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                    elif pick == 0:
                        print('''
1.N50 for 40MB
2.N100 for 100MB
3.N100 for 350MB (IG & TIK TOK ONLY)
4.N200 for 3200MB (3 days)
5.N300 for 1GB
6.N500 for 2GB (2 days)
99.Next
0.Back
    ''')
                elif chose == 3:
                    print(''' You Will Be Charged N100 For
The Purchase of 350MB IG & Tik Tok Daily Plan.
To Proceed Please Select Any,
1.Auto-Renew  
2.One-Off
0.Back  
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                        break
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                        break
                    elif pick == 0:
                        print('''
1.N50 for 40MB
2.N100 for 100MB
3.N100 for 350MB (IG & TIK TOK ONLY)
4.N200 for 3200MB (3 days)
5.N300 for 1GB
6.N500 for 2GB (2 days)
99.Next
0.Back
    ''')
                        break
                elif chose == 4:
                    print(''' You Will Be Charged N200 For 
The Purchase of 200MB 3-Days Plan.To proceed 
Please Select Any,
1.Auto-Renew
2.One-Off
3.Buy For A Friend
4.Redeem Promo Code
0.Back    
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        n = 1
                        while n < 2:
                            sleep(1)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        break
                    elif pick == 2:
                        n = 1
                        while n < 2:
                            sleep(1)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
            ''')
                        break
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                        break
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                        break
                    elif pick == 0:
                        print('''
1.N50 for 40MB
2.N100 for 100MB
3.N100 for 350MB (IG & TIK TOK ONLY)
4.N200 for 3200MB (3 days)
5.N300 for 1GB
6.N500 for 2GB (2 days)
99.Next
0.Back
    ''')
                        break
                elif chose == 5:
                    print(''' You Will Be Charged N300 For
The Purchase of 1GB Daily Plan.To Proceed Please
Select Any,
1.Auto-Renew
2.One-Off
3.Buy For A Friend
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                    elif pick == 2:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        break
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                        break
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                        break
                    elif pick == 0:
                        print('''
1.N50 for 40MB
2.N100 for 100MB
3.N100 for 350MB (IG & TIK TOK ONLY)
4.N200 for 3200MB (3 days)
5.N300 for 1GB
6.N500 for 2GB (2 days)
99.Next
0.Back
    ''')
                        break
                elif chose == 6:
                    n = 1
                    while n < 2:
                        sleep(0.9)
                        n += 1
                    print(''' You Will Be Charged N500 For 
The Purchase of 2GB 2-Days Plan.To Proceed Please
Select Any,
1.Auto-Renew
2.One-Off 
3.Buy For A Friend
4.Redeem Promo Code      
0.Back        
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        break
                    elif pick == 2:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        break
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                        break
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                        break
                    elif pick == 0:
                        n = 1
                        while n < 2:
                            sleep(0.9)
                            n += 1
                        print('''
1.N50 for 40MB
2.N100 for 100MB
3.N100 for 350MB (IG & TIK TOK ONLY)
4.N200 for 3200MB (3 days)
5.N300 for 1GB
6.N500 for 2GB (2 days)
99.Next
0.Back
    ''')
                        break
                elif chose == 99:
                    n = 1
                    while n < 2:
                        sleep(1)
                        n += 1
                    print('''
7.N25 For 250MB(NightLife)
8.N50 For 500MB(NightLife)    
9.N300 For 750MB(3-Day Plan)        
10.N25 For WhatsApp Daily     
99.Next
0.Back        
    ''')
                    break
                elif chose == 7:
                    print(''' You Will Be Charged N25 For The 
Purchase of 250MB Pulse Nightlife Bundle.
1.Proceed 
0.Back      
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('''Do You Want Your 250MB Pulse Night
Bundle To Be Automatically Renewed Every one day Select Any,  
1.Yes(Auto-Renew)                 
2.No(One-Off)                                
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            n = 1
                            while n < 2:
                                sleep(1)
                                n += 1
                            print('''You Have Successfully Purchase Nightlife 
Bundle at N25 For 250MB and Will Be Auto-Renewed.
    ''')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print('''REMINDER! Your 250MB MTN Pulse NightLife
Bundle Will Expire By 6am and Your Unused Will Be Cleared After Expiry.
    ''')
                            break
                        elif proceed == 2:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''You Have Successfully Purchase Nightlife 
Bundle at N25 For 250MB.Data Bundle Won't Be Renewed.
    ''')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print('''REMINDER! Your 250MB MTN Pulse NightLife
Bundle Will Expire By 6am and Your Unused Will Be Cleared After Expiry
    ''')
                            break
                        else:
                            print('Sorry Invalid Input')
                            break
                    elif pick == 0:
                        n = 1
                        while n < 2:
                            sleep(1)
                            n += 1
                        print('''
1.Daily
2.Weekly
3.Monthly
4.2-3Month
5.Always ON Plans
6.Mi-fi Plans
7.Family Packs
8.Hot Deals
9.Free Youtube
10.Manage Data
99.Next
0.Back                                
    ''')
                        break
                elif chose == 8:
                    n = 1
                    while n < 2:
                        sleep(1)
                        n += 1
                    print(''' You Will Be Charged N50 For The    
Purchase of 500MB Pulse Nightlife Bundle.
1.Proceed        
0.Back     
    ''')
                    proceed = int(input('Proceed: '))
                    if proceed == 1:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('''You Have Successfully Purchase Nightlife 
Bundle at N50 For 500MB and Will Be Auto-Renewed.
    ''')
                        n = 1
                        while n < 2:
                            sleep(3)
                            n += 1
                        print('''REMINDER! Your 500MB MTN Pulse NightLife
Bundle Will Expire By 6am and Your Unused Will Be Cleared After Expiry.
    ''')
                        break
                    elif proceed == 2:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('''You Have Successfully Purchase Nightlife 
Bundle at N50 For 500MB.Data Bundle Won't Be Renewed.
    ''')
                        n = 1
                        while n < 2:
                            sleep(3)
                            n += 1
                        print('''REMINDER! Your 500MB MTN Pulse NightLife
Bundle Will Expire By 6am and Your Unused Will Be Cleared After Expiry
    ''')
                        break
                    else:
                        print('Sorry Invalid Input')
                        break
                elif chose == 9:
                    n = 1
                    while n < 2:
                        sleep(1)
                        n += 1
                    print(''' You Will Be Charged N300 For The 
The Purchase of 750MB 3 Days Plan.To Proceed Please
Select Any,
1.Auto-Renew        
2.One-Off        
0.Back
    ''')
                    break
                elif chose == 10:
                    n = 1
                    while n < 2:
                        sleep(1)
                        n += 1
                    print(''' You Will Be Charged N25 For This 
Purchase of WhatsApp Daily Bundle.To Proceed Please
Select Any,
1.Auto-Renew
2.One-Off 
0.Back
    ''')
                    break
                elif chose == 99:
                    n = 1
                    while n < 2:
                        sleep(1)
                        n += 1
                    print(''' 
11.N50 Jolly Combo Offer        
12.N100 Jolly Combo Offer 
0.Back        
    ''')
                    break
                else:
                    print('Sorry Invalid Input')
                    break
            elif select == 2:
                n = 1
                while n < 2:
                    sleep(1)
                    n += 1
                print('''
1.N200 for 1GB (IG & Tik Tok Only)
2.N300 for 350MB
3.N500 for 1.5GB
4.N500 for 750MB (2-Week Plan)
5.N1,500 for 6GB
6.N1,000 for 2GB
99.Next
0.Back    
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    n = 1
                    while n < 2:
                        sleep(0.8)
                        n += 1
                    print('''You Will Be Charged N200
For The Purchase of 1GB IG & TIK TOK 
Weekly Plan To Proceed Select 
1.Auto-Renewal
2.One-off
0.Back
00.MainMenu
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        n = 1
                        while n < 2:
                            sleep(0.5)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            n = 1
                            while n < 2:
                                sleep(0.5)
                                n += 1
                            print('''Activation of 1GB Weekly Plan For IG & TIK TOK Was
Successful and Will Be Renewed Tomorrow 12:38:21.You Will Receive An 
SMS Shortly With More Details
    ''')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(SMS_2)
                            break
                        elif proceed == 2:
                            n = 1
                            while n < 2:
                                sleep(2)
                                n += 1
                            print('''Y'ellow! Activation of 1GB  Weekly Plan For 
IG & TIK TOK Failed Due To Insufficient Balance.
Dail *904# To Recharge From Your Bank OR *606# To Borrow                    
Airtime, Thank You.                    
    ''')
                            break
                        elif proceed == 3:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''For 1GB weekly Plan For IG & TIK TOK, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                            break
                        elif proceed == 4:
                            n = 1
                            while n < 2:
                                sleep(2)
                                n += 1
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, IG/Tik Tok Bundles or Music Time 
and Exchange Your Points For Free.Thank You
    ''')
                            break
                        else:
                            print('Sorry Input Is Invalid/Incorrect')
                            break
                    elif pick == 2:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        break
                    elif pick == 0:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('''
1.N200 for 1GB (IG & Tik Tok Only)
2.N300 for 350MB
3.N500 for 1.5GB
4.N500 for 750MB (2-Week Plan)
5.N1,500 for 6GB
6.N1,000 for 2GB
99.Next
0.Back    
    ''')
                        break
                    elif pick == 00:
                        n = 1
                        while n < 2:
                            sleep(1.5)
                            n += 1
                        print(DAIL)
                        break
                    else:
                        print('Sorry Invalid Input')
                        break
            elif select == 3:     #To Be Continued 1
                n = 1
                while n < 2:
                    sleep(1)
                    n += 1
                print('''
1.N1,000 for 1.5GB
2.1,200 for 2GB
3.1,500 for 3GB
4.2,000 for 4.5GB
5.N2,500 for 6GB
6.N3,500 for 12GB
7.N5,000 for 20GB
99.Next
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    n = 1
                    while n < 2:
                        sleep(0.8)
                        n += 1
                    print('''You Will Be Charged N1,000
For The Purchase of 1.5GB Monthly Plan.To
Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For a friend
4.Redeem promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''Activation of 1.5GB Monthly Plan Was
Successful and Will Be Renewed Next Month 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(SMS_3)
                            break
                        elif proceed == 2:
                            n = 1
                            while n < 2:
                                sleep(2)
                                n += 1
                            print('''Y'ellow! Activation of 1.5GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank OR *606# To Borrow                    
Airtime Thank You.                    
    ''')
                            break
                        elif proceed == 3:
                            n = 1
                            while n < 2:
                                sleep(0.5)
                                n += 1
                            print('''For 1.5GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                            break
                        elif proceed == 4:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, IG/Tik Tok Bundles or Music Time and Exchange Your Points For 
Free.Thank You
    ''')
                            break
                        else:
                            print('Sorry Wrong Input')
                            break
                    elif pick == 2:
                        n = 1
                        while n < 2:
                            sleep(0.5)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                        break
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                        break
                    elif pick == 0:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('''
1.N1,000 For 1.5GB
2.N1,200 For 2GB
3.N1,500 For 3GB
4.N2000  For 4.5GB
5.N2,500 For 6GB
6.N3,500 For 12GB 
7.N5,000 For 20GB
99.Next
0.Back
    ''')
                        break
                    #Not Completed But Stop
            elif select == 4:       #To Be Continued From Choose == 2 to Choose == 0
                n = 1
                while n < 2:
                    sleep(1)
                    n += 1
                print('2-3 Months Plans')
                print('''
1.N,8000 for 30GB/60Days
2.N20,000 for 100GB/60Days
3.N30,000 for 160GB/60Days
4.N50,000 for 400GB/90Days
5.N75,000 for 600GB/90Days
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    n = 1
                    while n < 2:
                        sleep(0.8)
                        n += 1
                    print('''You Will Be Charged N8000
For The Purchase of 30GB 2-Month Plan.
To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For A friend 
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))   #To Be  Continued
                    if pick == 1:
                        n = 1
                        while n < 2:
                            sleep(0.5)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''Activation of 30GB 2-Months Plan Was
Successful and Will Be Renewed Next Two Months 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(SMS_4)
                            break
                        elif proceed == 2:
                            n = 1
                            while n < 2:
                                sleep(2)
                                n += 1
                            print('''Y'ellow! Activation of 30GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                            break
                        elif proceed == 3:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''For 30GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                            break
                        elif proceed == 4:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months Plan and Exchange Your Points For Free.Thank You
    ''')
                            break
                        else:
                            print('Sorry Wrong Input')
                            break
                    elif pick == 2:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            n = 1
                            while n < 2:
                                sleep(1.5)
                                n += 1
                            print('''Activation of 30GB 2-Months Plan Was
Successful and Won't Be Renewed For The Next Two Months 12:38:21.You 
Will Receive An SMS Shortly With More Details Will Be Sent To You.
    ''')
                            break
                        elif proceed == 2:
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print('''Y'ellow! Activation of 30GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                            break
                        elif proceed == 3:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''For 30GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                            break
                        elif proceed == 4:
                            n = 1
                            while n < 2:
                                sleep(1)
                                n += 1
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months and Exchange Your Points For Free.Thank You
    ''')
                            break
                        else:
                            print('Sorry Wrong Input')
                            break
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                        break
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                        break
                    elif pick == 0:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('''
1.N,8000 for 30GB/60Days
2.N20,000 for 100GB/60Days
3.N30,000 for 160GB/60Days
4.N50,000 for 400GB/90Days
5.N75,000 for 600GB/90Days
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 2:
                    n = 1
                    while n < 2:
                        sleep(1)
                        n += 1
                    print('''You Will Be Charged N20,000
For The Purchase of 100GB 2-Month Plan.
To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For A friend 
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''Activation of 100GB 2-Months Plan Was
Successful and Will Be Renewed Next Two Months 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(SMS_41)
                            break
                        elif proceed == 2:
                            n = 1
                            while n < 2:
                                sleep(2)
                                n += 1
                            print('''Y'ellow! Activation of 100GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                            break
                        elif proceed == 3:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''For 100GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                            break
                        elif proceed == 4:
                            n = 1
                            while n < 2:
                                sleep(1.5)
                                n += 1
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months Plan and Exchange Your Points For Free.Thank You
    ''')
                            break
                        else:
                            print('Sorry Wrong Input')
                            break
                    elif pick == 2:
                        n = 1
                        while n < 2:
                            sleep(1)
                            n += 1
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''Activation of 100GB 2-Months Plan Was
Successful and Won't Be Renewed For The Next Two Months 12:38:21.You 
Will Receive An SMS Shortly With More Details Will Be Sent To You.
    ''')
                            break
                        elif proceed == 2:
                            n = 1
                            while n < 2:
                                sleep(2)
                                n += 1
                            print('''Y'ellow! Activation of 100GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                            break
                        elif proceed == 3:
                            n = 1
                            while n < 2:
                                sleep(0.8)
                                n += 1
                            print('''For 30GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                            break
                        elif proceed == 4:
                            n = 1
                            while n < 2:
                                sleep(1.5)
                                n += 1
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months and Exchange Your Points For Free.Thank You
    ''')
                            break
                        else:
                            print('Sorry Wrong Input')
                            break
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))
                        break
                    elif pick == 4:
                        Code = int(input('Input Your Code: '))
                        break
                    elif pick == 0:
                        n = 1
                        while n < 2:
                            sleep(0.8)
                            n += 1
                        print('''
1.N,8000 for 30GB/60Days
2.N20,000 for 100GB/60Days
3.N30,000 for 160GB/60Days
4.N50,000 for 400GB/90Days
5.N75,000 for 600GB/90Days
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 3:
                    n = 1
                    while n < 2:
                        sleep(1)
                        n += 1
                    print('''You Will Be Charged 30,000
For The Purchase of 160GB 2-Month Plan.
To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For A friend 
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 160GB 2-Months Plan Was
Successful and Will Be Renewed Next Two Months 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                            print(SMS_42)
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 160GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 160GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel    
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months Plan and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 160GB 2-Months Plan Was
Successful and Won't Be Renewed For The Next Two Months 12:38:21.You 
Will Receive An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 160GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 100GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))

                    elif pick == 4:
                        Code = int(input('Input Your Code: '))

                    elif pick == 0:
                        print('''
1.N,8000 for 30GB/60Days
2.N20,000 for 100GB/60Days
3.N30,000 for 160GB/60Days
4.N50,000 for 400GB/90Days
5.N75,000 for 600GB/90Days
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 4:
                    print('''You Will Be Charged N50,000
For The Purchase of 400GB For 3-Month Plan.
To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For A friend 
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 400GB 2-Months Plan Was
Successful and Will Be Renewed Next Three Months 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                            print(SMS_43)
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 400GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 400GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 3-Months Plan and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 400GB 3-Months Plan Was
Successful and Won't Be Renewed For The Next Two Months 12:38:21.You 
Will Receive An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 400GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 400GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 3-Months and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))

                    elif pick == 4:
                        Code = int(input('Input Your Code: '))

                    elif pick == 0:
                        print('''
1.N,8000 for 30GB/60Days
2.N20,000 for 100GB/60Days
3.N30,000 for 160GB/60Days
4.N50,000 for 400GB/90Days
5.N75,000 for 600GB/90Days
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 5:
                    print('''You Will Be Charged N75,000
For The Purchase of 600GB 3-Month Plan.
To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For A friend 
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 600GB For 3-Months Plan Was
Successful and Will Be Renewed Next Two Months 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                            print(SMS_44)
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 600GB 3-Months Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 600GB 3-Months Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 3-Months Plan and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 600GB 3-Months Plan Was
Successful and Won't Be Renewed For The Next Two Months 12:38:21.You 
Will Receive An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 600GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 600GB Monthly Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))

                    elif pick == 4:
                        Code = int(input('Input Your Code: '))

                    elif pick == 0:
                        print('''
1.N,8000 for 30GB/60Days
2.N20,000 for 100GB/60Days
3.N30,000 for 160GB/60Days
4.N50,000 for 400GB/90Days
5.N75,000 for 600GB/90Days
0.Back
    ''')
                else:
                    print('Sorry Wrong Input') #Completed
            elif select == 5:
                print('''
1.N60 for 200MB/24Hrs    
2.N120 for 450MB/7Days
3.N3000 for 15GB/30Days
4.N6,000 for 45GB/30Days
0.Back
00.MainMenu    
    ''')
                print('Always On Bundles')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''You Will Be Charged N60
For The Purchase of 200MB For 24Hrs.To
Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For a friend
4.Redeem promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 200MB For 24Hrs Was
Successful and Will Be Renewed Next Month 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 200MB For 24Hrs Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank OR *606# To Borrow                    
Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 200MB For 24Hrs Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 24Hrs and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))

                    elif pick == 4:
                        Code = int(input('Input Your Code: '))

                    elif pick == 0:
                        print('''
1.N60 For 200MB/24Hrs
2.N120 for 450MB/7Days
3.N3000 for 15GB/30Days
4.N6,000 for 45GB/30Days
0.Back
00.MainMenu
    ''')

                chose = int(input('Chose: '))
                if chose == 2:
                    print('''You Will Be Charged N120
For The Purchase of 450MB For 7-Days Always On 
Plan.To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For A friend 
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 450MB 7-Days Always On Plan 
Was Successful and Will Be Renewed Next Week 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 450MB 7-Days Always On Plan Failed 
Due To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 450MB 7-Days Always On Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 7-Days Plan and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 450 7-Days Always On Plan Was
Successful and Won't Be Renewed For The Next Seven Days 12:38:21.You 
Will Receive An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 450 7-Days Always On Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 450MB 7-Days Always On Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For Always On Plan and Exchange Your Points For Free.Thank You
        ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))

                    elif pick == 4:
                        Code = int(input('Input Your Code: '))

                    elif pick == 0:
                        print('''
1.N60 For 200MB/24Hrs
2.N120 For 450MB/7Days
3.N3,000 For 15GB/30Days
4.N6,000 For 45GB/30Days
0.Back
00.MainMenu
    ''')
                chose = int(input('Chose: '))
                if chose == 3:
                    print('''You Will Be Charged N3,000
For The Purchase of 15GB 1-Month Always On Plan.
To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For A friend 
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 15GB 1-Month Always On Plan Was
Successful and Will Be Renewed Next Month 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 15GB 1-Month Always On Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 15GB 1-Month Always On Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months Plan and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 15GB 1-Month Always On Plan Was
Successful and Won't Be Renewed For The Next Month 12:38:21.You 
Will Receive An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 15GB Monthly Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 15GB 1-Month Always On Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))

                    elif pick == 4:
                        Code = int(input('Input Your Code: '))

                    elif pick == 0:
                        print('''
1.N50 For 200MB/24Hrs
2.N120 For 450MB/7Days
3.N3,000 For 15GB/30Days
4.N6,000 For 45GB/30Days
0.Back
00.MainMenu
    ''')
                chose = int(input('Chose: '))
                if chose == 4:
                    print('''You Will Be Charged 6,000
For The Purchase of 45GB 1-Month Always On Plan.
To Proceed Select 
1.Auto-Renewal
2.One-off
3.Buy For A friend 
4.Redeem Promo Code
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 45GB 1-Month Always On Plan Was
Successful and Will Be Renewed Next Month 12:38:21.You Will Receive 
An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 45GB 1-Month Always On Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 45GB 1-Month Always On Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 1-Month Always On Plan and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 2:
                        print('Kindly Select Payment Type')
                        print('''
1.Airtime
2.Pulse Point                
3.Pulse Point and Airtime
4.About Pulse Point
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''Activation of 45GB 1-Month Always On Plan Was
Successful and Won't Be Renewed Next Month 12:38:21.You 
Will Receive An SMS Shortly With More Details Will Be Sent To You.
    ''')
                        elif proceed == 2:
                            print('''Y'ellow! Activation of 45GB 1-Month Always on Plan Failed Due
To Insufficient Balance.Dail *904# To Recharge From Your Bank Account OR *606# To 
Borrow Airtime Thank You.                    
    ''')
                        elif proceed == 3:
                            print('''For 45GB 1-Month Always On Plan, Your Pulse Points 
Will Be Charged First.If You Have Insufficient Points We Will Charge                    
From Your Airtime.Please Select Any,
1.proceed                    
2.Cancel
    ''')
                        elif proceed == 4:
                            print('''Y'ellow To Earn Pulse Point, Dail *131# or *406# To
Buy Data Bundles, For 2-Months and Exchange Your Points For Free.Thank You
    ''')
                        else:
                            print('Sorry Wrong Input')
                    elif pick == 3:
                        Number = int(input('Enter Recipients Number: '))

                    elif pick == 4:
                        Code = int(input('Input Your Code: '))

                    elif pick == 0:
                        print('''
1.N60 For 200MB/24Hrs
2.N120 For 450MB/7Days
3.N3,000 For 150GB/30Days
4.N6,000 For 45GB/30Days
0.Back
00.MainMenu
    ''')
                chose = int(input('Chose: '))
                if chose == 0:
                    print('''
1.Daily
2.Weekly      
3.Monthly    
4.2-3 Months   
5.Always On Plans
6.Mi-Fi 
7.Family Packs    
8.Hot Deals 
9.Free YouTube 
10.Manage Data 
99.Next
0.Back   
     ''')
                chose = int(input('Chose: '))
                if chose == 00:
                    print(DAIL)
                else:
                    print('UNKNOWN APPLICATION')
            elif select == 6:
                print('''
1.Link Device
2.Recharge Device
3.Buy Data Bundle On Device
4.Check Device Balance
5.View & Unlink Device  
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''
To Proceed Select 
1.Link Device
0.Back
    ''')
                    pick = int(input('Pick: '))  # To Be  Continued
                    if pick == 1:
                        MiFi_Code = int(input('Enter Mi-Fi MSISDN: '))
                        print('You Have Successfully Link Your SIM Card To Your Device')
                    elif pick == 0:
                        print('''
1.Link Device
2.Recharge Device
3.Buy Data Bundle On Device
4.Check Device Balance
5.View & Unlink Device                  
    ''')
                    else:
                        print('Invalid IMEI Code')
                chose = int(input('Chose: '))
                if chose == 2:
                    print('No Mi-Fi Consumer Attached')
                elif chose == 3:
                    print('''
1.Daily Bundles
2.Weekly Bundles
3.Monthly Bundles
4.2-3 Months
5.Mi-Fi Bundles
6.HyNetFlex Bundles
0.Back
    ''')
                    pick = int(input('Pick:'))
                    if pick == 1:
                        print('No Mi-Fi Consumer Attached')
                    elif pick == 2:
                        print('Sorry No Mi-Fi Consumer Attached')
                    elif pick == 3:
                        print('Still No Mi-Fi Consumer Connected')
                    elif pick == 4:
                        print('No MI-Fi Device Found Connected')
                    elif pick == 5:
                        print('Sorry No Mi-Fi Device Connected')
                    elif pick == 6:
                        print('''
1.Weekly Unlimited Bundle
2.Monthly Unlimited Bundles
3.Monthly HyNetFlex Bundles 
4.2-Month HyNetFlex Bundles
5.3-Month HyNetFlex Bundles
99.Next
    ''')
                        pick = int(input('Pick:'))
                        if pick == 1:
                            print('''You Have Successfully Purchase
Weekly Unlimited Bundle 
For Your Device Thanks.
    ''')
                        elif pick == 2:
                            print('''You Have successfully Purchase 
Monthly Unlimited Bundle
For Your Device Thanks. 
    ''')
                        elif pick == 3:
                            print('''You have Successfully Purchase
Monthly HyNetFlex Bundle
For Your Device Thanks.
    ''')
                        elif pick == 4:
                            print('''You Have Successfully Purchase 
2-Month HyNetFlex Bundle
For Your Device Thanks.
    ''')
                        elif pick == 5:
                            print('''You Have Successfully Purchase
3-Month HyNetFlex Bundle
For Your Device Thanks.
    ''')
                        else:
                            print('Oops Sorry Wrong Input')
                    else:
                        print('Connection Problem or Invalid MMI Code')
                elif chose == 4:
                    print('''
1.Airtime
2.Data Balance    
3.HyNetFlex Balance
0.Back           
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('No Mi-Fi Consumer Attached')
                    elif pick == 2:
                        print('No Mi-Fi Consumer Attached')
                    elif pick == 3:
                        print('No Mi-Fi Consumer Attached')
                    elif pick == 0:
                        print('''
1.Link Device
2.Recharge Device
3.Buy Data Bundle On Device
4.Check Device Balance
5.View & Unlink Device                                  
    ''')
                    else:
                        print('Wrong User Input!!!')
                elif chose == 5:
                    print('''
1.Unlink Device
2.View Device
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('No Mi-Fi Consumer Attached')
                    elif pick == 2:
                        print('No Mi-Fi Number Is Linked')
                    elif pick == 0:
                        print('''
1.Link Device
2.Recharge Device
3.Buy Data Bundle On Device
4.Check Device Balance
5.View & Unlink Device                                                  
    ''')
                else:
                    print('Sorry Invalid User Input')
            elif select == 7:
                print('''
1.Buy Family Pack    
2.Add New Beneficiary/Sponsor  
3.Manage Beneficiary/Sponsor
4.Balance Enquiry
5.Deactivate Service
6.Help
0.Back
00.MainMenu
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''
1.Buy Family pack
2.Add New Beneficiary/Sponsor
3.Manage Beneficiary/Sponsor
4.Balance Enquiry
5.De-activate Service
6.Help
0.Back
00.MainMenu        
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('''
1.Monthly
2.3-Month        
3.Top-Up Plans
0.Back
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('''You Have Successfully Purchase 20GB 
Monthly Family Pack For N5,000.
    ''')
                        elif proceed == 2:
                            print('''You Have Successfully Purchase 40GB
Monthly Family pack For N10,000.
    ''')
                        elif proceed == 3:
                            print('''You Have Successfully Purchase 75GB
Monthly Family Pack For N15,000.   
    ''')
                        elif proceed == 4:
                            print('''You Have Successfully Purchase 120GB
Monthly Family Pack For N20,000.
    ''')
                        elif proceed == 5:
                            print('''You Have Successfully Purchase
Monthly Family Pack For N30,000.
    ''')
                        elif proceed == 0:
                            print('''
1.Buy Family Pack
2.Add New Beneficiary/Sponsor   
3.Manage Beneficiary/Sponsor
4.Balance Enquiry
5.De-activate Service
0.Back
00.MainMenu                    
    ''')
                        else:
                            print('Sorry Wrong Input')

                    elif pick == 2:
                        print('''
1.N50,000 For 400Gb
2.N75,000 For 600GB
0.Back             
    ''')
                        proceed = int(input("Proceed: "))
                        if proceed == 1:
                            print('''You Have Successfully Purchase 400GB
3-Months Family Pack For N50,000                    
    ''')
                        elif proceed == 2:
                            print('''You Have Successfully Purchase 600GB
3-Months Family Pack For N75,000
    ''')
                        elif proceed == 0:
                            print('''
1.Monthly
2.3-Month        
3.Top-Up Plans
0.Back                    
    ''')
                        else:
                            print('Sorry Wrong User Input')
                    elif pick == 3:
                        print('Top-Up Plans')
                        print('''
1.N1,000 For 4GB
2.N3,000 For 14GB
0.Back
    ''')
                        proceed = int(input('Procedd: '))
                        if proceed == 1:
                            print('''You Have Successfully Purchase 4GB For N1,000 
Top-Up Family Pack, SMS Will Be Send Shortly.
    ''')
                        elif proceed == 2:
                            print('''You Have Successfully Purchase 14GB For N3,000
Top-Up Family Pack,SMS Will Be Send Shortly.
    ''')
                        elif proceed == 0:
                            print('''
1.Monthly
2.3-Month        
3.Top-Up Plans
0.Back                                        
    ''')
                        else:
                            print('Invalid Input')
                elif chose == 2:
                    print('''
1.Add New Beneficiary
2.Allocate Family Pack
3.Rest Family Pack      
0.Back
00.MainMenu          
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('To Add Beneficiary To Family Pack Service')
                        print('Please Enter Your Phone Number')
                        proceed = int(input('Phone Number: '))
                    elif pick == 2:
                        print('No Consumer On Entered MSISDN')
                    elif pick == 3:
                        print('''
1.Reset All Beneficiary
2.Reset Beneficiary
0.Back 
00.MainMenu
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print(' Do You Want To Reset The Limit')
                            print('For All Your Beneficiary,Select Any')
                            print('''
1.Yes
2.Cancel
0.Back
00.MainMenu               
    ''')
                        elif proceed == 2:
                            print('No Consumer On The Entered MSISDN')
                        elif proceed == 0:
                            print('''
1.Add New Beneficiary
2.Allocate Family Pack
3.Rest Family Pack      
0.Back
00.MainMenu                              
    ''')
                        elif proceed == 00:
                            print('''
1.Data Plans
2.Social Bundles
3.Balance Check
4.Roaming/Int'i
5.Borrow Credit/Recharge
6.Gift Data
7.Video Packs
8.Hot Deals
9.Chat Zigi
    ''')
                    elif pick == 0:
                        print('''
1.Buy Family Pack
2.Add New Beneficiary/Sponsor   
3.Manage Beneficiary/Sponsor
4.Balance Enquiry
5.De-activate Service
0.Back
00.MainMenu                                
    ''')
                    elif pick == 00:
                        print('''
1.Data Plans
2.Social Bundles
3.Balance Check
4.Roaming/Int'i
5.Borrow Credit/Recharge
6.Gift Data
7.Video Packs
8.Hot Deals
9.Chat Zigi                
    ''')
                    else:
                        print(' Oops, Looks Like The Code You Used')
                        print('Was Incorrect Please Check & Try Again')
                elif chose == 3:
                    print('''
1.View Beneficiary
2.View Sponsor
3.Delete All Beneficiary          
4.Delete Beneficiary
5.Delete Sponsor
6.Ask Data
0.Back
00.MainMenu       
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('No Consumer On The Entered MSISDN')
                    elif pick == 2:
                        print('''Sorry You Don't Have A Family Pack Sponsor.Thank You''')
                    elif pick == 3:
                        print('  Do You Want To Delete All Your')
                        print('Beneficiary From Your Family pack Service')
                        print('''
1.Yes
2.Cancel
0.Back
00.MainMenu           
    ''')
                        proceed = int(input('Proceed: '))
                        if proceed == 1:
                            print('You Have Successfully Delete All Beneficiary,thank You')
                        elif proceed == 2:
                            print('You Have Cancel Your Operation')
                        elif proceed == 0:
                            print('''
1.View Beneficiary
2.View Sponsor
3.Delete All Beneficiary          
4.Delete Beneficiary
5.Delete Sponsor
6.Ask Data
0.Back
00.MainMenu                       
    ''')
                        elif proceed == 00:
                            print('''
1.Data Plans
2.Social Bundles
3.Balance Check
4.Roaming/Int'i
5.Borrow Credit/Recharge
6.Gift Data
7.Video Packs
8.Hot Deals
9.Chat Zigi                                
    ''')
                        else:
                            print('Sorry Wrong User Input')
                    elif pick == 4:
                        print('''Sorry No Consumer On The Entered MSISDN''')
                    elif pick == 5:
                        print('''NO Provider Attached On The Entered MSISDN''')
                    elif pick == 6:
                        print(''' To Request Data From A Friend''')
                        print('''Please Enter Phone Number(e.g08xxxxxxxxx''')
                        Phone_Number = int(input("Phone Number: "))
                    elif pick == 0:
                        print('''
1.View Beneficiary
2.View Sponsor
3.Delete All Beneficiary          
4.Delete Beneficiary
5.Delete Sponsor
6.Ask Data
0.Back
00.MainMenu                                   
    ''')
                    elif pick == 00:
                        print('''
1.Data Plans
2.Social Bundles
3.Balance Check
4.Roaming/Int'i
5.Borrow Credit/Recharge
6.Gift Data
7.Video Packs
8.Hot Deals
9.Chat Zigi                                            
    ''')
                    else:
                        print('Oops Sorry Wrong User Input')

                elif chose == 4:
                    print('''
1.Sponsor Balance Enquiry
2.Beneficiary Enquiry
0.Back
00.MainMenu       
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('''
Dear Customer,You Don't Have Any Active Data Bundle.
Please Dial *131# To Buy Another Data Bundle.Thank you. 
    ''')
                    elif pick == 2:
                        print('''
Dear Customer,You Are Not A FamilyPack Beneficiary.
Please Dial *131# To Check Your Data Balance.Thank You            
    ''')
                    elif pick == 0:
                        print('''
1.Buy Family Pack
2.Add New Beneficiary
3.Manage Beneficiary/Sponsor
4.Balance Enquiry
5.De-activate Service
6.Help
0.Back
00.MainMenu            
    ''')
                    elif pick == 00:
                        print('''
1.Data Plans
2.Social Bundles
3.Balance Check
4.Roaming/Int'i
5.Borrow Credit/Recharge
6.Gift Data
7.Video Packs
8.Hot Deals
9.Chat Zigi                                                        
    ''')
                    else:
                        print('Sorry Invalid MMI Code')

                elif chose == 5:
                    print('''
Are You Sure You Want To Deactivate Family Pack Note
That All Beneficiary Will Be Removed During This Process.
1.proceed
0.Back
00.MainMenu
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('You Have Successfully Deactivate Family Pack Bundle')
                    elif pick == 0:
                        print('''
1.Buy Family Pack
2.Add New Beneficiary
3.Manage Beneficiary/Sponsor
4.Balance Enquiry
5.De-activate Service
6.Help
0.Back
00.MainMenu                            
    ''')
                    elif pick == 00:
                        print('''
1.Data Plans
2.Social Bundles
3.Balance Check
4.Roaming/Int'i
5.Borrow Credit/Recharge
6.Gift Data
7.Video Packs
8.Hot Deals
9.Chat Zigi                                                                        
    ''')
                    else:
                        print('Sorry Wrong/Invalid Input')

                elif chose == 6:
                    print('''
Welcome To MTN Family Pack Service.You Can
Share Your Family Pack Bundle With 5 Phone
numbers and Enjoy 24hrs Of Internet Connection.
To Begin Dial *131*1*7#.Thank You
    ''')
                elif chose == 0:
                    print('''
1.Daily
2.Weekly
3.Monthly
4.2-3 Month
5.Always On Plans
6.Mi-Fi Plans
7.Family Packs
8.Hot Deals
9.Free YouTube
10.Manage Data
99.Next
0.Back
    ''')
                elif chose == 00:
                    print('''
1.Data Plans
2.Social Bundles
3.Balance Check
4.Roaming/Int'i
5.Borrow Credit/Recharge
6.Gift Data
7.Video Packs
8.Hot Deals
9.Chat Zigi                                                                                    
    ''')
                else:
                    print('Oops,Looks Like The Code You Entered was')
                    print('Incorrect.Please Check & Try Again Later')
            elif select == 8:
                print('New XtraValue Plans.')
                print('''
1.N500 For 750MB + N500 TalkTime. Val/14Days    
2.N1,000 For 1.5GB + N1,000 TalkTime. Val/30Days    
3.2,000 For 4.5GB + N2000 TalkTime. Val/30Days    
0.Back    
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''''')
            elif select == 9:
                print('Buy & Get Free Data To Stream Youtube At Night(11PM To 6AM)')
                print('''
1.Weekly    
2.Monthly    
0.Back    
00.MainMenu    
    ''')
            elif select == 10:
                print('Manage Your Data Bundle')
                print('''
1.View Active Data Bundle    
2.Opt For Auto Renewal  
3.Cancel Auto Renewal  
4.Deal Zone Offer
0.Back  
    ''')
            elif select == 99:
                print('''
11.Pulse Tuesday Offer
0.Back    
    ''')
                chose = int(input("Chose: "))
                if chose == 11:
                    print('Service Is Temporary Unavailable')
                elif chose == 0:
                    print('''
1.Daily 
2.Weekly
3.Monthly
4.2-3 Month
5.Always On Plans
6.Mi-Fi Plans
7.Family Packs
8.Hot Deals
9.Free YouTube
10.Manage Data
99.Next
0.Back        
    ''')
                    print('Please Select Any Option')
                else:
                    print('Sorry You Enter Wrong Code!!!')
            elif select == 0:
                print(DAIL)
        elif Option == 2:#T0 Be Continued
            print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next
    ''')
            select = int(input('Chose: '))
            if select == 1:
                print('''
1.Daily @ N25
2.Weekly @ N50
3.Monthly @ N150
0.Back
    ''')
                chose = int(input("Chose: "))
                if chose == 1:
                    print('''
Activation of  Whatsapp Daily Plan Was Successful. You Have Be 
credited with 25MB Bundle Expires Tommmorrow By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.Thank You.
    ''')
                elif chose == 2:
                    print('''
Activation of  Whatsapp Weekly Plan Was Successful. You Have Be 
credited with 50MB Bundle Expires Next Week By 11:59PM, To Opt out 
Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.Thank You.
    ''')
                elif chose == 3:
                    print('''
Activation of  Whatsapp Monthly Plan Was Successful. You Have Be 
credited with 100MB Bundle Expires Next Month By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.Thank You.
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next
    ''')
                else:
                    print('Sorry Invalid Input')
            elif select == 2:
                print('FaceBook Plans')
                print('''
1.Daily @ N25
2.Weekly @ N50
3.Monthly @ N150
0.Back
    ''')
                chose = int(input("Chose: "))
                if chose == 1:
                    print('''
Activation of  FaceBook Daily Plan Was Successful. You Have Be 
credited with 25MB Bundle Expires Tomorrow By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You. 
    ''')
                elif chose == 2:
                    print('''
Activation of  FaceBook Weekly Plan Was Successful. You Have Be 
credited with 50MB Bundle Expires Next Week By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.
    ''')
                elif chose == 3:
                    print('''
Activation of  FaceBook Monthly Plan Was Successful. You Have Be 
credited with 100MB Bundle Expires Next Month By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next
    ''')
                else:
                    print('Sorry Invalid User Input')
            elif select == 3:
                print("Instagram Plans")
                print('''
1.N100 For 250MB/1-Day
2.N100 For 250MB
3.N200 For 1GB
4.N200 For 1GB/3-Days
0.Back
    ''')
                chose = int(input("Chose: "))
                if chose == 1:
                    print('''
Activation of  Instagram Daily Plan Was Successful. You Have Be 
credited with 250MB Bundle Expires Tomorrow By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.
    ''')
                elif chose == 2:
                    print('''
Activation of  Instagram Plan For N100 Was Successful. You Have Be 
credited with 250MB To Opt out Auto-Renewal Text N0114 To 131.Text 2 
For Data Balance.Thank You.
    ''')
                elif chose == 3:
                    print('''
Activation of  Instagram Plan For N200 Was Successful. You Have Be 
credited with 1GB To Opt out Auto-Renewal Text N0114 To 131.Text 2 
For Data Balance.Thank You.
    ''')
                elif chose == 4:
                    print('''
Activation of  Instagram 3-Days Plan Was Successful. You Have Be 
credited with 1GB Bundle Expires In The Next 3 Days By 11:59PM,To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next
    ''')
                else:
                    print('Sorry Invalid User Input')
            elif select == 4:
                print("TIK TOK Plans")
                print('''
1.N50 For 200MB/1-Day
2.N350 For 2Gb/7-Days
0.Back       
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''
Activation of  Tik Tok Daily Plan Was Successful. You Have Be 
credited with 200MB Bundle Expires Tomorrow By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.
    ''')
                elif chose == 2:
                    print('''
Activation of  Tik Tok 3-Days Plan Was Successful. You Have Be 
credited with 100MB Bundle Expires Next 3-Days By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.            
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next            
    ''')
                else:
                    print('Sorry Invalid/Incorrect Input')
            elif select == 5:
                print('''
1.N25 For 25MB/1-Day    
2.N50 For 50MB/7-Days
3.N150 For 150MB/30-Days
0.Back
00.MainMenu
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''
Activation of  Ayoba Daily Plan Was Successful. You Have Be 
credited with 25MB Bundle Expires Tommorrow By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.            
    ''')
                elif chose == 2:
                    print('''
Activation of  Ayoba Weekly Plan Was Successful. You Have Be 
credited with 50MB Bundle Expires Next Week By 11:59PM, To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.            
    ''')
                elif chose == 3:
                    print('''
Activation of  Ayoba Monthly Plan Was Successful. You Have Be 
credited with 150MB Bundle Expires Next Month By 11:59PM,To Opt 
out Auto-Renewal Text N0114 To 131.Text 2 For Data Balance.
Thank You.            
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next
    ''')
                elif chose == 00:
                    print(DAIL)
                else:
                    print('Sorry Wrong User Input')
            elif select == 6:
                print('''
For Use ONLY On Whatsapp,FaceBook,Istagram,
Ayoba,2GO,Wechat and Vskit.Select Any
1.Daily @ N50
2.Weekly @ N100
3.Monthly @ N250
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''
Activation of  Whatsapp,FaceBook,Istagram,Ayoba,2GO,
Wechat and Vskit Daily Plan Was Successful.You Have 
Be credited with 50MB Bundle Expires Tommorrow By 
11:59PM, To Opt out Auto-Renewal Text N0114 To 131.
Text 2 For Data Balance.Thank You.             
    ''')
                elif chose == 2:
                    print('''
Activation of  Whatsapp,FaceBook,Istagram,Ayoba,
2GO,Wechat and Vskit Weekly Plan Was Successful. 
You Have Be credited with 100MB Bundle Expires Next 
Week By 11:59PM, To Opt out Auto-Renewal Text N0114 
To 131.Text 2 For Data Balance.Thank You.                         
    ''')
                elif chose == 3:
                    print('''
Activation of  Whatsapp,FaceBook,Istagram,Ayoba,
2GO,Wechat and Vskit Monthly Plan Was Successful. 
You Have Be credited with 150MB Bundle Expires Next 
Month By 11:59PM, To Opt out Auto-Renewal Text N0114 
To 131.Text 2 For Data Balance.Thank You.                                     
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next            
    ''')
                else:
                    print('Oops Invalid Input')
            elif select == 7:
                print('''
Subscribe To This Bundle To Enjoy video Streaming Or 
Download On YouTube, Instagram & Tik Tok For 24hrs.
1.Daily @ N100
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''
Y'ellow You Have Successfully Subscribe To Enjoy Video 
Streaming or Download On Youtube,Instagram & Tik Tok For
24hrs,Thank You.
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next        
    ''')
            elif select == 8:
                print('''
For Use Only On Opera Mini browser and 
opera News.Streaming & Downloads Not 
Allowed.Select Any
1.N20/25MB/1Day
2.N50/100MB/7Days
3.N100/300MB/30Days
0.Back    
    ''')
                chose = int(input("Chose: "))
                if chose == 1:
                    print('''
Activation of  Opera Mini Browser & Opera Mini News Daily 
Plan Was Successful. You Have Be credited with 25MB Bundle 
Expires Tommorrow By 11:59PM, To Opt out Auto-Renewal Text 
N0114 To 131.Text 2 For Data Balance.Thank You.                        
    ''')
                elif chose == 2:
                    print('''
Activation of  Opera Mini Browser & Opera Mini News Weekly 
Plan Was Successful. You Have Be credited with 50MB Bundle 
Expires Next Week By 11:59PM, To Opt out Auto-Renewal Text 
N0114 To 131.Text 2 For Data Balance.Thank You.                                    
    ''')
                elif chose == 3:
                    print('''
Activation of  Opera Mini Browser & Opera Mini News Monthly 
Plan Was Successful. You Have Be credited with 100MB Bundle 
Expires Next Month By 11:59PM, To Opt out Auto-Renewal Text 
N0114 To 131.Text 2 For Data Balance.Thank You.                        
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles    
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next        
    ''')
                else:
                    print('Connection Problem Or Invalid MMI Code')
            elif select == 9:
                print('''
Subscribe To This Bundle To Enjoy Video Streaming Or 
Download On FaceBook,YouTube and Instagram.Select Any.
1.750MB For N200(3-Days)
2.1GB For N300(7-Days)
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 1:
                    print('''
Y'ellow You Have Successfully Subscribe To Enjoy Video 
Streaming or Download On FaceBook Youtube and Instagram 
For 3-Days,Thank You.
    ''')
                elif chose == 2:
                    print('''
Y'ellow You Have Successfully Subscribe To Enjoy Video 
Streaming or Download On FaceBook Youtube and Instagram 
For 7-Days,Thank You.   
    ''')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next                
    ''')
            elif select == 99:
                print('''
10.2GB
11.WeChat
12.Eskimi
0.Back
    ''')
                chose = int(input('Chose: '))
                if chose == 10:
                    print('''
1.Daily @ N25
2.Weekly @ N50
3.Monthly @ N150
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('''
Activation of  2GO Daily Plan Was Successful. You Have Be 
credited with 25MB, Bundle Expires Tomorrow By 11:59PM,To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.            
    ''')
                    elif pick == 2:
                        print('''
Activation of  2GO Weekly Plan Was Successful. You Have Be 
credited with 50MB, Bundle Expires Next Week By 11:59PM,To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.                        
    ''')
                    elif pick == 3:
                        print('''
Activation of  2GO Monthly Plan Was Successful. You Have Be 
credited with 100MB, Bundle Expires Next Month By 11:59PM,To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.                        
    ''')
                    elif pick == 0:
                        print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next                            
    ''')
                    else:
                        print('Service Is Temporary Unavailable')
                elif chose == 11:
                    print('''
1.Daily @ N25
2.Weekly @ N50
3.Monthly @ N150
0.Back
    ''')
                chose = int(input("Chose: "))
                if chose == 10:
                    print('''
1.Daily @ N25
2.Weekly @ N50
3.Monthly @ N150
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('''
Activation of  Wechat Daily Plan Was Successful. You Have Be 
credited with 25MB, Bundle Expires Tomorrow By 11:59PM, To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.            
    ''')
                    elif pick == 2:
                        print('''
Activation of  Wechat Weekly Plan Was Successful. You Have Be 
credited with 50MB, Bundle Expires Next Week By 11:59PM, To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.                        
    ''')
                    elif pick == 3:
                        print('''
Activation of  WeChat Monthly Plan Was Successful. You Have Be 
credited with 100MB, Bundle Expires Next Month By 11:59PM, To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.                        
    ''')
                    elif pick == 0:
                        print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next                            
    ''')
                    else:
                        print('Service Is Temporary Unavailable')
                elif chose == 12:
                    print('''
1.Daily @ N25
2.Weekly @ N50
3.Monthly @ N150
0.Back
    ''')
                    pick = int(input('Pick: '))
                    if pick == 1:
                        print('''
Activation of  Eskimi Daily Plan Was Successful. You Have Be 
credited with 25MB, Bundle Expires Tomorrow By 11:59PM,To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.            
    ''')
                    elif pick == 2:
                        print('''
Activation of  Eskimi Weekly Plan Was Successful. You Have Be 
credited with 50MB, Bundle Expires Next Week By 11:59PM,To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.                        
    ''')
                    elif pick == 3:
                        print('''
Activation of  Eskimi Monthly Plan Was Successful. You Have Be 
credited with 100MB, Bundle Expires Next Month By 11:59PM,To 
Opt out Auto-Renewal Text N0114 To 131.Text 2 For Data 
Balance Thank You.                        
    ''')
                    elif pick == 0:
                        print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next                            
    ''')
                    else:
                        print('Service Is Temporary Unavailable')
                elif chose == 0:
                    print('''
1.Whatsapp
2.Facebook
3.Instagram
4.Tik Tok
5.Ayoba
6.All Social Bundles
7.Youtube, Instagram and Tik Tok
8.Opera Mini & News
9.Social Mega Bundle
99.Next                            
    ''')
                else:
                    print('Invalid MMI Code/User Input')
            else:
                print('Oops,Looks Like The Code You Entered Was Incorrect')
        elif Option == 3:
            print(''' Your Data Balance is:
To Link Your NIN With Your Phone Number
Click On The Link https://bit.ly/3DVytHu
    ''')
        elif Option == 4:
            print('''
1.Roaming Data Bundles 
2.Roaming Voice + Data Bundles
3.Free Incoming Roaming Cell
4.Int Calling Bundle
5.Roaming Balance Check
    ''')
            chose = int(input('Chose: '))
            if chose == 1:
                print('''''')
            elif chose == 2:
                print('''''')
            elif chose == 3:
                print('''''')
            elif chose == 4:
                print('''''')
            elif chose == 5:
                print('''''')
            else:
                print('Service Is Temporary Unavailable')
        elif Option == 5:
            print('''
1.Borrow Airtime 
2.Borrow Data
3.Recharge
0.Back
    ''')
            chose = int(input('Chose: '))
            if chose == 1:
                print('''
Welcome To MTN Xtra Time. you Can Borrow 
Up-to N1,500.Service Fee Includes VAT
1:Borrow Data
2:My Account
    ''')
                pick = int(input('Pick: '))
                if pick == 1:
                    print('''
MTN XtraByte.Price Includes VAT        
1:2GB/2-Days @N576.80
2:1GB/7-Days @N576.80
0.Back
    ''')
                elif pick == 2:
                    print('''''')
                else:
                    print('Invalid MMI Code')
            elif chose == 2:
                print('''
Welcome To MTN Xtra Time. you Can Borrow 
Up-to N1,500.Service Fee Includes VAT
1:Borrow Data
2:My Account    
    ''')
            elif chose == 3:
                print('''''')
            elif chose == 0:
                print('''''')
            else:
                print('Service Is Temporary Unavailable')
        elif Option == 6:
            print('''
1.Transfer From Data balance
2.Buy For A Friend
3.Request From A Friend
4.View Pending Request
0.Back
00.MainMenu
    ''')
            chose = int(input('Chose: '))
            if chose == 1:
                Phone_Number = int(input("Enter Recipient's Number: "))
                print('''
You Have Successfully Transfered 2.5GB To 090xxxxxxxx    
    ''')
            elif chose == 2:
                print('''
Welcome To MTN Gifting.Select Data 
Plan To Gift:
1.Daily Plans
2.Weekly Plans
3.Monthly Plans
4.2-Months Plans
5.3-Months Plans
0.Back    
    ''')
                pick = int(input("Pick: "))
                if pick == 1:
                    print('''''')
                elif pick == 2:
                    print('''''')
                elif pick == 3:
                    print('''''')
                elif pick == 4:
                    print('''''')
                elif pick == 5:
                    print('''''')
                elif pick == 0:
                    print('''''')
                else:
                    print('Sorry Invalid Input')
            elif chose == 3:
                print('''''')
            elif chose == 4:
                print('''''')
            elif chose == 0:
                print('''
            
    ''')
            elif chose == 00:
                print(DAIL)
            else:
                print('Sorry Wrong/Invalid Input')
        elif Option == 7:
            print('''
1.YouTube Video Packs
2.StarTimes Video Packs 
3.1GB (YouTube Only) + 500MB (Data Access)
4.Showmax Mobile
    ''')
            chose = int(input("Chose: "))
            if chose == 1:
                print('''
1.1Hour @ N50
2.3Hours @ N130
3.500MB @ N50(12am - 5am)
4.2GB Weekly @ N200(11pm - 6am)
5.Check Balance    
    ''')
                pick = int(input('Pick: '))
                if pick == 1:
                    print('''''')
                elif pick == 2:
                    print('''''')
                elif pick == 3:
                    print('''''')
                elif pick == 4:
                    print('''''')
                elif pick == 5:
                    print('''''')
                else:
                    print('UNKNOWN APPLICATION')
            elif chose == 2:
                print('''''')
            elif chose == 3:
                print('''''')
            elif chose == 4:
                print('''''')
            else:
                print('UNKNOWN APPLICATION')
        elif Option == 8:
            print('''
1.TopDeal 4ME
2.Data 4ME
3.Recharge 4ME
4.Combo 4ME
5.VAS 4ME
    ''')
            chose = int(input('Chose: '))
            if chose == 1:
                print('''
1.Enjoy 1.5GB For N500
0.Back
    ''')
                pick = int(input('Pick: '))
                if pick == 1:
                    print('''
Congratulations! You have successfully Purchased 1.5GB
Data For N500 To Browse Your Favourite Websites.Data Is
Valid For 7 Days. Dial *131*4# To View Data,To Link Your 
NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.       
    ''')
                elif pick == 2:
                    print(DAIL)
                else:
                    print('Wrong User Input')
            elif chose == 2:
                print('''
1.Enjoy 1.5GB For N300
2.Enjoy 2GB For N500
0.Back
    ''')

                pick = int(input("Pick: "))
                if pick == 1:
                    print('''
Congratulations! You have successfully Purchased 1.5GB
Data For N300 To Browse Your Favourite Websites.Data Is
Valid For 7 Days. Dial *131*4# To View Data,To Link Your 
NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.        
    ''')
                elif pick == 2:
                    print('''
Congratulations! You have successfully Purchased 2GB
Data For N500 To Browse Your Favourite Websites.Data Is
Valid For 7 Days. Dial *131*4# To View Data,To Link Your 
NIN With Your Phone Number Click On The Link:
https://bit.ly/3DVytHu.                   
    ''')
                elif pick == 0:
                    print(DAIL)
                else:
                    print('UNKNOWN APPLICATION')
            elif chose == 3:
                print('''
1.Recharge N100 and Get N2,400
2.Recharge N100 and Get Free 10MB
    ''')
            elif chose == 4:
                print('''
1.Enjoy 24mins For Calls and 200MB To Browse
2.Enjoy 12mins For Calls and 100MB To Browse
    ''')
                pick = int(input("Pick: "))
                if pick == 1:
                    print('''
Congratulations! You Now Enable To Enjoy All Calls For 24Mins 
and also Credited With 200MB To Browse All Network        
    ''')
                elif pick == 2:
                    print('''
Congratulations! You Now Enable To Enjoy All Calls For 12Mins 
and also Credited With 100MB To Browse All Network        
    ''')
                else:
                    print('UNKNOWN APPLICATION')
            elif chose == 5:
                print('''
1.Win N100,000 CASH Instantly.
2.Win Airtime and Up To N100,000,000 CASH
    ''')
            else:
                print('Invalid MMI Code')
        elif Option == 9:
            print('''Yellow! Need Help? Chat With Zigi On Your Preferred 
Channels;Whatsapp, Facebook Messenger, Web and Telegram.
Detail Via SMS.''')
    else:
        print("Sorry Invalid IMEI Code")









