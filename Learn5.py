# Everything inside runs 5 times
for i in range(5):
    print(f"Iteration {i}")
    print(f"Square of {i} is {i ** 2}")

# This runs once — after all 5 iterations complete
print("Loop is done")

# Count vowels in a string
vowel_count = 0
consonant = 0
for char in "AdityaPavan" :
    if char.lower() in "aeiou":
        vowel_count += 1
    elif char.isalpha():
        consonant += 1
print(f"Count of Vowels : {vowel_count}")
print(f"Count of Vowels : {consonant}")


# Print each character with its index
word = "AdityaPavan"
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")


# Find first number divisible by both 7 and 11
found = False
for i in range(1, 1000):
    if i % 7 == 0 and i % 11 == 0:
        print(f"First number divisible by 7 and 11: {i}")
        found = True
        break     # stop as soon as we find it

if not found:
    print("No such number found")


# Login attempt limiter
MAX_ATTEMPTS = 3
PASSWORD = "1234566789"

for attempt in range(1, MAX_ATTEMPTS + 1):
    entered = input(f"Attempt {attempt} — Enter password: ")
    if entered == PASSWORD:
        print("Access granted")
        break
    else:
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining.")
else:
    print("Account locked — too many failed attempts")


data = "12,45,abc,67,xyz,89,234.56,34567,4567"
items = data.split(",")
valid_total = 0
for item in items:
    if not item.isdigit():
        print(f"Skipping invalid value: {item}")
        continue
    valid_total += int(item)
print(f"Total of valid numbers: {valid_total}")    # 213


# Input validation — keep asking until valid input received
while True:
    age = input("Enter your age (must be a number): ").strip()
    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    print("Invalid input — please enter a positive number")

print(f"Your age is {age}")


# Multiplication table grid
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j:<3}", end="   ")
    print()     # newline after each row


fruits = ["apple", "banana", "mango", "grape"]

# Without enumerate — manual index tracking
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate — cleaner, more Pythonic
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start index from 1 instead of 0
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# 1. apple
# 2. banana
# 3. mango
# 4. grape


names   = ["Marvin", "Priya", "Arjun"]
scores  = [88, 95, 72]
grades  = ["B", "A", "C","D"]

# Iterate all three simultaneously
for name, score, grade in zip(names, scores, grades):
    print(f"{name:<10} — Score: {score}  Grade: {grade}")

# Output:
# Marvin     — Score: 88  Grade: B
# Priya      — Score: 95  Grade: A
# Arjun      — Score: 72  Grade: C


# You need to repeat 5 times but don't care about i
for _ in range(5):
    print("Hello!")

# _ is convention for "I don't need this value"
# It's a valid variable name — just signals to readers: ignore this




# Exercises
# Exercise 1: Write a loop that prints all numbers from 1 to 50 
# that are divisible by both 3 and 5. Then print how many such numbers exist.

count = 0
for num in range (1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
        count += 1
print(f"Count of all numbers from 1 to 50 that are divisible by both 3 and 5 are {count}")


# Exercise 2: Ask the user for a word. Using a loop, count how many vowels and how many consonants it contains. 
# Print both counts and the percentage of vowels in the word.

word = input("Enter a word : ").strip().lower()

vowel_count = 0
consonants_count = 0

for char in word:
    if char in "aeiou":
        vowel_count += 1
    elif char.isalpha():
        consonants_count += 1
    else:
        print(f"{char} is not a alphabet in word")

print(f"Total number of vowels in word are {vowel_count}")
print(f"Total number of consonants in word are {consonants_count}")
percentage = (vowel_count)/(vowel_count + consonants_count) * 100
print(f"Percentage of vowels in word is {percentage:.1f}")


# Exercise 3: Build a times table printer. Ask the user for a number and how many rows they want. 
# Print the complete times table using a loop. Format it neatly — each row aligned.

TOP     = "╔══════════════════════════════════════════════════╗"
DIVIDER = "╠══════════════════════════════════════════════════╣"
BOTTOM  = "╚══════════════════════════════════════════════════╝"
SIDE    = "║"
InnerWidth = 50

number = int(input("Enter a number and how many rows you want "))

count = 0
print(TOP)
print(f"{SIDE}{f"Table".center(InnerWidth)}{SIDE}")
print(DIVIDER)
while count != number:
    cal = number * count
    count_cal = f"  {number} * {count} = {cal}"
    print(f"{SIDE}{count_cal:<{InnerWidth}}{SIDE}")
    count += 1
print(BOTTOM)


# Exercise 4: Ask the user to enter numbers one at a time. After each entry ask "Add another? (yes/no)". 
# Keep a running total and count. When they say no, print the total, count, and average. Use a while loop.

count = 0
total = 0
while True:
    num = int(input("Enter a number : "))
    count += 1
    total += num
    text = input("Would you like to add another (yes/no)? :").strip().lower()
    if text == 'no':
        break
    
print(f"Count of numbers entered : {count}")
print(f"Total of numbers entered : {total}")
print(f"Average of numbers entered : {total/count}")

# Exercise 5: Write a program that prints this exact pattern using nested loops. 
# The size should be controlled by one variable n = 5:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = int(input("Enter the number to print the pattern : "))
for i in range(num):
    for j in range(i+1):
        print(j+1, end = " ")
    print()



# Challenge
# Build a number guessing game with full loop control. 
# The computer picks a secret number between 1 and 100 (use this for now — secret = 42). 
# The player gets maximum 7 attempts. After each guess tell them "Too high", "Too low", or "Correct!". 
# If they guess correctly — show how many attempts they used and  
#  a rating: 1–2 attempts = "Genius", 3–4 = "Great", 5–6 = "Good", 7 = "Lucky". 
# If they use all 7 attempts without guessing — reveal the number and say "Better luck next time." 
# Also validate input — if the user types something that isn't a number, don't count it as an attempt, 
# just say "Please enter a valid number."
# Requirements:
# 
# Use a while loop with attempt tracking
# Use break when the correct answer is found
# Use continue for invalid input
# Use if/elif for the rating system
# Display remaining attempts after each wrong guess

max_attempts = 7
secret_number = 42
count = 0
won = False

print("You have 7 attempts to guess the number")
while count < max_attempts:
    guess_number = input("Guess and enter a number between 1 - 100 : ").strip()
    if not guess_number.isdigit():
        print("Invalid_input - Please enter a valid number between 1 - 100")
        continue

    guess_number = int(guess_number)

    count += 1
    remaining = max_attempts - count


    if guess_number > secret_number:
        print("Too High")
    elif guess_number < secret_number:
        print("Too Low")
    else:
        print(f"Correct! You guessed it in {count} attempt(s)!")
        won = True
        break
    
    if remaining > 0:
        print(f"Attempts remaining: {remaining}")
    else:
        print()   

if won:
    if (count <= 2):
        print("Genius")
    elif  (count <=4):
        print('Great')
    elif  (count <= 6):
        print('Good')
    else:
        print('Lucky')
    
else:
    print(f"Out of attempts! The secret number was {secret_number}.")
    print("Better luck next time.")