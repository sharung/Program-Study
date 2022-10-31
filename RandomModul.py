import random

# randomDecimal = round(random.random() * 5)
# print(randomDecimal)


# # coin = random.randint(0, 1)
# coin = round(random.random())
# if coin == 1:
#     print("Heads")
# else:
#     print("Tails")


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random
name = names[round(random.random() * (len(names) - 1))]
print(f"{name} is going to buy the meal today!")
# choice()
random.choice(name)











