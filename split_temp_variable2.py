# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


user_username = input('Please enter your username: ')
save_into_db(user_username)
user_birthyear = int(input('Please enter your birth year: '))
age = 2020 - user_birthyear
print("You are",age, "years old.")
