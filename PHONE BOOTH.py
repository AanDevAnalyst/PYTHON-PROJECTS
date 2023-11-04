import random

identifier = [
'+93',"+355","+213","+376","+244","+1264","672","+1268","+54","+374","+297","+61","+43","+251"
    
"+994","+1242","+973","+880","+375","+32","+359","+226","+257","+855","+237","+238","+1345",

"+236","+235","+56","+86","+225","+45","+253","+1767","+593","+20","+503","+240","+291","+372",

]
countries = [
"Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antarctica","Antigua & Barbuda","Argentina",

"Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Belarus","Belgium",

"Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Central African Republic",

"Chad","Chile","China","Cote d'Ivoire","Denmark","Djibouti","Dominica","Ecuador","Egypt","El Salvador","Eritrea",

"Equatorial Guinea", "Estonia","Ethiopia"
]
Tuples = (+234,+98,+355)
print(Tuples)
picked = random.choice(countries)
if picked == "Cambodia":
    print(f"+855: {identifier}")
print(picked)
print(identifier)
phone = input('PHONE NUMBER: ')
code_identifier = {
    "93": "Afghanistan",
    "355": "Albania",
    "213": "Algeria",
    "376": "Andorra",
    "244": "Angola",
    "1264": "Anguilla",
    "672": "Antarctica",
    "1268": "Antigua & Barbuda",
    "54": "Argentina",
    "374": "Armenia",
    "297": "Aruba",
    "61": "Australia",
    "43": "Austria",
    "994": "Azerbaijan",
    "1242": "Bahamas",
    "973": "Bahrain",
    "880": "Bangladesh",
    "375": "Belarus",
    "32": "Belgium",
    "359": "Bulgaria",
    "226": "Burkina Faso",
    "257": "Burundi",
    "855": "Cambodia",
    "237": "Cameroon",
    "238": "Cape Verde",
    "1345": "Cayman Islands",
    "236": "Central African Republic",
    "235": "Chad",
    "56": "Chile",
    "86": "China",
    "225": "Cote d'Ivoire",
    "45": "Denmark",
    "253": "Djibouti",
    "1767": "Dominica",
    "593": "Ecuador",
    "20": "Egypt",
    "503": "El Salvador",
    "240": "Equatorial Guinea",
    "291": "Eritrea",
    "372": "Estonia",
    "251": "Ethiopia",
}
output = ""
for ch in phone:
    code_identifier.get(ch,"!!!")
    output += code_identifier + " "

print(output)