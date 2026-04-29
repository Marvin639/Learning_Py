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
consumer_number = input("Enter your dedicated electricity connecction number : ").strip()
units = int(input("Enter the amount of units consumed : "))

TOP     = "╔════════════════════════════════════════════════╗"
DIVIDER = "╠════════════════════════════════════════════════╣"
BOTTOM  = "╚════════════════════════════════════════════════╝"
SIDE    = "║"
INNER_WIDTH = 48

title = "Electricity Bill Statement".center(INNER_WIDTH)
nameline = f"     {'Consumer':<12} :    {name}"
billnoline = f"     {'Billno':<12} :    {consumer_number}"
unitsline = f"     {'Units':<12} :    {units}"

print(TOP)
print(f"{SIDE}{title:<{INNER_WIDTH}}{SIDE}")
print(DIVIDER)
print(f"{SIDE}{nameline:<{INNER_WIDTH}}{SIDE}")
print(f"{SIDE}{billnoline:<{INNER_WIDTH}}{SIDE}")
print(f"{SIDE}{unitsline:<{INNER_WIDTH}}{SIDE}")
print(BOTTOM)

slab1line = f"Slab1 (0 - 100 units @ Rs.3.50 ) :{100 * 3.50} "
slab2line = f"Slab2 (100 - 200 units @ Rs.5.00 ) :{100 * 5.00} "
slab3line = f"Slab3 (200 - 300 units @ Rs.7.50 ) :{100 * 7.50}"
remainedunits = "Cost of remaining units is "

if units <= 0:
    print(f"{SIDE}{'    Error or no units consumed':<{INNER_WIDTH}}{SIDE}")
    print(BOTTOM)
elif 0 <= units <= 100 :
    print(f"{SIDE}   {slab1line:<{INNER_WIDTH}}{SIDE}")
    print(DIVIDER)
    sub_total = units * 3.50
    print(f"{SIDE}   {f'sub_total is {sub_total:<{INNER_WIDTH}}'}{SIDE}")
    gst_added = sub_total * (GST)
    print(f"{SIDE}   {f'GST added is {gst_added:<{INNER_WIDTH}}'}{SIDE}")
    print(DIVIDER)
    grand_total = sub_total + gst_added
    print(f"{SIDE}   {f'Final bill amount is {grand_total:<{INNER_WIDTH}}'}{SIDE}")
    print(BOTTOM)

elif 100 < units <=200 :
    print(f"{SIDE}   {slab1line:<{INNER_WIDTH}}{SIDE}")
    print(f"{SIDE}   {f'remainedunits :{100 * 5.00} :<{INNER_WIDTH - 10}'}{SIDE}")
    print(DIVIDER)
    sub_total = (100 * 3.50) + (units - 100) * 5.00
    print(f"{SIDE}   {f'sub_total is {sub_total:<{INNER_WIDTH}}'}{SIDE}")
    gst_added = sub_total * (GST)
    print(f"{SIDE}   {f'GST added is {gst_added:<{INNER_WIDTH}}'}{SIDE}")
    print(DIVIDER)
    grand_total = sub_total + gst_added
    print(f"{SIDE}   {f'Final bill amount is {grand_total:<{INNER_WIDTH}}'}{SIDE}")
    print(BOTTOM)
elif 200 < units <= 300 :
    print(f"{SIDE}   {slab1line:<{INNER_WIDTH}}{SIDE}")
    print(f"{SIDE}   {slab2line:<{INNER_WIDTH}}{SIDE}")
    print(f"{SIDE}   {f'remainedunits :{100 * 7.50}:<{INNER_WIDTH - 10}'}{SIDE}")
    print(DIVIDER)
    sub_total = (100 * 3.50) + (100 * 5.00) + (units - 200) * 7.50
    print(f"{SIDE}   {f'sub_total is {sub_total:<{INNER_WIDTH}}'}{SIDE}")
    gst_added = sub_total * (GST)
    print(f"{SIDE}   {f'GST added is {gst_added:<{INNER_WIDTH}}'}{SIDE}")
    print(DIVIDER)
    grand_total = sub_total + gst_added
    print(f"{SIDE}   {f'Final bill amount is {grand_total:<{INNER_WIDTH}}'}{SIDE}")
    print(BOTTOM)
else :
    print(f"{SIDE}   {slab1line:<{INNER_WIDTH}}{SIDE}")
    print(f"{SIDE}   {slab2line:<{INNER_WIDTH}}{SIDE}")
    print(f"{SIDE}   {slab3line:<{INNER_WIDTH}}{SIDE}")
    print(f"{SIDE}   {f'remainedunits : {units - 300 * 10.00}:<{INNER_WIDTH}'}:{(units - 300) * 10.00}{SIDE}")
    print(DIVIDER)
    sub_total = (100 * 3.50) + (100 * 5.00) + (100 * 7.50) + (units - 300) * 10.00
    sub_total_c = "sub_total is :"
    print(f"{SIDE}{sub_total_c:<{INNER_WIDTH}}{SIDE}")
    gst_added = sub_total * (GST)
    print(f"{SIDE}   {f'GST added is {gst_added:<{INNER_WIDTH}}'}{SIDE}")
    print(DIVIDER)
    grand_total = sub_total + gst_added
    print(f"{SIDE}   {f'Final bill amount is {grand_total:<{INNER_WIDTH}}'}{SIDE}")
    print(BOTTOM)