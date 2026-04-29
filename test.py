SIDE = "║"
INNER_WIDTH = 20

name = "Marvin"
city = "Hyderabad"
age = 27

# Try 1 — just text
print(f"{SIDE}{name:<{INNER_WIDTH}}{SIDE}")

# Try 2 — with a label
line = f"  Name : {name}"
print(f"{SIDE}{line:<{INNER_WIDTH}}{SIDE}")

# Try 3 — with a number variable
line = f"  Age  : {age}"
print(f"{SIDE}{line:<{INNER_WIDTH}}{SIDE}")

# Try 4 — what happens if your content is longer than INNER_WIDTH?
long_text = "This is a very long sentence that exceeds the width"
print(f"{SIDE}{long_text:<{INNER_WIDTH}}{SIDE}")