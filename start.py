# Imports

import webbrowser
import random 

# Lists

metals = [
    "Aluminum",
    "Arsenic",
    "Barium",
    "Beryllium",
    "Bismuth",
    "Cadmium",
    "Calcium",
    "Chromium",
    "Cobalt",
    "Copper",
    "Gold",
    "Iron",
    "Lead",
    "Magnesium",
    "Manganese",
    "Mercury",
    "Nickel",
    "Platinum",
    "Potassium",
    "Silver",
    "Sodium",
    "Tin",
    "Titanium",
    "Tungsten",
    "Zinc",
]

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Strawberry",
    "Grapes",
    "Watermelon",
    "Pineapple",
    "Mango",
    "Peach",
    "Pear",
    "Cherry",
    "Kiwi",
    "Blueberry",
    "Raspberry",
    "Blackberry",
    "Lemon",
    "Lime",
    "Pomegranate",
    "Cantaloupe",
    "Honeydew",
    "Apricot",
    "Plum",
    "Grapefruit",
    "Coconut",
]

# Vars

ranmet = random.choice(metals)
ranfru = random.choice(fruits)


# Usr Input

times = int(input("How Many Accounts Do You Want to Open?:"))
code = input("What is the Blooket Code?:")

# Launching Browser, Entering Code, and Making Usr

for number in range(times):
    webbrowser.open_new("https://play.blooket.com/play")
