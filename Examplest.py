hospital_number=1
while hospital_number <=5:
    print("please show you hospital verification".upper())
    hospital_number +=1
    hospital_id = str(input("HOSPITAL CARD: "))
    if len(hospital_id) <5:
        print("hospital id must be atleast 5 characters")
        continue

    elif len(hospital_id) >5:
        print("hospital id must be a maximum of 5 characters")
        hospital_id == 5
        continue
    
    else:
        print("YOU MAY PROCEED FOR YOUR MEDICATIONS!")
        break   

bed_count = 1
print("number of available bed spaces")
while bed_count <= 20:
    print(bed_count)
    bed_count = bed_count + 1
bed_number = int(input("enter bed number assign to: "))
def bed_count():
    print("only assign patient are allowed to be bededd")
    
HOSPITAL_NOTIFICATION="""
HOSPITAL MANAGER,

      To inform patient to make sure they are well treated well and make sure

    to open up to their assign doctor and make sure to follow the legal process

    to open file with the hospital

LASTLY,

    Make sure to report any inconvinecies to the available authorities."""
    
