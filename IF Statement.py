from time import *





def browser(website):
    welcome_greeting = '''
Dear Students,

Welcome to another new session which Marks 

The Beginning of 2050/2051 Academic Session

Please Be Aware of Malicious Website.

Thank you,
From The Office of VC Prof.Catherine Halsey.
'''
    first_semester = '''
'Code'                      'Course Title'                  'Credits'

'CHM1231'                  'Inorganic Chemistry'                '2'

'CHM1241'                   'Organic Chemistry'                 '2'

'CSC1201'              'Introduction to Computer Science'       '2'

'GSP1201'                    'Use of English'                   '2'

'MTH1301'                'Elementary Mathematics I'             '3'

'MTH1302'                'Elementary Mathematics II'            '3'

'PHY1170'                  'Physics Practical I'                '1'

'PHY1210'                        'Mechanics'                    '2'

'PHY1220'                 'Electricity and Magnetism'           '2'
'''
    second_semester = '''
'Code'                      'Course Title'                  'Credits'

'CHM1251'                 'Physical Chemistry'                  '2'

'CHM1261'                 'Practical Chemistry'                 '2'

'GSP1202'            'Use of Library,Study Skills & ICT'        '2'

'MTH1303'             'Elementary Mathematics III'              '3'

'PHY1180'                'Physics Practical II'                 '1'

'PHY1230'                'Behaviour of Matter'                  '2'

'STA1311'                  'Probability I'                      '3'

'''

    URL = 'www.buk.edu.ng'
    while True:

        if website == "":
            print("User didn't Enter Any URL")
            break
        elif website != URL:
            print('The URL You Entered Is Not Available On The Server')
            break
        elif website == URL:
            print('LOADING !!!')
            n = 1
            while n < 2:
                sleep(2)
                n += 1
            print(welcome_greeting)
            print('BUK Registration Portal')
            n = 1
            while n < 2:
                sleep(1)
                n += 1
            User_name = input('Enter Your Username: ')

            Pass_word = input('Key In Password: ')
            if len(Pass_word) < 4:
                print('Minimum Length of Password must Be At-least  11 character')

            elif len(Pass_word) == 11:
                print('''
If You Click on Okay Your Password Will Be Saved To System Automatically
1.Okay
    ''')
                click = int(input('Click: '))
                if click == 1:
                    print('Your Password Has Been Saved')
                    print('''
To Proceed With Your Registration Select Any Option Below
1.Student Information Form
2.Payment of Registration Fees
3.Course Registration Form
4.Student Accommodation Form
    ''')
                    option = int(input('Option: '))
                    if option == 1:  #
                        print('''
1.Student Personal and Academic Information
2.Student Contact Information
3.Next of Kin Information
4.Health Information
5.Attestation or Declaration
    ''')
                        pick = int(input('Pick: '))
                        if pick == 1:
                            print('''
\t\t\tSTUDENT PERSONAL AND ACADEMIC INFORMATION
    ''')
                            Full_name = input('FULL NAME: ').capitalize()
                            Registration_number = input('REGISTRATION NO_: ')
                            Faculty = input('FACULTY: ').capitalize()
                            Department = input('DEPARTMENT: ').capitalize()
                            Programme = input('PROGRAMME: ').capitalize()
                            try:
                                Level = int(input('LEVEL: '))
                            except ValueError:
                                print('Invalid Value')
                            JAMB_No = input('JAMB NO_: ')
                            Entry_status = input('ENTRY STATUS: ').capitalize()
                            Marital_status = input('MARITAL STATUS: ').capitalize()
                            Country = input('COUNTRY: ').capitalize()
                            State_region = input('SATE/REGION: ').capitalize()
                            Local_govt_area = input('LOCAL GOVT. AREA: ').capitalize()
                            Mode_of_Entry = input('MODE OF ENTRY: ').upper()
                            Mode_of_Study = input('MODE OF STUDY: ').capitalize()
                            Date_of_Birth = input('DATE OF BIRTH: ').capitalize()
                            Gender = input('GENDER: ')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(f'''
FULL NAME: {Full_name}
REG NUMBER: {Registration_number}
FACULTY: {Faculty}
DEPARTMENT: {Department}
PROGRAMME: {Programme}
LEVEL: {Level}
JAMB NUMBER: {JAMB_No}
ENTRY STATUS: {Entry_status}
MARITAL STATUS: {Marital_status}
COUNTRY: {Country}
STATE/REGION: {State_region}
LOCAL GOVT.AREA: {Local_govt_area}
MODE OF ENTRY: {Mode_of_Entry}
MODE OF STUDY: {Mode_of_Study}
DATE OF BIRTH: {Date_of_Birth}
GENDER: {Gender}
    ''')
                            break
                        elif pick == 2:
                            print('''
\t\t\t\t\tSTUDENT CONTACT INFORMATION
    ''')
                            try:
                                Phone_No = int(input('PHONE NUMBER: '))
                            except ValueError:
                                print('Invalid Value')
                            Username = input('USER NAME: ').lower()
                            Email = input('EMAIL: ').lower()
                            Address = input('ADDRESS: ').capitalize()
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(f'''
Phone Number: {Phone_No}
Username: {Username}
Email: {Email}
Address: {Address}
    ''')
                            break
                        elif pick == 3:
                            print('''
\t\t\t\t\tNEXT OF KIN INFORMATION                    
    ''')
                            Kin_Full_Name = input('FULL NAME: ').capitalize()
                            Relation_ship = input('RELATIONSHIP: ').capitalize()
                            try:
                                Phone = int(input('PHONE NUMBER: '))
                            except ValueError:
                                print('Invalid Value')
                            Email = input('EMAIL: ').lower()
                            Address = input('ADDRESS: ').capitalize()
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(f'''
Kin_Full_Name: {Kin_Full_Name}
Relation_ship: {Relation_ship}
Email: {Email}
Address: {Address}
    ''')
                            break
                        elif pick == 4:
                            print('''
\t\t\t\t\tHEALTH INFORMATION                    
    ''')
                            Health_Status = input('HEALTH STATUS: ').capitalize()
                            Blood_Group = input('BLOOD GROUP: ').upper()
                            Disability = input('DISABILITY: ').capitalize()
                            Medication = input('MEDICATION: ').capitalize()
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            print(f'''
Health_Status: {Health_Status}    
Blood Group: {Blood_Group} 
Disability: {Disability}
Medication: {Medication}
    ''')
                            break
                        elif pick == 5:
                            Full_name = input('FULL NAME: ').capitalize()
                            Registration_number = input('REGISTRATION NO_: ')
                            print(f'''
\t\t\t\t\tATTESTATION OR DECLARATION
\t\tI HEREBY CERTIFY THAT ALL INFORMATION ABOVE ARE CORRECT
        _____________________________________________________
            {Full_name} {Registration_number}                         
    
    ''')
                            break
                        else:
                            print('Sorry Wrong Input')
                    elif option == 2:
                        print('To Make Your Payment Using REMITA Filling The Form ')
                        Name_of_Card_Holder = input('NAME OF CARD HOLDER: ').capitalize()
                        try:
                            Card_Number = int(input('CARD NUMBER: '))
                        except ValueError:
                            print('Invalid Value')
                        Service_Type = input('SERVICE TYPE: ')
                        Expiry_Date = input('EXPIRY DATE: ')
                        try:
                            Cvv = int(input('CVV: '))
                        except ValueError:
                            print('Invalid Value')
                        Amount_paid = int(input('AMOUNT PAID: '))
                        print('''
\t\t\t\t\tREMITA (HIDE PAYMENT) DETAIL REMITA RETRIEVAL REFERENCE                    
    ''')
                        break
                    elif option == 3:  # Courses Registration Form
                        print('''
Select option to Register Courses
1.First Semester
2.Second Semester
3.Registration Completed
    ''')
                        select = int(input('Select: '))
                        if select == 1:
                            Total_First_Semester_Registered_Credits = 19
                            print(f'''
\t\t\t\t\tFIRST SEMESTER COURSES
{first_semester}
\t\t\t\t\tTOTAL FIRST SEMESTER REGISTERED CREDITS: {Total_First_Semester_Registered_Credits}
    ''')
                            print('First Semester Courses Registered')
                            break

                        elif select == 2:
                            Total_Second_Semester_Registered_Credits = 15
                            print(f'''
\t\t\t\t\tSECOND SEMESTER COURSES
{second_semester}
\t\t\t\t\tTOTAL SECOND SEMESTER REGISTERED CREDITS: {Total_Second_Semester_Registered_Credits}
    ''')
                            print('Second Semester Courses Registered')
                            break

                        elif select == 3:
                            print('PLEASE WAIT !!!')
                            n = 1
                            while n < 2:
                                sleep(3)
                                n += 1
                            Total_Credits_Registered_For_The_Session = 19 + 15
                            print(f'''
FIRST SEMESTER COURSES                        
{first_semester}
SECOND SEMESTER COURSES
{second_semester}
\t\t\t\t\tTOTAL CREDITS REGISTERED FOR THE SESSION: {Total_Credits_Registered_For_The_Session}
    ''')
                            print('COURSES REGISTRATION COMPLETED')
                            break

                        else:
                            print('Sorry Wrong Input')
                    elif option == 4:  # Student Accommodation Form
                        print('''''')
                    else:
                        print('Available Options Are Five Please Chose From Them')
                else:
                    print('Please Select From The Provided Option.')

            elif len(Pass_word) > 5:
                print('Length of password will be difficult for You To Remember')

            else:
                print('Password Must Be 11 Characters')


website = input('Enter Your School URL: ').lower()
browser(website)



