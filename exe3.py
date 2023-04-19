#Receiving information from user
name = input("Type your name: \n")
age = input("Type your age: \n")
age = int(age)
money = input("How much money do you receive? \n")
money = int(money)
sex = input("What's your sex? M or F \n")
civil_state = input("What's you civil state? S, C, V, D \n")
confirm = False
while confirm == False:
    if len(name) < 3 :
        name = input("Type your name: \n")
    if age < 0 or age > 150 :
        age = int(input("Type your age: \n"))
        age = int(age)
    if money < 0 :
        money = int(input("How much money do you receive? \n"))
        money = int(money)
    print("All okay!")
    break
