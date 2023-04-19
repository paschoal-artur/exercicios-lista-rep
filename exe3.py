#Receiving information from user
name = input("Type your name: \n")
age = input("Type your age: \n")
money = input("How much money do you receive? \n")
sex = input("What's your sex? M or F \n")
civil_state = input("What's you civil state? S, C, V, D \n")
three = 3

name_1 = name > "tri"
age_1 = int(age) > 0 and int(age) < 150
money_1 = int(money) > 0
sex_1 = "M" or "F"
civil_state_1 = "C" or "S" or "V" or "D"

all_true = name_1 + age_1 + money_1 + sex_1 + civil_state_1

while all_true :
    print("All okay!")
    break
