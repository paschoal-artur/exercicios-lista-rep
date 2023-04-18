#Receiving information from user
user = input("Username: \n")
password = input("Password: \n")

while str(user) == str(password) :
    print("Error, check your information and try again!")
    input("Username: \n")
    input("Password: \n")