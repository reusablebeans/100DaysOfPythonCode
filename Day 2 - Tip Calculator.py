# Greeting message introducing program
print("Thank you for using the Tip Calculator!")

# Theses gather inputs to calculate the tip
total_cost = float(input("Enter the cost of the total bill: "))
percent_tip = float(input("Enter the tip percentage you would like to give: "))
num_ppl = int(input("Enter how many people are splitting the bill: "))

# This calculates the total tip
total_tip = total_cost * (percent_tip / 100)
# This calculates the tip paid per person
tip_per_person = round(total_tip / num_ppl, 2)

# Outputs the amount of tip money paid out per person
print(f"Each person should pay the following: ${tip_per_person}")
