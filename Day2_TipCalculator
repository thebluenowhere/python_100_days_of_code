# TIP CALCULATOR

# welcome message
print("Welcome to the tip calculator!")

#input for total bill (float)
total_bill = float(input("What was the total bill? "))

# input for tip given (integer)
tip = int(input("How much would you like to give? 10, 12, or 15? "))

# tip as a percentage 
tip_percent = 1 + tip / 100 

# Number of people splitting bill (integer)
split = int(input("How many people to split the bill? "))

result = (total_bill / split) * tip_percent
result = round(result, 2)
# using f string to force output to 2 decimal spaces even if it rounds at 1
print(f"Each person should pay: ${result:.2f}")
