# Variable is used to store the value such that It can be reused again in the code

Mango = 24
Price_each = 5

print(f"The Price of 24 Mangos is {Mango * Price_each}")

Total_Cost = Mango * Price_each

print(f"The Price of 24 Mangos is {Total_Cost}")


age = 27
city = 'Hyderabad'

print(f"{age, city}")

age = 30
city = 'Mumbai'

print(f"updated - {age, city}")


name = "Marvin"
age = 25
score = 98.5
is_active = True

# type() tells you what data type a variable is
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(score))      # <class 'float'>
print(type(is_active))  # <class 'bool'>

# id() tells you the memory address — where Python stored this value
print(id(name))         # something like 2345678901234 — unique number
print(id(age))          # different number


# int() — converts to whole number
price_text = "42"
price_number = int(price_text)
print(price_number + 8)      # 50 — now you can do maths on it

float_to_int = int(9.9)
print(float_to_int)          # 9 — int() does NOT round, it cuts the decimal off

# float() — converts to decimal number
whole = 5
decimal = float(whole)
print(decimal)               # 5.0

text_float = float("3.14")
print(text_float + 1)        # 4.140000000000001

# str() — converts anything to text
age = 25
age_text = str(age)
print("I am " + age_text + " years old")   # I am 25 years old
# without str() this would crash — you cannot add a string and an integer

# bool() — converts to True or False
print(bool(0))        # False  — zero is always False
print(bool(1))        # True   — any non-zero number is True
print(bool(""))       # False  — empty string is False
print(bool("hello"))  # True   — any non-empty string is True
print(bool(None))     # False  — None is always False


name, age, city, is_employed, monthly_salary = "Marvin", 27, "India", False, 0.000

print(name)
print(age)
print(city)
print(is_employed)
print(monthly_salary)


stock = 200
stock -= 45
stock -= 30
stock += 80
stock += 12
print(f"Final stock left for the day is {stock}")


length, width, height = 12, 8, 5
Volume = length * width * height
Surface_area = 2 * ((length * width) + (width * height) + (height * length))

print(Volume)
print(Surface_area)

user_input = "1989"

user_input = int(user_input)

user_input += 35

user_input = str(user_input)

print(user_input)
print(type(user_input))


# You are building a basic billing system for a small restaurant. 
# Define these as constants at the top: GST_RATE = 0.05, SERVICE_CHARGE_RATE = 0.10.
# A table orders: 3 plates of biryani at ₹180 each, 2 cold drinks at ₹60 each, 1 dessert at ₹120. 
# Calculate the subtotal, GST amount, service charge amount, and grand total. 
# Print a formatted bill showing every line. Python must do all the maths — you type no calculated numbers yourself. */


# Constants for billing system
GST_RATE = 0.05
SERVICE_CHARGE_RATE = 0.10

biryani = 180
cold_drinks = 60
desert = 120

subtotal = (3 * biryani) + (2 * cold_drinks) + (1 * desert)

grand_total = subtotal + GST_RATE + SERVICE_CHARGE_RATE

print(grand_total)