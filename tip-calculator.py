print("Welcome to the tip calculator")
bill = input("what was the total bill ? $")
person = input("How many people to spllit the bill ? ")
tips = input("What percentage tip would you like to give ? 10, 12 or 15 ? ")

tips_person = int(tips) / 100
result = round((float(bill) / int(person)) * tips_person, 2)
print(result)