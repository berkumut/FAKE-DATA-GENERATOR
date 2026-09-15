from faker import Faker

# LANGUAGE SETTİNGS
languages = {
    "1": {
        "locale": "en_US",
        "country": "United States",
        "phone_code": "+1",
    },

    "2": {
        "locale": "tr_TR",
        "country": "Turkey",
        "phone_code": "+90",
    },

    "3": {
        "locale": "de_DE",
        "country": "Germany",
        "phone_code": "+49",
    },

    "4": {
        "locale": "ru_RU",
        "country": "Russia",
        "phone_code": "+7",
    },

    "5": {
        "locale": "fr_FR",
        "country": "France",
        "phone_code": "+33",
    },
}

# PRINTS THE SELECTION TO THE SCREEN
print(""" SELECT A VALUE : 

    1- SELECT 1 FOR ENGLİSH
    2- SELECT 2 FOR TURKISH
    3- SELECT 3 FOR GERMAN
    4- SELECT 4 FOR RUSSIAN
    5- SELECT 5 FOR FRENCH
""")

# IT GIVES THE USER A CHOICE
choice = input("PİCK A NUMBER : 1,2,3,4,5 :")

# IF THEY GIVE A DIFFERENT NUMBER, I WILL WARN THEM AND LEAVE
if choice not in languages:
    print("Please enter a valid value !!!")
    exit()

# IT ASKS THE USER HOW MANY LETTERS THEY WANT
while True:
    try:
        fakeLength = int(input("Enter how many you want to create :"))
        break

    except ValueError:
        print("Please enter a valid value !!!")
        exit()

# WE ARE ASSIGNING IT TO A VARIABLE
fake = Faker(languages[choice]["locale"])

# IT ROTATES AS MUCH AS THE USER WANTS
for i in range(fakeLength):

    user = {

        "Name" : fake.name(),
        "Age" : fake.random_int(min=18, max=83),
        "Email" : fake.email(),
        "Phone" : languages[choice]["phone_code"] + fake.numerify("##########"),

    }

    print(user)