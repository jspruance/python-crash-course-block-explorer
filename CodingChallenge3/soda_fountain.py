# Coding Challenge #3 - Soda Fountain

# Create a list of at least 4 soft drinks
# ex. coke, diet coke, pepsi, sprite

# Create a list of at least 4 sizes
# ex. small, medium, large, extra large

# Create a button label for each combination of drink and size for the fountain
# Ex. "Press here for a large Coke."

# Make sure the soda name is capitalized
# Sort the sodas alphabetically A-Z
# Sort the sodas alphabetically A-Z

drinks = ["coke", "diet coke", "sprite", "pepsi"]
sizes = ["small", "medium", "large", "extra large"]

drinks.sort()

for drink in drinks:
    for size in sizes:
        print(f"Press here for a {size} {drink.title()}.")