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