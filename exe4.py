#Receiving information from user
pop = int(input("Report a population value for city A: \n"))
pop_2 = int(input("Report a population value for city B: \n"))
growing = float(input("Report a population growth % value for city A: \n"))
growing_2 = float(input("Report a population growth % value for city B: \n"))

percentage1 = int(growing/100)
percentage2 = int(growing_2/100)

first_operation = int(pop + (percentage1 * pop))
second_operation = int(pop_2 + (percentage2 * pop_2))
t = 0
condition = pop <= pop_2
#Operating with information
while condition == True:
    pop += first_operation
    pop_2 += second_operation
    t += 1
print(t)