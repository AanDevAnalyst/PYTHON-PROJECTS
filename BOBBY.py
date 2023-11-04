print("************************************")
print("!!!......WELCOMME TO AMINU KANO TECHING HOSPITAL(AKTH)......!!!")
card_number = int(input("Hospital number: "))
card_number = 1
while card_number <= 11:
    print("welcome to AKTH please you may have a seat")
    card_number = card_number + 1
doctor_identification = {
    "name": "prof.Abdullahi Idris",
    "age": "28",
    "department": "optimatry",
    "area_of_specialization": "optimatist"
}
message = input(">")
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "Iam happy",
        ":(": "I am sad"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        print(output)

    
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

    
