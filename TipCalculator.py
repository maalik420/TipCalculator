print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_share = int(bill*(tip/100))
total_bill = bill + tip_share
Person_share = total_bill / people
print((f"Each person should pay: $ {Person_share}" ))
