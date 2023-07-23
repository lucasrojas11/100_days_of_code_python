print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
persentage_tip = int(input("What persentage tip would you like to give? 10, 12 or 15? "))
persentage = (persentage_tip * bill) /100 
people = int(input("How many people to split the bill? "))

tip = round((persentage + bill) / people, 2)

print(f"Each person sould pay: {tip}") 