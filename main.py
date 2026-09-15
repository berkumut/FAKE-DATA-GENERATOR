from faker import Faker

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

print(""" SELECT A VALUE : 

    1- SELECT 1 FOR ENGLİSH
    2- SELECT 2 FOR TURKISH
    3- SELECT 3 FOR GERMAN
    4- SELECT 4 FOR RUSSIAN
    5- SELECT 5 FOR FRENCH
""")

choice = input("PİCK A NUMBER : 1,2,3,4,5 :")

if choice not in languages:
    print("Please enter a valid value !!!")
    exit()

while True:
    try:
        fakeLength = int(input("Enter how many you want to create :"))
        break

    except ValueError:
        print("Please enter a valid value !!!")
        exit()

fake = Faker(languages[choice]["locale"])

for i in range(fakeLength):

    user = {

        "Name" : fake.name(),
        "Age" : fake.random_int(min=18, max=83),
        "Email" : fake.email(),
        "Phone" : languages[choice]["phone_code"] + fake.numerify("##########"),

    }

    print(user)