#Receiving information from user
pop = int(input("Report a population value for city A: \n"))
pop_2 = int(input("Report a population value for city B: \n"))
growing = float(input("Report a population growth % value for city A: \n"))
growing_2 = float(input("Report a population growth % value for city B: \n"))

years = 0

#Operating with information
while pop <= pop_2 :
    pop += pop * (growing/100)
    pop_2 += pop_2 * (growing_2/100)
    years += 1
print(f"Population 1 passes population 2 in number of people in {years} years.")
