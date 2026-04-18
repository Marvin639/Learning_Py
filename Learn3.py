# Strings + Input

Name = input ("What is your name? ");
print(f"Hello {Name}")

print(f"{Name[1]}")

print(f"{Name[-1]}")

print(f"{Name[1:5]}")

print(f"{Name[-3:]}")

print(f"{Name[1:-4]}")

print(f"{Name[::3]}")

print(f"{Name[::-1]}")


print(f"{len(Name)}")

print(f"{Name[len(Name) -1]}")

# String Methods

text = "Hello, World"

# Case methods
print(text.upper())         # "  HELLO, WORLD!  "
print(text.lower())         # "  hello, world!  "
print(text.title())         # "  Hello, World!  " — capitalises first letter of each word
print(text.capitalize())    # "  hello, world!  " — only first character of whole string
print(text.swapcase())      # "  hELLO, wORLD!  " — swaps all cases

# Whitespace removal
print(text.strip())         # "Hello, World!"  — removes spaces from both ends
print(text.lstrip())        # "Hello, World!  " — removes from left only
print(text.rstrip())        # "  Hello, World!" — removes from right only

# CRITICAL: strip() is essential after input() — users accidentally add spaces
name = input("Enter name: ")   # user types "  Marvin  "
name = name.strip()            # now it's cleanly "Marvin"

sentence = "I love Python and Python loves me"

# Finding and replacing
print(sentence.find("Python"))      # 7  — index where "Python" first appears
print(sentence.find("Java"))        # -1 — returns -1 if not found
print(sentence.index("Python"))     # 7  — same as find but crashes if not found
print(sentence.count("Python"))     # 2  — how many times "Python" appears
print(sentence.replace("Python", "coding"))
# "I love coding and coding loves me"
# replace ALL occurrences by default

print(sentence.replace("Python", "coding", 1))
# "I love coding and Python loves me"
# third argument limits how many replacements




# Splitting and joining — extremely important for data work and APIs
csv_line = "Marvin,27,Hyderabad,Python"

parts = csv_line.split(",")     # split by comma
print(parts)                    # ['Marvin', '27', 'Hyderabad', 'Python']
print(parts[0])                 # Marvin
print(parts[2])                 # Hyderabad

# Split by space (default if no argument given)
sentence = "I am learning Python"
words = sentence.split()
print(words)                    # ['I', 'am', 'learning', 'Python']
print(len(words))               # 4 — number of words

# join() — opposite of split, combines a list into a string
words = ["Hyderabad", "is", "a", "great", "city"]
joined = " ".join(words)        # join with space between each
print(joined)                   # "Hyderabad is a great city"

csv = ",".join(["Marvin", "27", "India"])
print(csv)                      # "Marvin,27,India"


# Checking string content — returns True or False
code = "A1B2C3"
name = "Marvin"
number = "12345"

print(code.isdigit())     # False — contains letters
print(number.isdigit())   # True  — only digits
print(name.isalpha())     # True  — only letters
print(code.isalnum())     # True  — letters and numbers (no special chars)
print("  ".isspace())     # True  — only whitespace

# startswith and endswith
email = "marvin@gmail.com"
print(email.startswith("marvin"))    # True
print(email.endswith(".com"))        # True
print(email.endswith(".org"))        # False

filename = "report_2024.pdf"
print(filename.endswith(".pdf"))     # True — useful for file type checking


# Padding and alignment — useful for formatted output
number = "42"
print(number.zfill(5))         # "00042" — pad with zeros to width 5

bill_item = "Biryani"
price = "Rs.540"
print(len(bill_item.ljust(20) + price.rjust(10)))   # left-align + right-align
# "Biryani              Rs.540"

# center() — centre text within a width
print("RECEIPT".center(30))         # "           RECEIPT           "
print("RECEIPT".center(30, "="))    # "===========RECEIPT==========="


# Concatenation — joining strings with +
first = "Hyderabad"
second = " is amazing"
full = first + second
print(full)    # "Hyderabad is amazing"

# You can only concatenate strings with strings — not with numbers
city = "Hyderabad"
population = 10000000
# print(city + population)        # TypeError — crashes
print(city + str(population))     # "Hyderabad10000000" — works with conversion
print(f"{city} has {population} people")  # f-string is cleaner

# Repetition — repeating a string with *
line = "=" * 30
print(line)            # ============================== (30 equals signs)
print("Ha" * 5)        # HaHaHaHaHa
print("-" * 20)        # -------------------- (20 dashes)

# You saw this in the restaurant bill example — now you know how it works



name = "Marvin"
age = 27
score = 98.6789
price = 1500

# Basic — you already know this
print(f"Hello {name}, you are {age}")

# Expressions inside {} — Python evaluates them
print(f"Next year you will be {age + 1}")
print(f"Double your age is {age * 2}")

# Formatting numbers — controlling decimal places
print(f"Score: {score:.2f}")       # 98.68 — 2 decimal places, rounds
print(f"Score: {score:.0f}")       # 99   — 0 decimal places
print(f"Price: {price:,}")         # 1,500 — comma separator for thousands
print(f"Price: {price:010}")       # 0000001500 — pad with zeros to width 10

# Alignment inside f-strings

print(f"{'Item':<15} {'Price':>10}")     # left-align 15, right-align 10
print(f"{'Biryani':<15} {'Rs.540':>10}")
print(f"{'Cold Drink':<15} {'Rs.120':>10}")

# Percentage formatting
rate = 0.185
print(f"Tax rate: {rate:.1%}")     # Tax rate: 18.5% — automatic % conversion

# \n — newline
print("Line 1\nLine 2\nLine 3")
# Line 1
# Line 2
# Line 3

# \t — tab (indentation)
print("Name:\tMarvin")
print("City:\tHyderabad")
# Name:    Marvin
# City:    Hyderabad

# \\ — a literal backslash
print("C:\\Users\\Marvin\\Documents")
# C:\Users\Marvin\Documents

# \' and \" — quotes inside strings
print("He said \"Hello\" to me")    # He said "Hello" to me
print('It\'s a great day')          # It's a great day

# \r — carriage return (moves cursor to start of line — rare but exists)

# Raw strings — r"" — ignores ALL escape characters
# Useful for file paths and regular expressions
normal = "C:\new_folder\test"
print(normal)    # C:
                 # ew_folder	est  ← \n became newline, \t became tab — WRONG

raw = r"C:\new_folder\test"
print(raw)       # C:\new_folder\test ← exactly as written — CORRECT

# Always use raw strings for Windows file paths


# Triple quotes — strings across multiple lines
address = """123 Main Street
Hyderabad
Telangana - 500001
India"""

print(address)
print(len(address))    # counts every character including newlines

# Triple single quotes work the same
note = '''This is a
multiline note
written across three lines'''

# The 'in' operator — checking if something exists inside a string
email = "marvin@gmail.com"
print("gmail" in email)       # True
print("yahoo" in email)       # False
print("@" in email)           # True — useful for basic email validation
print("@" not in email)       # False

sentence = "Python is powerful"
print("powerful" in sentence)   # True
print("weak" in sentence)       # False

# Practical example — simple input validation
user_email = input("Enter your email: ")
if "@" in user_email:
    print("Looks like a valid email format")
else:
    print("That doesn't look like an email — missing @")



print("=" * 40)
print("   PERSONAL PROFILE GENERATOR".center(40))
print("=" * 40)

# Collect inputs
full_name = input("Enter your full name: ").strip().title()
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip().title()
email = input("Enter your email: ").strip().lower()

# Process
first_name = full_name.split()[0]
name_length = len(full_name)
birth_year = 2024 - age
email_valid = "@" in email and "." in email
domain = email.split("@")[-1] if email_valid else "unknown"

# Display profile
print("\n" + "=" * 40)
print("        YOUR PROFILE")
print("=" * 40)
print(f"Full name   : {full_name}")
print(f"First name  : {first_name}")
print(f"Name length : {name_length} characters")
print(f"Age         : {age}")
print(f"Birth year  : {birth_year}")
print(f"City        : {city}")
print(f"Email       : {email}")
print(f"Valid email : {email_valid}")
print(f"Domain      : {domain}")
print("=" * 40)


# Exercise 1: Ask the user for a sentence. Then print: the sentence in uppercase, in lowercase, 
# the number of characters, the number of words, the sentence reversed, and whether the word "Python" appears in it.

Sentence = input("Enter a sentence of your choice: ").strip()

print(f"Uppercase of sentence is {Sentence.upper()}")
print(f"Lowercase of sentence is {Sentence.lower()}")

print(f"Number of Characters in sentence is {len(Sentence)}")

Words_sentence = Sentence.split()
print(f"Number of words: {len(Words_sentence)}")

print(f"Reverse of sentence: {Sentence[::-1]}")

print(f"Word Python in sentence or not: {"Python" in Sentence}")


# Exercise 2: Ask the user for their full name. Extract and print their first name, last name, and initials.
# For example "Marvin Kumar" → first: "Marvin", last: "Kumar", initials: "M.K."

Name = input("Enter your full name (First name and Last name only) : ").strip()
fullname = Name.split()

firstname = fullname[0]
lastname = fullname[1]

firstname_initial = firstname[0].upper()
lastname_initial = lastname[0].upper()

print(f"first name : {firstname}")
print(f"last name : {lastname}")
print(f"initials are {firstname_initial}.{lastname_initial}.")

# Exercise 3: Ask the user for a phone number as text.
# Check if it contains only digits. If yes, print it formatted as +91-XXXXX-XXXXX. 
# If no, print "Invalid phone number — only digits allowed."

Phonenumber = input("Enter your phone number : ").strip()

if Phonenumber.isdigit() and len(Phonenumber) == 10:
    print(f"+91-{Phonenumber[:5]}-{Phonenumber[5:]}")
else:
    print(f"Invalid phone number — only digits allowed.")


# Exercise 4: Ask the user to enter a CSV line of 4 items separated by commas — like apple,banana,mango,grape. 
# Split it, print each item on its own line with its index number, then join them back with " | " and print that too.

csvfile  = input("Enter a CSV line of 4 items separated by commas — like apple,banana,mango,grape. ").split(",")
print(f"{csvfile[0]}\n{csvfile[1]}\n{csvfile[2]}\n{csvfile[3]}")

combineddata = " | ".join(csvfile)

print(f"{combineddata}")



# Challenge
# Build an interactive name card generator. Ask the user for their full name, job title, company, email, and phone number. Then print a formatted name card like this:
# ╔══════════════════════════════════════╗
# ║           PROFESSIONAL CARD          ║
# ╠══════════════════════════════════════╣
# ║  Name    : Marvin Kumar              ║
# ║  Title   : AI/ML Engineer            ║
# ║  Company : TechCorp India            ║
# ║  Email   : marvin@techcorp.com       ║
# ║  Phone   : +91-98765-43210           ║
# ╚══════════════════════════════════════╝
# Requirements:
# 
# Name must display in title case regardless of how they typed it
# Email must display in lowercase regardless of how they typed it
# Strip all whitespace from every input
# Phone must contain only digits — if not, display "Invalid" instead
# Each line inside the card must be exactly the same width with ║ on both sides

full_name = input("Enter your full name: ").strip().title()
job_title = input("Enter your job title: ").strip()
company = input("Enter your company name: ").strip()
email = input("Enter your email: ").strip().lower()
phone_number = input("Enter your phone number: ").strip()

# Phone validation
if phone_number.isdigit() and len(phone_number) == 10:
    phone_display = f"+91-{phone_number[:5]}-{phone_number[5:]}"
else:
    phone_display = "Invalid"

# Card constants
TOP     = "╔══════════════════════════════════════╗"
DIVIDER = "╠══════════════════════════════════════╣"
BOTTOM  = "╚══════════════════════════════════════╝"
SIDE    = "║"
INNER_WIDTH = 38

# Title line — center "PROFESSIONAL CARD" within INNER_WIDTH
title_content = "PROFESSIONAL CARD".center(INNER_WIDTH)

# Content lines — use the f"  {label:<9}: {value}" pattern
name_line    = f"   {'Name':<9}: {full_name}"
title_line   = f"   {'Title':<9}: {job_title}"
company_line = f"   {'Company':<9}: {company}"
email_line   = f"   {'Email':<9}: {email}"
phone_line   = f"   {'Phone':<9}: {phone_display}"

# Print the card
print(TOP)
print(f"{SIDE}{title_content}{SIDE}")
print(DIVIDER)
print(f"{SIDE}{name_line:<38}{SIDE}")
print(f"{SIDE}{title_line:<38}{SIDE}")
print(f"{SIDE}{company_line:<38}{SIDE}")
print(f"{SIDE}{email_line:<38}{SIDE}")
print(f"{SIDE}{phone_line:<38}{SIDE}")
print(BOTTOM)