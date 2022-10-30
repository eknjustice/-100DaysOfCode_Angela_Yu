print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
tipPercentage = int(input("What percentage tip would you like to give? 10,12, or 15? "))
peopleSharingBill = int(input("How many people to split the bill? "))
tipAmount = (tipPercentage / 100) * totalBill
totalCost = totalBill + tipAmount
sharePerPerson = totalCost / peopleSharingBill
print(f"Each person should pay: $"+"{:.2f}".format(sharePerPerson))
