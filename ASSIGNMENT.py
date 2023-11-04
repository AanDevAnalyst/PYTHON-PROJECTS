from time import *
print("\t___________________________________________________________________")
print("                                                                      ")
print("\t!!!......WELCOME TO AMINU KANO TECHING HOSPITAL(AKTH).........!!!!")
print("           \a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
print("\t___________________________________________________________________")
print("\v first_doctor(input)\n\b second_doctor(Input)\n\v fourth_doctor(input)\n\b fifth_doctor(input)\n\v bed_space(bed_count)\n\b hospital(hospital_number\n\v complain(patient_complain)")

ANNOUNCEMENT = '''
HOSPITAL MANAGEMENT,

      To inform patient to make sure they are well treated before leaving the hospital

    to open up to their assign doctor,legal process must be followed to have a file with
    
    with the hospital.

LASTLY,

    Make sure to report any inconvinecies to the available authorities,
    THANK YOU.

'''
choice = 0
def menu(choice):
    while choice <= 5:
        choice+=1
        x = int(input("CHOOSE: "))
        if choice == 1:
            print(first_doctor(department_of_physiotheraphy))
            
        elif choice == 2:
            print(second_doctor(department_of_dentistry))

        elif choice == 4:
            print(third_doctor(department_of_ear_nose_and_throat))

        elif choice == 5:
            print(fourth_doctor(department_of_pharmacy))

        elif choice == 6:
            print(fifth_doctor(department_of_physiotheraphy))

        else:
            print("wrong in put".upper())
print(ANNOUNCEMENT)
department_of_physiotheraphy =  "muscle problem"
def first_doctor(department_of_physiotheraphy):
    department_of_physiotheraphy = {
        "name": "prof.Abdullahi Idris",
        "age": "28",
        "specialization": "physiotheraphist",
        "room_number": "1AB"
    }
    print(department_of_physiotheraphy["name"])
    print(department_of_physiotheraphy["age"])
    print(department_of_physiotheraphy["specialization"])
    print(department_of_physiotheraphy["room_number"])
department_of_dentistry = "tooth problem"
def second_doctor(department_of_dentistry):
    department_of_dentistry = {
    "name": "Bello Ibrahim",
    "age": "35",
    "specialization":"Tooth Doctor",
    "room_number": "2BC"
}
    print(department_of_dentistry["name"])
    print(department_of_dentistry["age"])
    print(department_of_dentistry["specialization"])
    print(department_of_dentistry["room_number"])
    print("YOU MAY PROCEED FOR YOUR MEDICATION")

department_of_ear_nose_and_throat = "ear, nose or throat problem"
def third_doctor(depatment_of_ear_nose_and_throat):
    depatment_of_ear_nose_and_throat = {
    "name": "Amir Shehu Yakasai",
    "age": "40",
    "specialization": "Ear doctor",
    "room_number": "3DF"
}
    print(depatment_of_ear_nose_and_throat["name"])
    print(depatment_of_ear_nose_and_throat["age"])
    print(depatment_of_ear_nose_and_throat["specialization"])
    print(depatment_of_ear_nose_and_throat["room_number"])
    print("YOU MAY PROCEED FOR YOUR MEDICATION")
    
department_of_phrmacy = "Medicien"
def fourth_doctor(department_of_phrmacy):
    department_of_phrmacy = {
    "name": "Muhammad Abdulmajid",
    "age": "37",
    "specialization": "phramasist",
    "room_number": "5JK"
}
    print(department_of_phrmacy["name"])
    print(department_of_phrmacy["age"])
    print(department_of_phrmacy["specialization"])
    print(department_of_phrmacy["room_number"])
    print("YOU MAY PROCEED FOR YOUR MEDICATION")
    
department_of_physiotheraphy = "muscle problem"
def fifth_doctor(department_of_physiotheraphy):
    department_of_physiotheraphy = {
    "name": "Muhammad Abdulmajid",
    "age": "37",
    "specialization":"physiotheraphist",
    "room_number": "6GH"
}
    print(department_of_physiotheraphy["name"])
    print(department_of_physiotheraphy["age"])
    print(department_of_physiotheraphy["specialization"])
    print(department_of_physiotheraphy["room_number"])
    print("YOU MAY PROCEED FOR YOUR MEDICATION")

        
hospital_number=1
def hospital(hospital_number):
    while hospital_number <=5:
        print("please show your hospital verification number".upper())
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

patient_complain = input("COMPLAIN: ")
def complain(patient_complain):
    if patient_complain == "tooth problem": 
        print("please show doctor details")
        print(second_doctor(department_of_dentistry))
        

    elif patient_complain == "muscle problem":
        print("you assign to fifth doctor")
        print(fifth_doctor(department_of_physiotheraphy))
            

    elif patient_complain == "ear problem":
        print("you are assign to third doctor")
        print(third_doctor(department_of_ear_nose_and_throat))


    elif patient_complain == "medicien":
        print("you are assign to fourth doctor")
        print(fourth_doctor(department_of_phrmacy))


    elif patient_complain == "throat problem":
        print("you are assign to third doctor")
        print(third_doctor(department_of_ear_nose_and_throat))


    else:
        print("you are not assign properly to the right doctor".upper())    


bed_count = 1
def bed_space(bed_count):
    print("number of available bed spaces")
    while bed_count <= 100:
        print(bed_count)
        bed_count = bed_count + 1   


    

    


  
