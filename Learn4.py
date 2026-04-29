# Conditionals

# These are all FALSY — Python treats them as False in conditions
if 0:           print("runs")   # does not run
if 0.0:         print("runs")   # does not run
if "":          print("runs")   # does not run — empty string
if []:          print("runs")   # does not run — empty list (Lesson 5)
if None:        print("runs")   # does not run

# These are all TRUTHY — Python treats them as True in conditions
if 1:           print("runs")   # runs — any non-zero number
if -5:          print("runs")   # runs — negative numbers too
if "hello":     print("runs")   # runs — any non-empty string
if "0":         print("runs")   # runs — the STRING "0" is truthy



print("=" * 45)
print("     LOAN ELIGIBILITY CHECKER".center(45))
print("=" * 45)

name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))
monthly_income = float(input("Enter monthly income (Rs.): "))
employment_type = input("Employment type (salaried/self-employed): ").strip().lower()
credit_score = int(input("Enter your credit score (300-900): "))
loan_amount = float(input("Loan amount requested (Rs.): "))

# Eligibility checks
is_age_eligible = 21 <= age <= 60
is_income_eligible = monthly_income >= 25000
is_credit_eligible = credit_score >= 700
is_employment_valid = employment_type in ("salaried", "self-employed")

# Determine max loan based on income
max_loan = monthly_income * 60   # standard: 60x monthly income

# Decision logic
print("\n" + "=" * 45)
print(f"  ELIGIBILITY REPORT FOR {name.upper()}")
print("=" * 45)

if not is_employment_valid:
    print("Invalid employment type entered.")
elif not is_age_eligible:
    print(f"Age {age} is not eligible. Must be between 21 and 60.")
elif not is_income_eligible:
    print(f"Income Rs.{monthly_income:,.0f} is below minimum Rs.25,000.")
elif not is_credit_eligible:
    print(f"Credit score {credit_score} is too low. Minimum is 700.")
elif loan_amount > max_loan:
    print(f"Requested Rs.{loan_amount:,.0f} exceeds max eligible Rs.{max_loan:,.0f}.")
else:
    # All checks passed
    interest_rate = 8.5 if employment_type == "salaried" else 10.5
    status = "APPROVED"
    print(f"Status          : {status}")
    print(f"Loan amount     : Rs.{loan_amount:,.0f}")
    print(f"Interest rate   : {interest_rate}%")
    print(f"Max eligible    : Rs.{max_loan:,.0f}")

print("=" * 45)


# Exercise 1: Ask the user for a number. Print whether it is positive, negative, or zero. 
# Then also print whether it is even or odd. Both pieces of information must always print.

user_input = int(input("Enter a number : "))

if user_input > 0:
    print("Positive")
elif user_input < 0:
    print("Negative")
else:
    print("Zero")

if user_input % 2 == 0:
    print("even")
else:
    print("odd")

# Exercise 2: Ask the user for their age and whether they have a driving licence (yes/no). 
# Print one of four possible outcomes: under age with licence, under age without licence, of age with licence, of age without licence. 
# Each outcome has a different message.

user_age = int(input("Enter your age : "))
user_dl = input("Enter if you have a driving licence (yes/no) : ").strip().lower()


if user_dl not in ("yes","no"):
    print("Invalid input enetered - Enter Yes or No")
elif user_age < 18 and user_dl == "yes":
    print(f"Under age with License")
elif user_age < 18 and user_dl == "no":
    print(f"Under age without License")
elif user_age >= 18 and user_dl == "yes":
    print(f"of age with License")
elif user_age >= 18 and user_dl == "no":
    print(f"of age without License")


# Exercise 3: Ask the user for a temperature and the unit (C or F). 
# If Celsius — convert to Fahrenheit and classify as Freezing (below 0°C), Cold (0–15), Comfortable (16–25), Hot (26–35),
#  or Extreme (above 35). If Fahrenheit — convert to Celsius first then classify. Formula: C = (F - 32) * 5/9 and
#  F = C * 9/5 + 32.

temperature = float(input("Enter the temperature : "))
unit = input("Enter the unit (C or F) : ").strip().upper()

if unit == "C":
    F = float(temperature * 9.0/5.0 + 32.0)   
elif unit == "F":
    C = float((temperature - 32.0) * 5.0/9.0)
else : 
    print ("Invalid unit - "U","F" ")

if C is not None: 
    print(f"Temperature: {C:.1f}°C / {F:.1f}°F")

    if C < 0:
        print(f"Below 0")
    elif 0 < C <= 15:
        print(f"Cold (0-15)")
    elif 16 <= C <= 25:
        print(f"Comfortable (16-25)") 
    elif 26 <= C <= 35:
        print(f"Hot (26-35)")
    else:
        print(f"Extreme (above 35)")


# Exercise 4: Build a simple login system. Define a correct username and password at the top as constants. 
# Ask the user to enter both. Check: if both match — "Login successful". 
# If username matches but password is wrong — "Wrong password". If username doesn't match — "Username not found".
# Use a ternary operator somewhere in your solution.

USERNAME = 'aditya'
PASSWORD = 'Pass123'

name = input("Enter system login username : ").lower()
password = input("Enter you password to login : ")

if name == USERNAME and password == PASSWORD :
    print("Login successful")
elif name != USERNAME : 
    print("Username not found")
else:
    "password is too short" if len(password) < 7 else print("Wrong password")


# Challenge
# Build a smart electricity bill calculator for a household. 
# Use this slab rate system — this is exactly how real Indian electricity billing works:
# 
# Units 0–100      → Rs. 3.50 per unit
# Units 101–200    → Rs. 5.00 per unit (for the units in this range)
# Units 201–300    → Rs. 7.50 per unit (for the units in this range)
# Units above 300  → Rs. 10.00 per unit (for the units above 300)
# 
# Important: each slab applies only to the units within that range — not to all units. 
# So if someone uses 250 units: first 100 units at Rs.3.50, next 100 units at Rs.5.00, remaining 50 units at Rs.7.50.
# Ask the user for: their name, consumer number, and units consumed. Calculate the bill correctly using slabs. 
# Add 18% GST on top. Print a formatted bill showing each slab's cost, subtotal, GST, and grand total. 
# If units consumed is 0 or negative — print an error.

GST = 18/100

name = input("Enter your name : ").strip().title()
consumer_number = int(input("Enter your dedicated electricity connecction number : "))
units = int(input("Enter the amount of units consumed : "))

print("Electricity Bill Statement")
print(f"Consumer : {name}")
print(f"Bill no : {consumer_number}")
print(f"Units : {units}")

if units <= 0:
    print("Error or no units consumed")
elif 0 <= units <= 100 :
    print(f"Cost of first 100 units is {units * 3.50}")
    sub_total = units * 3.50
    print(f"sub_total is {sub_total}")
    gst_added = sub_total * (GST)
    print(f"GST added is {gst_added}")
    grand_total = sub_total + gst_added
    print(f"Final bill amount is {grand_total}")
elif 100 < units <=200 :
    print(f"Cost of first 100 units is {100 * 3.50}")
    print(f"Cost of remaining units is {(units - 100) * 5.00}")
    sub_total = (100 * 3.50) + (units - 100) * 5.00
    print(f"sub_total is {sub_total}")
    gst_added = sub_total * (GST)
    print(f"GST added is {gst_added}")
    grand_total = sub_total + gst_added
    print(f"Final bill amount is {grand_total}")
elif 200 < units <= 300 :
    print(f"Cost of first 100 units is {100 * 3.50}")
    print(f"Cost of second 100 units is {100 * 5.00}")
    print(f"Cost of remaining units is {(units - 200) * 7.50}")
    sub_total = (100 * 3.50) + (100 * 5.00) + (units - 200) * 7.50
    print(f"sub_total is {sub_total}")
    gst_added = sub_total * (GST)
    print(f"GST added is {gst_added}")

    grand_total = sub_total + gst_added
    print(f"Final bill amount is {grand_total}")
else :
    print(f"Cost of first 100 units is {100 * 3.50}")
    print(f"Cost of second 100 units is {100 * 5.00}")
    print(f"Cost of second 100 units is {100 * 7.50}")
    print(f"Cost of remaining units is {(units - 300) * 10.00}")
    sub_total = (100 * 3.50) + (100 * 5.00) + (100 * 7.50) + (units - 300) * 10.00
    print(f"sub_total is {sub_total}")
    gst_added = sub_total * (GST)
    print(f"GST added is {gst_added}")
    grand_total = sub_total + gst_added
    print(f"Final bill amount is {grand_total}")

